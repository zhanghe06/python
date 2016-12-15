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
