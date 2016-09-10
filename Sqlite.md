## Sqlite

安装
```
$ sudo apt-get install sqlite3
```

查看版本
```
$ sqlite3 -version
3.8.2 2013-12-06 14:53:30 27392118af4c38c5203a04b8013e1afdb1cebd0d
```

进入sqlite
```
$ sqlite3
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> 
```

查看帮助：
```
sqlite> .help
```

显示数据库信息；包含当前数据库的位置
```
sqlite> .database
```

显示表名称，没有表则不显示
```
sqlite> .tables
```

查看所有表的创建语句：
```
sqlite> .schema
```

查看指定表的创建语句：
```
sqlite> .schema table_name
```

改变输出格式，具体如下
```
sqlite> .mode list|column|insert|line|tabs|tcl|csv
```

生成形成数据库表的 SQL 脚本
```
sqlite> .dump
```

退出
```
sqlite>.quit
或
sqlite>.exit
或
Ctrl + d
```

sqlite3 支持的数据类型 
```
NULL：标识一个NULL值
INTEGER：整数类型
REAL：浮点数
TEXT：字符串
BLOB：二进制数
```

但实际上，sqlite3 也接受如下的数据类型：
```
smallint 16 位元的整数。
integer 32 位元的整数。
decimal(p,s) p 精确值和 s 大小的十进位整数，精确值p是指全部有几个数(digits)大小值，s是指小数点後有几位数。如果没有特别指定，则系统会设为 p=5; s=0 。
float  32位元的实数。
double  64位元的实数。
char(n)  n 长度的字串，n不能超过 254。
varchar(n) 长度不固定且其最大长度为 n 的字串，n不能超过 4000。
graphic(n) 和 char(n) 一样，不过其单位是两个字元 double-bytes， n不能超过127。这个形态是为了支援两个字元长度的字体，例如中文字。
vargraphic(n) 可变长度且其最大长度为 n 的双字元字串，n不能超过 2000
date  包含了 年份、月份、日期。
time  包含了 小时、分钟、秒。
timestamp 包含了 年、月、日、时、分、秒、千分之一秒。
```

输出当前时间（格林威治时间）
```
sqlite> select datetime('now'); 
```

输出当前时间（本地时间）
```
sqlite> select datetime('now','localtime');
```

参考： [http://blog.csdn.net/shen8686/article/details/6205045](http://blog.csdn.net/shen8686/article/details/6205045)
