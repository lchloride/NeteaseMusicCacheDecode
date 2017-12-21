# 网易云音乐缓存解码

## 版本
- v1.2_pycmd (更新于 东部标准时间 2017年12月20日)

## 功能

- 将网易云音乐的uc!缓存文件转换成MP3音乐文件。
- 兼容Python2与Python3，可在支持Python(如：MacOSX和Ubuntu)的系统中使用。
- 使用命令行调用，没有图形界面。*命令行的简单使用方法参见最后。*

## 使用说明
1. 使用命令格式：
- python nemusiccd.py \<source\> [destination]

  或

- python3 nemusiccd.py \<source\> [destination]

2. \<source\>指的是缓存文件，需要填入缓存文件全路径。如果路径中存在空格，请用双引号将整个<source>部分包住。
   全路径格式如：E:\489970551-192000-1c89dba007e8df107be88e74f1c071d1.mp3.uc!。
   
   通常，缓存文件的扩展名是uc!。如果不指定路径只指定了文件名，程序在**命令行当前目录**下寻找文件。

3. [destination]指的是输出文件，需要填入缓存文件的全路径。如果不指定该参数，则输出文件和输入文件同名且在同目录下。

   如果路径中存在空格，请用双引号将整个[destination]部分包住。

   如果不指定路径只指定文件名，则文件保存在**命令行当前目录**下。

4. 请注意输入输出文件的路径权限，使用系统路径需要超级用户权限。为了避免不必要的误操作，不建议在系统路径中进行操作。

## 常见问题

1. 提示“[Errno 2] IOError xxx”

   请检查指定路径下是否存在该文件，文件路径及文件名是否正确。

2. 提示“[Errno 21] Is a directory: xxx”

   请检查应该填写文件名的地方是否填写了路径。
   
3. 提示“[Errno 1] Operation not permitted: xxx”

   请检查现在登陆的用户是否有读写指定路径的权限。
   像“/system/Library/test.mp3”路径的文件一定是需要超级用户权限的。
   
4. 程序运行的时候为什么光标在闪

   这是因为输出进度数值的原因。
   
5. 程序永久有效吗

   当然不会，如果网易哪天又换了一种编码方式，程序就自然失效了。

## 声明
本程序为免费程序，分享请注明出处，尊重开发者劳动。本程序传播过程中造成的任何形式的后果与开发者无关。

## 项目地址
Github：github.com/lchloride/NeteaseMusicCacheDecode

如有问题请在issue中留言。

---

## 命令行基础
这是一个简单的教程，主要说的是如何使用命令行来运行程序。如果您使用的是MacOSX、Ubuntu或其他\*nix系统，您应该掌握命令行的使用方法。

### 命令行是什么
平常我们使用的程序，不论是Word、网易云音乐还是游戏，它们都有一个或多个可以交互的视图窗口。我们可以输入，看到输出；点击按钮，执行命令。我们称这样的程序具有图形界面。
那么，没有图形界面的程序如何运行呢？这就需要命令行工具了。通常，每个操作系统都具有命令行工具，例如Windows平台命令行是**命令提示符(cmd)**，Ubuntu和MacOSX平台都是**终端(terminal)**。
命令行没有图形界面，所有的操作都通过输入命令完成，结果会一行行地输出到屏幕上。由于界面丑陋，所以命令行还有一个俗名，黑窗口。
(不过，默认下Windows的命令提示符是黑窗口，Ubuntu的终端是紫色的，MacOSX的终端是白色，并且很多命令行的背景颜色都是可以调整的)

Windows的命令提示符通常是这样：

![Windows Command Line](https://s3browser.com/images/s3cmd/s3browser-con-without-args.png)

MacOSX的终端通常是这样：

![MacOSX Terminal](https://cdn2.macworld.co.uk/cmsdata/features/3608274/Screen_Shot_2015-04-13_at_11.48.16_thumb.png)

Ubuntu的终端通常是这样:

![Ubuntu Terminal](http://ubuntuhandbook.org/wp-content/uploads/2016/05/ubuntu-terminal.jpg)

### 运行程序

1. 首先打开命令行工具

2. 使用cd命令将当前目录切换到程序所在目录下
- 格式是：cd "目录全路径"
- 使用双引号将路径括起来以防止路径中的空格被错误解析
- 对于Windows系统，切换前后路径不在一个硬盘下的情况，需要额外使用"盘符:"命令(如c:)来切换硬盘分区

3. 路径切换好后，可用dir(Windows)或ls(MacOSX, Ubuntu等)命令查看当前路径下的全部文件。确认当前目录下存在要执行的程序。

4. 按照格式要求输入命令

- 例如`python nemusiccd.py <source> [destination]` 我们可以输入`python nemusiccd.py E:\cache.mp3.uc! F:\test.mp3`然后键入回车来执行这条命令。
- 注意，如果路径中存在空格，则整个路径要用双引号括起来，比如：`python nemusiccd.py "E:\space directory\cache.mp3.uc!" "F:\test.mp3"`
- 对于非Windows系统，路径中的分隔符是"/"，不是"\\"
