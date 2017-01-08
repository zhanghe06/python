## Docker

基础概念

- Images（镜像）：Docker可以通过Pull和Push命令构建对象到服务中心
- Containers（容器）：Docker可以通过Start/Stop命令管理容器的生命周期
- Logging（日志）：Docker可以通过stdout，stderro捕获输出所有的容器内部信息
- Volumes（存储）：Docker可以创建和管理容器的相关文件存储
- Networking（网络）：Docker可以创建管理虚拟的接口和内部所有容器之间的网络桥接
- RPC：Docker服务器提供允许外部程序去控制所有容器的行为的API


配置加速器

注册：[配置 Docker 加速器](https://www.daocloud.io/mirror#accelerator-doc)

配置：
```
$ curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sudo sh -s http://12248bc3.m.daocloud.io
```


安装

参考：https://docs.docker.com/engine/installation/

入门：http://tuxknight-notes.readthedocs.io/en/latest/docker/docker_command.html

笔记：https://blog.phpgao.com/docker-note1.html#%E6%9E%84%E5%BB%BA%E9%95%9C%E5%83%8F

```
$ curl -sSL https://get.daocloud.io/docker | sh
```

```
If you would like to use Docker as a non-root user, you should now consider
adding your user to the "docker" group with something like:

  sudo usermod -aG docker zhanghe

Remember that you will have to log out and back in for this to take effect!
```


检查 docker 守护进程状态
```
$ sudo service docker status
```

```
docker start/running, process 1650
```


获取当前 docker 版本
```
$ sudo docker version
```

```
Client:
 Version:      1.12.1
 API version:  1.24
 Go version:   go1.6.3
 Git commit:   23cf638
 Built:        Thu Aug 18 05:22:43 2016
 OS/Arch:      linux/amd64

Server:
 Version:      1.12.1
 API version:  1.24
 Go version:   go1.6.3
 Git commit:   23cf638
 Built:        Thu Aug 18 05:22:43 2016
 OS/Arch:      linux/amd64
```


查看当前 docker 信息
```
$ sudo docker info
```

```
Containers: 0
 Running: 0
 Paused: 0
 Stopped: 0
Images: 0
Server Version: 1.12.1
Storage Driver: aufs
 Root Dir: /var/lib/docker/aufs
 Backing Filesystem: extfs
 Dirs: 0
 Dirperm1 Supported: false
Logging Driver: json-file
Cgroup Driver: cgroupfs
Plugins:
 Volume: local
 Network: host null bridge overlay
Swarm: inactive
Runtimes: runc
Default Runtime: runc
Security Options: apparmor
Kernel Version: 3.13.0-97-generic
Operating System: Ubuntu 14.04.5 LTS
OSType: linux
Architecture: x86_64
CPUs: 4
Total Memory: 7.756 GiB
Name: ThinkPad-L421
ID: XACY:MKNQ:Q7Q7:7JBI:JH3W:GISV:DIZO:QS7U:ERD2:XQHB:5JRK:3NCW
Docker Root Dir: /var/lib/docker
Debug Mode (client): false
Debug Mode (server): false
Registry: https://index.docker.io/v1/
WARNING: No swap limit support
Insecure Registries:
 127.0.0.0/8
```


搜索可用 docker 镜像
```
$ sudo docker search ubuntu
```

```
NAME                              DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
ubuntu                            Ubuntu is a Debian-based Linux operating s...   4758      [OK]       
ubuntu-upstart                    Upstart is an event-based replacement for ...   66        [OK]       
rastasheep/ubuntu-sshd            Dockerized SSH service, built on top of of...   42                   [OK]
ubuntu-debootstrap                debootstrap --variant=minbase --components...   27        [OK]       
torusware/speedus-ubuntu          Always updated official Ubuntu docker imag...   27                   [OK]
nickistre/ubuntu-lamp             LAMP server on Ubuntu                           9                    [OK]
nuagebec/ubuntu                   Simple always updated Ubuntu docker images...   8                    [OK]
nickistre/ubuntu-lamp-wordpress   LAMP on Ubuntu with wp-cli installed            6                    [OK]
nimmis/ubuntu                     This is a docker images different LTS vers...   5                    [OK]
maxexcloo/ubuntu                  Base image built on Ubuntu with init, Supe...   2                    [OK]
darksheer/ubuntu                  Base Ubuntu Image -- Updated hourly             1                    [OK]
admiringworm/ubuntu               Base ubuntu images based on the official u...   1                    [OK]
jordi/ubuntu                      Ubuntu Base Image                               1                    [OK]
datenbetrieb/ubuntu               custom flavor of the official ubuntu base ...   0                    [OK]
lynxtp/ubuntu                     https://github.com/lynxtp/docker-ubuntu         0                    [OK]
webhippie/ubuntu                  Docker images for ubuntu                        0                    [OK]
life360/ubuntu                    Ubuntu is a Debian-based Linux operating s...   0                    [OK]
esycat/ubuntu                     Ubuntu LTS                                      0                    [OK]
widerplan/ubuntu                  Our basic Ubuntu images.                        0                    [OK]
teamrock/ubuntu                   TeamRock's Ubuntu image configured with AW...   0                    [OK]
ustclug/ubuntu                    ubuntu image for docker with USTC mirror        0                    [OK]
konstruktoid/ubuntu               Ubuntu base image                               0                    [OK]
dorapro/ubuntu                    ubuntu image                                    0                    [OK]
uvatbc/ubuntu                     Ubuntu images with unprivileged user            0                    [OK]
gopex/ubuntu                      Automatic build of GoPex customization ove...   0                    [OK]
```


下载 ubuntu 官方镜像
```
$ sudo docker pull ubuntu
```

下载中
```
Using default tag: latest
latest: Pulling from library/ubuntu
ff1f1f1de862: Downloading [===========================>                       ] 27.43 MB/49.79 MB
0c7b035e2a1a: Download complete 
ac8ee255ff41: Download complete 
bf3d47be55f8: Download complete 
22a909724a97: Download complete
```
下载完成
```
Using default tag: latest
latest: Pulling from library/ubuntu
ff1f1f1de862: Pull complete 
0c7b035e2a1a: Pull complete 
ac8ee255ff41: Pull complete 
bf3d47be55f8: Pull complete 
22a909724a97: Pull complete 
Digest: sha256:3235a49037919e99696d97df8d8a230717272d848ee4ddadbca8d54f97ee30cb
Status: Downloaded newer image for ubuntu:latest
```


查看当前镜像列表
```
$ sudo docker images
```

```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              latest              45bc58500fa3        6 days ago          126.9 MB
hello-world         latest              c54a2cc56cbb        12 weeks ago        1.848 kB
```


显示所有容器
```
$ sudo docker ps        # 显示状态为运行中（Up）的
$ sudo docker ps -a     # 显示所有容器,包括运行中（Up）的和退出的(Exited)
```

```
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                    PORTS               NAMES
accbcfa5e2e6        hello-world         "/hello"            15 hours ago        Exited (0) 15 hours ago                       angry_bhabha
```


删除容器
```
$ sudo docker rm angry_bhabha
```

删除镜像
```
$ sudo docker rmi hello-world
```

删除所有正在运行的容器
```
$ sudo docker kill $(docker ps -a -q)
```

删除所有已经停止的容器
```
$ sudo docker rm $(docker ps -a -q)
```

删除所有镜像
```
$ sudo docker rmi $(docker images -q)
```

构建镜像
```
sudo docker build --rm=true -t zh/redis .

sudo docker build --rm=true -t zh/redis -f redis.dockerfile
```
