# Youtube_downloader
Console program for downloading videos from youtube

## Example
~~~
$python3 ./YouTubeLoader.py 

usage: YouTubeLoader.py [-h] [-n NAME] [-md] [-m]
                        [-r {240,360,480,720,240p,360p,480p,720p}]
                        link path

positional arguments:
  link                  link to content
  path                  save to path

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name of file. Default title from file
  -md, --make_dir       create a path if it does not exist
  -m, --music           download only music
  -r {240,360,480,720,240p,360p,480p,720p}, --resolution {240,360,480,720,240p,360p,480p,720p}
                        resolution of video


$python3 ./YouTubeLoader.py link_with_content path_to_save -m #download only audio file

$python3 ./YouTubeLoader.py link_with_content path_to_save -n some_name -r 240
~~~
