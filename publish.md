## 团队项目中的代码发布流程


一、新建项目（从最新的 开发分支 拉出 个人分支）：
```
git checkout [开发-分支]
git pull origin [开发-分支]
git checkout -b [个人-分支]
```

二、进入开发流程--（开发人员）

三、开发完毕，将最新的 开发分支 合并到 个人分支
```
git checkout [开发-分支]
git pull origin [开发-分支]
git checkout [个人-分支]
git merge [开发-分支]
git push origin [个人-分支]
```

四、测试环境拉取远程分支
```
git pull origin [个人-分支]:[个人-分支]
git checkout [个人-分支]
```

五、进入测试流程--（测试人员）

六、测试完成，将 个人分支 合并到 开发分支
```
git checkout [开发-分支]
git pull origin [开发-分支]
//先自己ide比较代码，再合并
git merge [个人-分支]
git push origin [开发-分支]
```

七、准备上线: 从 开发分支 合并到 master 分支 ,
并且打上 发布标签 release-2015xxxx 年月日 (备注本次上线的内容)
```
git checkout master
git pull origin master
//先自己ide比较代码，再合并
git merge [开发-分支]
git tag -a release-[2015-xx-xx] -m '[上线描述]'
git push origin master
git push origin --tags
```

八、检查标签
```
//查看本地标签
git tag
//查看远程标签
git ls-remote
```

特别注意：结束以上流程，马上从master切到自己下一个 个人分支。
