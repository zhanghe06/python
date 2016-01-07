## 修改 GitHub commit 的作者信息

GitHub 客户端迁移之后，发现 contribution graph 提交代码之后还是空白，想起来可能是作者信息没有设置正确

查看 git log 记录，发现邮箱果然不是 GitHub 账号的邮箱

修改配置
```
$ git config user.name "Zhang He"
$ git config user.email "zhang_he06@163.com"
```

查看配置
```
$ git config -l
```
最下面两条
```
user.name=Zhang He
user.email=zhang_he06@163.com
```

修改之后只能对以后的提交有效，之前的提交记录还是没有变

下面修改 git log 作者信息

首先基于代码仓库克隆一个全新并且空的版本库
```
$ git clone --bare https://github.com/zhanghe06/python.git
```

然后进入目录创建以下替换脚本，执行后推送修改；
过程中提示输入 GitHub 用户名 密码
```
$ cd python.git/
$ vim git-author-rewrite.sh
$ chmod a+x git-author-rewrite.sh
$ ./git-author-replace.sh
$ git push --force --tags origin 'refs/heads/*'
Username for 'https://github.com': 
Password for 'https://zhanghe06@github.com': 
```

清除临时 clone
```
$ cd ..
$ rm -rf python.git
```

此时远程仓库作者已经修改，本地不能直接拉取，否则 log 会合并；
现在需要删除本地版本库，重新从远程仓库克隆到本地
```
$ rm -rf python
$ git clone git@github.com:zhanghe06/python.git
```
进入项目目录并按上面的方案修改配置


git-author-rewrite.sh

    #!/bin/sh
    
    git filter-branch --env-filter '
    OLD_EMAIL="zhanghe@xxxx.com"
    CORRECT_NAME="Zhang He"
    CORRECT_EMAIL="zhang_he06@163.com"
    if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
    then
        export GIT_COMMITTER_NAME="$CORRECT_NAME"
        export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
    fi
    if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
    then
        export GIT_AUTHOR_NAME="$CORRECT_NAME"
        export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
    fi
    ' --tag-name-filter cat -- --branches --tags


只需替换以下3个变量：
```
OLD_EMAIL
CORRECT_NAME
CORRECT_EMAIL
```

参考链接：[https://help.github.com/articles/changing-author-info/](https://help.github.com/articles/changing-author-info/)
