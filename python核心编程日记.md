##input()与raw_input()区别
```
14.3.5 input()
内建函数input()是eval()和raw_input()的组合，等价于eval(raw_input())。类似于
raw_input()，input()有一个可选的参数，该参数代表了给用户的字符串提示。如果不给定参数的
话，该字符串默认为空串。
从功能上看,input 不同于raw_input()，因为raw_input()总是以字符串的形式，逐字地返回用
户的输入。input()履行相同的的任务；而且，它还把输入作为python 表达式进行求值。这意味着
input()返回的数据是对输入表达式求值的结果：一个python 对象。
```

##xrange()与range()
```
8.6.5 xrange() 内建函数
xrange() 类似 range() , 不过当你有一个很大的范围列表时, xrange() 可能更为适合, 因为
它不会在内存里创建列表的完整拷贝. 它只被用在 for 循环中, 在 for 循环外使用它没有意义。
同样地, 你可以想到, 它的性能远高出 range(), 因为它不生成整个列表。
```
