## 快速排序

[快速排序](https://zh.wikipedia.org/wiki/快速排序)

快速排序（英语：Quicksort），又称划分交换排序（partition-exchange sort）

快速排序算法其实很简单，采用分治策略。步骤如下：

选取一个基准元素（pivot）
比pivot小的放到pivot左边，比pivot大的放到pivot右边
对pivot左边的序列和右边的序列分别递归的执行步骤1和步骤2

平均时间复杂度 O(n log n)
每次都选取的是最大或者最小, 是最坏情况, 最坏的情况, O(n^2), 但通过随机算法可以避免最坏情况
