# python+赛尔号 登陆器教程

## 1、安装

这个环境比较。。反正就是不断试错最终得出一个成功的套路

我们首先修改一下conda环境，改成win32

在cmd窗口输入命令`set CONDA_FORCE_32BIT=1`

由于pyqt5与python默认环境可能存在一些问题，所以我们创建一个新的32位python的虚拟环境

`conda create --name pyqt32 python=3.6`

创建好后我们激活环境

`conda activate pyqt32`

紧接着，我们需要在虚拟环境中安装pip

`conda install pip`

安装完成后，我们就装最新版的pyqt5

`pip install pyqt5`

由于pyqt5.9以上的版本不自带PyqtWebEngine，我们需要再安装一下这个包

`pip install PyQtWebEngine`

然后还有一个pyqt的工具包

`pip install pyqt-tools`

接下来把几个库配置一下`numpy`,`pywin32`

```
pip install numpy
pip install pywin32
pip install pycaw
```

大致这样环境就配好了，现在可以解释一下为什么了，因为dm.dll跟变速的dll都是32位系统的，我们如果用默认的Python（64位）就会出现各种报错，为了避免这种尴尬的事儿，所以我们就换成32位的Python

## 2、运行

在cmd窗口切换到下载好的兔儿爷赛尔号登陆器源码目录，输入`python 赛尔号启动.py`

游戏就成功载入了，这是星小夜登陆器开源源码的最后一个版本，之前已经有c#，c++，易语言了，现在加上python，目的的话，就是希望更多的人，能通过赛尔号喜欢上编程吧，或许也能成为一个谋生的技俩，也说不准