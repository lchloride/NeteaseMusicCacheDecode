# NetEase Music Cache Decode 网易云音乐缓存解码 

**Note: This English version of readme may not be latest. It is recommended to read Chinese(Simplified) version if possible.**

**注意: 这份英文的readme文档不一定是最新版本。如果可能，建议阅读(简体)中文版本。**

## Version
- v1.2_pycmd (Built on Dec.20, 2017 EST)

## Features

- Convert cache file of uc! format to music file of mp3 format
- Be compatible with Python2 and Python3, validate on any system supporting Python (like MacOSX and Ubuntu)
- Work under command line, no GUI

## Instructions
1. Usage of commands：
- python nemusiccd.py \<source\> [destination]      

  OR

- python3 nemusiccd.py \<source\> [destination]     

2. \<source\> indicates cache file and full path is preferable. 
   If whitespace exists in path, the \<source\> part must be wrapped using double quotation marks.
   Full path is like E:\489970551-192000-1c89dba007e8df107be88e74f1c071d1.mp3.uc!。
   
   Usually, cache file has filename extension of uc!. 
   If filename is specified without path, program would find this file at **directory of command line**. 

3. [destination] indicates output file and full path is preferable.
   If this parameter is ignored, output file is located at same directory of source file and has the same name of source file.

   If whitespace exists in path, the [desination] part must be wrapped using double quotation marks.

   If filename is specified without path, output file will save at the directory of **directory of command line**.
  

4. Please be careful of file permission. System path requires super user permission. It is not recommended to run program at system directory.

## FAQs

1. Exception: “[Errno 2] IOError xxx”

   Please check existence of specified files.

2. Exception: “[Errno 21] Is a directory: xxx”

   Please check whether the place for filename is fulfilled with directory path.
   
3. Exception: “[Errno 1] Operation not permitted: xxx”

   Please check whether current user can access specified file or path.
   
4. Why the cursor is always flickering?

   Because of progress info displaying.
   
5. Is it valid forever?

   Of course not, it will expire when NetEase changes to another encoding approach.

## Announcement
This project is free to obtain. Please assign the link of project to your sharing content.
All consequences have no association with developer during its sharing procedures.

## Project Link
Github：github.com/lchloride/NeteaseMusicCacheDecode

Please leave message at issue if there are something strange. All kinds of advices are welcomed.

