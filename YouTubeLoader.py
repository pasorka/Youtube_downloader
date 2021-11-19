import argparse
from pytube.cli import on_progress
from pytube import YouTube, Stream
from pytube.exceptions import VideoUnavailable
import os



def get_argument() -> argparse.Namespace:
    """
    parser for command line arguments

    Returns:
        argparse.Namespace: arguments
    """

    parser = argparse.ArgumentParser()
    
    
    # Position arg
    parser.add_argument('link', help='link to content')
    parser.add_argument('path', help='save to path')
    
    # Optional arg
    parser.add_argument('-n', '--name', help='Name of file. Default title from file', default='')
    parser.add_argument('-md', '--make_dir', action='store_true', help='create a path if it does not exist')
    parser.add_argument('-m', '--music', action='store_true', help='download only music')
    parser.add_argument('-r', '--resolution', choices=['240', '360', '480', '720',
                                                       '240p', '360p', '480p', '720p'],
                      help='resolution of video', default='720p')
    
    
    
    args = parser.parse_args()
    
    if not ('r' == args.resolution[-1]):
        args.resolution += 'p'

    return args


def download(link: str, path: str, name: str = '', music: bool= False, resolution: str = '') -> None:
    """
    Downloads video or music from YouTube

    Args:
        link (str): link to content 
        path (str): file save path
        name (str, optional): name of file. Default title from file.
        music (bool, optional): download only music. Defaults to False.
        resolution (str, optional): resolution of video. Default highest resolution.
    """
    
    
    yt: YouTube = YouTube(link, on_progress_callback=on_progress)

    if not name:
        name: str = yt.title
    
    if music:
        content: Stream = yt.streams.get_audio_only()
        format_file: str = '.mp3'
    
    else:
        content: Stream = yt.streams.get_by_resolution(resolution)
        
        if content is None:
            content = yt.streams.get_highest_resolution()
            
        format_file: str = '.mp4'
    
    name = name[:25]   
    name += format_file
    
    content.download(path, name)





def main():
    arguments: argparse.Namespace = get_argument()
    
    path_exists: bool = os.path.exists(arguments.path)
    assert (path_exists and arguments.make_dir) or path_exists, 'Path does not exists'
    
    print('Ожидается скачивание файла')
    
    download(link= arguments.link, 
            path= arguments.path,
            name= arguments.name,
            music= arguments.music,
            resolution= arguments.resolution)

    print('Скачивание файла завершенно')    
    
    
    
    
    
if __name__ == '__main__':
    main()
