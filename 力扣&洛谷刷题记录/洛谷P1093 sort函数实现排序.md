## 算法：sort排序

### 一、简述

​         我们学过很多种排序。在解决实际问题时，由于要满足时间需求，所以我们要尽量挑选时间复杂度低的排序算法。快速排序往往是最佳的选择。

​         快速排序的实现比较简单，无非是递归＋二分的结合体，即使默写不下来也可以很方便的查到。今天介绍的是如何用头文件自带算法实现排序。

### 二、应用

#### 题目描述

#### 链接：https://www.luogu.com.cn/problem/P1093

#### 洛谷提供

某小学最近得到了一笔赞助，打算拿出其中一部分为学习成绩优秀的前5名学生发奖学金。期末，每个学生都有3门课的成绩:语文、数学、英语。先按总分从高到低排序，如果两个同学总分相同，再按语文成绩从高到低排序，如果两个同学总分和语文成绩都相同，那么规定学号小的同学 排在前面，这样，每个学生的排序是唯一确定的。

任务：先根据输入的3门课的成绩计算总分，然后按上述规则排序，最后按排名顺序输出前五名名学生的学号和总分。注意，在前5名同学中，每个人的奖学金都不相同，因此，你必须严格按上述规则排序。例如，在某个正确答案中，如果前两行的输出数据(每行输出两个数:学号、总分) 是:

77 279279
55 279279

这两行数据的含义是:总分最高的两个同学的学号依次是77号、55号。这两名同学的总分都是 279279 (总分等于输入的语文、数学、英语三科成绩之和) ，但学号为77的学生语文成绩更高一些。如果你的前两名的输出数据是:

55 279279
77 279279

则按输出错误处理，不能得分。



#### 输入格式

共n+1行。

第11行为一个正整数n( \le 300)*n*(≤300)，表示该校参加评选的学生人数。

第22到n+1*n*+1行，每行有33个用空格隔开的数字，每个数字都在00到100100之间。第j*j*行的33个数字依次表示学号为j-1*j*−1的学生的语文、数学、英语的成绩。每个学生的学号按照输入顺序编号为1~n1 *n*（恰好是输入数据的行号减11）。

所给的数据都是正确的，不必检验。

//感谢 黄小U饮品 修正输入格式



#### 输出格式

共5行，每行是两个用空格隔开的正整数，依次表示前55名学生的学号和总分。



#### 输入输出样例

输入

```
6
90 67 80
87 66 91
78 89 91
88 99 77
67 89 64
78 89 98
```

输出 

```
6 265
4 264
3 258
2 244
1 237
```

输入

```
8
80 89 89
88 98 78
90 67 80
87 66 91
78 89 91
88 99 77
67 89 64
78 89 98
```

输出

```
8 265
2 264
6 264
1 258
5 258
```



#### sort函数实现

我们用简单的快速排序或冒泡排序（不一定满足时间复杂度的需求）时，有可能会被**附加的排序条件**困扰，这时我们可以考虑用自带排序算法实现：

- 首先要include头文件：

```c++
#include<bits/stdc++.h> //万能头文件
or
#include<algorithm.h>
```

- 其次，重载一个比较函数

```c++
int cmp(const stu &a,const stu &b){
	if(a.sum!=b.sum) return a.sum>b.sum;//如果总分不一样，如何排
	else if(a.yw!=b.yw) return a.yw>b.yw;//如果总分一样，语文分不同，如何排
	else return a.num<b.num;//如果语文也一样，如何排
}

//这个函数主要是给系统规定排序规则
//附加的排序条件可以在这里进行规定
```

- 最后在主函数中调用sort函数

```c++
sort(s,s+n,cmp);
```



### 三、总结

1. 条件：我们可以用常规的排序算法实现，但由于附加排序条件的存在，常规的排序算法会略有麻烦时。
2. 步骤一：调用头文件
3. 步骤二：重载函数
4. 步骤三：调用sort函数

- 时间复杂度：sort函数基于类似快排的排序方法，时间复杂度为n*log2(n)



### 四、我的题解代码

```c++
#include<bits/stdc++.h>
using namespace std;

struct stu{
	int num;
	int yw;
	int sx;
	int eng;
	int sum;
};

int cmp(const stu &a,const stu &b){
	if(a.sum!=b.sum) return a.sum>b.sum;
	else if(a.yw!=b.yw) return a.yw>b.yw;
	else return a.num<b.num;
}

int main()
{
    int n;
	cin>>n;
	stu s[n];
	for(int i=0;i<n;i++){
		s[i].num=i+1;
		cin>>s[i].yw>>s[i].sx>>s[i].eng;
		s[i].sum=s[i].yw+s[i].sx+s[i].eng;
	} 
    
    sort(s,s+n,cmp);
    
    for(int i=0;i<5;i++){
    	cout<<s[i].num<<" "<<s[i].sum<<endl;
	}
    return 0;
}
```

