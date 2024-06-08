# Assignment #1: 摸底考试

### 钟明衡2300011505

### 2023/9/19

## 1. 编程环境

操作系统：Windows_NT x64 10.0.19045

Python编程环境：Visual Studio Code 1.76.1

C/C++编程环境：Visual Studio 2022 Enterprise



## 2. 必做题目

#### OJ02750：鸡兔同笼

math, http://cs101.openjudge.cn/practice/02750

一个笼子里面关了鸡和兔子（鸡有2只脚，兔子有4只脚，没有例外）。已经知道了笼子里面脚的总数a，问笼子里面至少有多少只动物，至多有多少只动物。

**输入**

一行，一个正整数a (a < 32768)。

**输出**

一行，包含两个正整数，第一个是最少的动物数，第二个是最多的动物数，两个正整数用一个空格分开。
如果没有满足要求的答案，则输出两个0，中间用一个空格分开。

样例输入

```
20
```

样例输出

```
5 10
```



【钟明衡，物理学院，2023年秋】

思路：

n为4的倍数，则最少情况为全是兔子，最多情况为全是鸡

n为2的倍数但不是4的倍数，则最少情况为一只鸡剩下全是兔子，最多情况为全是鸡

n不为偶数，则不可能

##### Python3 代码

```python
n = int(input())
if n % 4 == 0:
    print(str(int(n/4))+' '+str(int(n/2)))
elif n % 2 == 0:
    print(str(int(n/4)+1)+' '+str(int(n/2)))
else:
    print('0 0')

```



Python代码运行截图

![image-20230919151532361](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230919151532361.png)



#### OJ02733：判断闰年

math, http://cs101.openjudge.cn/practice/02733

判断某年是否是闰年。

**输入**

输入只有一行，包含一个整数a(0 < a < 3000)

**输出**

一行，如果公元a年是闰年输出Y，否则输出N

样例输入

```
2006
```

样例输出

```
N
```

提示

公历纪年法中，能被4整除的大多是闰年，但能被100整除而不能被400整除的年份不是闰年， 能被3200整除的也不是闰年，如1900年是平年，2000年是闰年，3200年不是闰年。



【钟明衡，物理学院，2023年秋】

思路：

能被100整除，则判断是否能被400整除

不能被100整除，则判断是否能被4整除

##### Python3 代码

```python
n = int(input())
if n % 100 == 0:
    if n % 400 == 0:
        print('Y')
    else:
        print('N')
elif n % 4 == 0:
    print('Y')
else:
    print('N')

```



Python代码运行截图

![image-20230919151740101](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230919151740101.png)



#### OJ01218:THE DRUNK JAILER

http://cs101.openjudge.cn/practice/01218/

A certain prison contains a long hall of n cells, each right next to each other. Each cell has a prisoner in it, and each cell is locked.
One night, the jailer gets bored and decides to play a game. For round 1 of the game, he takes a drink of whiskey,and then runs down the hall unlocking each cell. For round 2, he takes a drink of whiskey, and then runs down the
hall locking every other cell (cells 2, 4, 6, ?). For round 3, he takes a drink of whiskey, and then runs down the hall. He visits every third cell (cells 3, 6, 9, ?). If the cell is locked, he unlocks it; if it is unlocked, he locks it. He
repeats this for n rounds, takes a final drink, and passes out.
Some number of prisoners, possibly zero, realizes that their cells are unlocked and the jailer is incapacitated. They immediately escape.
Given the number of cells, determine how many prisoners escape jail.

**输入**

The first line of input contains a single positive integer. This is the number of lines that follow. Each of the following lines contains a single integer between 5 and 100, inclusive, which is the number of cells n.

**输出**

For each line, you must print out the number of prisoners that escape when the prison has n cells.

样例输入

```
2
5
100
```

样例输出

```
2
10
```

来源

Greater New York 2002



【钟明衡，物理学院，2023年秋】

思路：

只有平方数具有奇数个因数，因此结果就是不超过n的平方数的平方根

##### Python3 代码

```python
N = int(input())
for i in range(0, N):
    print(int(int(input())**(1/2)))

```



Python代码运行截图 

![image-20230919154632875](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230919154632875.png)



#### OJ02689: 大小写字母互换

http://cs101.openjudge.cn/practice/02689

把一个字符串中所有出现的大写字母都替换成小写字母，同时把小写字母替换成大写字母。

**输入**

输入一行：待互换的字符串。

**输出**

输出一行：完成互换的字符串（字符串长度小于80）。

样例输入

```
If so, you already have a Google Account. You can sign in on the right. 
```

样例输出

```
iF SO, YOU ALREADY HAVE A gOOGLE aCCOUNT. yOU CAN SIGN IN ON THE RIGHT. 
```

来源

计算概论05



【钟明衡，物理学院，2023年秋】

思路：

如果字符的值在'a'到'z'之间，就输出大写

如果字符的值在'A'到'Z'之间，就输出小写

否则原样输出

##### Python3 代码

```python
s = input()
for i in range(0, len(s)):
    if 'a' <= s[i] <= 'z':
        print(s[i].upper(), end='')
    elif 'A' <= s[i] <= 'Z':
        print(s[i].lower(), end='')
    else:
        print(s[i], end='')

```



Python代码运行截图

![image-20230919155022127](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230919155022127.png)





#### OJ02808: 校⻔外的树

implementation, http://cs101.openjudge.cn/practice/02808

某校大门外长度为L的马路上有一排树，每两棵相邻的树之间的间隔都是1米。我们可以把马路看成一个数轴，马路的一端在数轴0的位置，另一端在L的位置；数轴上的每个整数点，即0，1，2，……，L，都种有一棵树。
马路上有一些区域要用来建地铁，这些区域用它们在数轴上的起始点和终止点表示。已知任一区域的起始点和终止点的坐标都是整数，区域之间可能有重合的部分。现在要把这些区域中的树（包括区域端点处的两棵树）移走。你的任务是计算将这些树都移走后，马路上还有多少棵树。

**输入**

输入的第一行有两个整数L（1 <= L <= 10000）和 M（1 <= M <= 100），L代表马路的长度，M代表区域的数目，L和M之间用一个空格隔开。接下来的M行每行包含两个不同的整数，用一个空格隔开，表示一个区域的起始点和终止点的坐标。

**输出**

输出包括一行，这一行只包含一个整数，表示马路上剩余的树的数目。

样例输入

```
500 3
150 300
100 200
470 471
```

样例输出

```
298
```

来源：noip2005普及组



【钟明衡，物理学院，2023年秋】

思路：

直接用list模拟树，True表示有树

移走树时，如果遇到True则改为False，同时答案加一，否则不操作

##### Python3 代码

```python
ans, n = map(int, input().split())
ans += 1
trees = []
for i in range(0, ans+1):
    trees.append(True)
for i in range(0, n):
    start, stop = map(int, input().split())
    for j in range(start, stop+1):
        if trees[j]:
            trees[j] = False
            ans -= 1
print(ans)

```



Python代码运行截图

![image-20230919155641439](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230919155641439.png)



## 3. 选做题目

### OJ25353: 排队

Greedy, http://cs101.openjudge.cn/practice/25353/

有 N 名同学从左到右排成一排，第 i 名同学的身高为 hi。现在张老师想改变排队的顺序，他能进行任意多次（包括0次）如下操作：

\- 如果两名同学相邻，并且他们的身高之差不超过 D，那么老师就能交换他俩的顺序。

请你帮张老师算一算，通过以上操作，字典序最小的所有同学（从左到右）身高序列是什么？

输入

第一行包含两个正整数 $N, D (1≤N≤10^5, 1≤D≤10^9)$。
接下去 N 行，每行一个正整数 hi (1<=hi<=109) 表示从左到右每名同学的身高。

输出

输出 N 行，第 i 行表示答案中第 i 名同学的身高。

样例输入

```
5 3
7
7
3
6
2
```

样例输出

```
6
7
7
2
3
```

提示

【样例解释】
一种交换位置的过程如下：
`7 7 3 6 2-> 7 7 6 3 2-> 7 7 6 2 3-> 7 6 7 2 3-> 6 7 7 2 3`

【数据范围和约定】
对于 10% 的数据，满足 N≤100；
对于另外 20% 的数据，满足 N≤5000；
对于全部数据，满足 $1≤N≤10_5, 1≤D≤10^9, 1≤h_i≤10^9$。



【钟明衡，物理学院，2023年秋】

思路：

输入身高后，如果是第一个同学，就放入列表

之后的同学，从后往前依次对比身高，如果身高差过大就立刻结束循环，如果在循环过程中检测到比输入更高的身高，就用该位置覆盖计数器，以此获得最小的字典序

复杂度应该是$O(N^2)$，TLE了，改用Pypy和C++都还是TLE，想不到更快的解决办法了😭

##### Python3 代码

```python
N, D = map(int, input().split())
l = []
l.append(int(input()))
for i in range(N-1):
    n = int(input())
    index = -1
    for j in range(i, -1, -1):
        if abs(l[j]-n) > D:
            break
        else:
            if l[j] > n:
                index = j
    if index != -1:
        l.insert(index, n)
    else:
        l.append(n)
for ans in l:
    print(ans)

```



Python代码运行截图

![image-20230925224512986](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230925224512986.png)



##### C++ 代码

```c++
#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
int main()
{
	int N, D, input, index;
	scanf("%d %d", &N, &D);
	scanf("%d", &input);
	vector<int> ans = { input };
	for (int i = 1; i < N; i++)
	{
		scanf("%d", &input);
		index = -1;
		for (int j = i - 1; j >= 0; j--)
		{
			if (ans[j] - input > D || input - ans[j] > D)
			{
				break;
			}
			else if (ans[j] > input)
			{
				index = j;
			}
		}
		if (index == -1)
		{
			ans.push_back(input);
		}
		else
		{
			ans.insert(ans.begin() + index, input);
		}
	}
	for (int i = 0; i < N; i++)
	{
		printf("%d\n", ans[i]);
	}
	return 0;
}

```



C++ 代码运行截图

![image-20230925224416880](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230925224416880.png)



## 4. 学习总结和收获

由于我很早以前学过一些编程，摸底考试AC5对我来说并不难，最后一题很遗憾地TLE了，当时没想出优化算法。

狱警那道题，当时第一反应是写了个模拟，后来想想可以直接用数学解决：只有因数为奇数个的房间能逃脱，而只有平方数满足这一点。因此，答案应该是不超过房间总数的最大平方数的平方根。
