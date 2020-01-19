## Python数据分析简介

本章的主要内容是python在数据分析方面的介绍。

笔记中只有正常python学习中没有的部分。

### 一、函数式编程

1. 函数式编程：是一种编程范型，将计算机运算视为数学上的函数计算。

2. 函数式编程的函数构成：

   ```python
   lambda(): #行内函数
   	f = lambda x : x + 2 #意为f(x)=x+2
       g = lambda x , y : x + y #意为g(x,y)=x+y
   map(): 
       b = map(lambda x : x+2 ,a)
       b = list(b) #b中每个元素+2
   reduce(): #用于递归 在库 fuctools
       reduce(lambda x,y: x*y , range(1,n+1)) #n的阶乘
   filter(): #过滤器
       b = filter(lambda x :x > 5 and x < 8 , range(10)) #得到6，7
   ```

### 二、python数据分析工具

- Numpy：提供基本的数组功能，且速度是c语言级别的。
- Scipy：提供矩阵支持。安装前请先安装Numpy。
- Matplotlib：著名的绘图库，用来实现数据可视化。
- Pandas：数据分析和探索工具。同样请先安装Numpy。
- StatsModels：统计建模工具。
- Scikit-learn：机器学习库。请先安装numpy，scipy，matplotlib。提供数据集
- keras：人工神经网络库。
- gensim：处理语言方面的任务。



### 库的安装方法：

1. 打开cmd
2. 将目录切换到python的script文件下（切换方法 ： 输入 cd xxxxx）
3. 输入 pip install --user xxxxx（库名） 
4. 回车等待下载