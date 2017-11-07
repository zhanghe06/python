## 安装 Command Line Tools

```
✗ xcode-select --install
或者自动安装：
✗ brew doctor
```


## sublime

[下载](https://www.sublimetext.com/3)

[文档](http://www.sublimetext.com/docs/3/)

[Package Control](https://packagecontrol.io/installation)


## 插件安装

shift + cmd + p 打开命令面板

输入 “Package Control: Install Package” 命令

输入安装插件的简写或全拼,找到后回车安装


JSCS-Formatter 依赖 nodejs

```
✗ brew install node
✗ node -v
v6.7.0
```


终端为subl添加软链
```
ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl
```

破解(没有尝试，没有验证)
```
✗ cd /Applications/Sublime Text.app/Contents/MacOS
✗ vim Sublime\ Text
:%!xxd
/Thanks
/3342
:s/3342/3242
:%!xxd -r
:wq
```


打开Sublime

help >> enter licence

将以下Licence贴进去

```
--BEGIN LICENSE--
China
Unlimited User License
EA7E-2861
BE67D2175D3569FDAB9EB5340FAD2822
E7B56B3397A76AA9FBE8AC3D3C65918B
DFC28F2EA158140D9E07853D594818EB
3A237B2E8E98ED257C269548F50EDA34
EF0C7F72D8917DB538A0245E46BFD6B1
85F4EDE331F253530ED67A5C19E92399
04C5F4A1AF4AF3DB5EC49C1FEE17CA76
7E369F8AAE4AC6C6E756B5882E1608B9
--END LICENSE--
```

提示：Thanks for purchasing! 成功！


## tree

显示文件树形结构
```
✗ brew install tree
✗ tree
# 解决中文乱码
✗ tree -N
# 组合（仅显示目录，目录深度2）
✗ tree -N -d -L 2
```

## 磁盘使用

显示磁盘使用情况
```
✗ du -h -d 2
```

## 提取系统安装文件
```
# 首先 App Store 下载完整系统文件
✗ cd /Applications/
✗ sudo mv Install\ macOS\ Sierra.app ~/tools/
```
然后可以制作U盘启动盘


## at

Mac 环境下，必须先启动 atrun (默认是关闭的)
```bash
man atrun  # 查看文档
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.atrun.plist  # 开启服务
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.atrun.plist  # 关闭服务
```

定时任务
```bash
echo `date`
at now + 1 minute <<< "/bin/echo `date` > /tmp/time.log"
at now + 10 minutes <<< "/bin/echo `date` > /tmp/time.log"   # 创建任务
at -l       # 列出任务
at -c 1     # 显示任务内容
```


## Mac 键盘图标与对应快捷按键

键盘图标 | 快捷按键
| --- | --- |
⌘ | Command () win
⌃ | Control ctrl
⌥ | Option alt
⇧ | Shift
⇪ | Caps Lock


### 文件校验
Mac md5 替代 md5sum
```
$ md5 .bashrc
MD5 (.bashrc) = 1f98b8f3f3c8f8927eca945d59dcc1c6
$ shasum .bashrc
c4d853993e323432cb84359de2c319b9a767b729  .bashrc
```


## Mac 安装 matplotlib

```bash
pip install matplotlib
```
测试导入报错
```
Traceback (most recent call last):
  File "wechat_jump_iOS_py3.py", line 3, in <module>
    import matplotlib.pyplot as plt
  File "/Users/zhanghe/code/wechat_jump_game/wechat_jump_game.env/lib/python3.6/site-packages/matplotlib/pyplot.py", line 116, in <module>
    _backend_mod, new_figure_manager, draw_if_interactive, _show = pylab_setup()
  File "/Users/zhanghe/code/wechat_jump_game/wechat_jump_game.env/lib/python3.6/site-packages/matplotlib/backends/__init__.py", line 60, in pylab_setup
    [backend_name], 0)
  File "/Users/zhanghe/code/wechat_jump_game/wechat_jump_game.env/lib/python3.6/site-packages/matplotlib/backends/backend_macosx.py", line 17, in <module>
    from matplotlib.backends import _macosx
RuntimeError: Python is not installed as a framework. The Mac OS X backend will not be able to function correctly if Python is not installed as a framework. See the Python documentation for more information on installing Python as a framework on Mac OS X. Please either reinstall Python as a framework, or try one of the other backends. If you are using (Ana)Conda please install python.app and replace the use of 'python' with 'pythonw'. See 'Working with Matplotlib on OSX' in the Matplotlib FAQ for more information.
```

解决办法:
```bash
echo "backend: TkAgg" > ~/.matplotlib/matplotlibrc
```


## iphone 真机调试

https://github.com/openatx/facebook-wda

Install python wda client
```bash
pip install --pre facebook-wda
```

https://github.com/Carthage/Carthage
```bash
brew install carthage
```

iOS 真机如何安装 WebDriverAgent
```bash
git clone https://github.com/facebook/WebDriverAgent
cd WebDriverAgent
./Scripts/bootstrap.sh
```
安装完成, 双击`WebDriverAgent.xcodeproj`文件

设置证书, 参考: 
- https://testerhome.com/topics/7220
- https://testerhome.com/topics/8085


```bash
brew install libimobiledevice
```

端口转发
```bash
iproxy --help
usage: iproxy LOCAL_TCP_PORT DEVICE_TCP_PORT [UDID]

iproxy 8100 8100
```

验证服务状态
```
curl http://localhost:8100/status
{
    "value": {
        "state": "success",
        "os": {
            "name": "iOS",
            "version": "11.2.1"
        },
        "ios": {
            "simulatorVersion": "11.2.1",
            "ip": "192.168.3.44"
        },
        "build": {
            "time": "Dec 30 2017 21:05:55"
        }
    },
    "sessionId": "BC69BB2F-945F-4EBC-B94B-5E8C01696F82",
    "status": 0
}
```
