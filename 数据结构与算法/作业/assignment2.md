# Assignment #2: 编程练习

Updated 1700 GMT+8 Feb 24, 2024

2024 spring, Complied by 钟明衡 物理学院



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:
- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统：Windows_NT x64 10.0.19045

Python编程环境：Visual Studio Code 1.76.1

C/C++编程环境：Visual Studio Code 1.76.1



## 1. 题目

### 27653: Fraction类

http://cs101.openjudge.cn/2024sp_routine/27653/



思路：（~5min）

创建一个fraction类，利用math.gcd来通分，并且把可能的负号移到分子上

str格式为“分子/分母”

##### 代码

```python
from math import gcd


class fraction:
    def __init__(self, a, b):
        g = gcd(a, b)
        if a*b >= 0:
            self.top = abs(a)//g
            self.bottom = abs(b)//g
        else:
            self.top = -abs(a)//g
            self.bottom = abs(b)//g

    def __str__(self):
        return '%d/%d' % (self.top, self.bottom)

    def __add__(self, other):
        e = self.top*other.bottom+self.bottom*other.top
        f = self.bottom*other.bottom
        return fraction(e, f)


a, b, c, d = map(int, input().split())
print(fraction(a, b)+fraction(c, d))

```



代码运行截图

![image-20240224160530499](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240224160530499.png)



### 04110: 圣诞老人的礼物-Santa Clau’s Gifts

greedy/dp, http://cs101.openjudge.cn/practice/04110



思路：（~5min）

按照单位重量的价值从大到小排序，然后按顺序装满背包即可

##### 代码

```python
n, W = map(int, input().split())
ans, v, w = 0, [], []
for i in range(n):
    a, b = map(int, input().split())
    v.append(a)
    w.append(b)
l = sorted([i for i in range(n)], key=lambda x: -v[x]/w[x])
for i in l:
    if W >= w[i]:
        W -= w[i]
        ans += v[i]
    else:
        ans += v[i]*W/w[i]
        break
print('%.1f' % (ans))

```



代码运行截图

![image-20240224161531626](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240224161531626.png)



### 18182: 打怪兽

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/



思路：（~5min）

将每时刻的伤害分别从大到小排序，取每时刻前m个加起来，

##### 代码

```python
N = int(input())
for _ in range(N):
    n, m, b = map(int, input().split())
    damage = {}
    for i in range(n):
        t, x = map(int, input().split())
        if t not in damage.keys():
            damage[t] = [x]
        else:
            damage[t].append(x)
    damage = dict(sorted(damage.items()))
    for i in damage.keys():
        if len(damage[i]) <= m:
            b -= sum(damage[i])
        else:
            dmg = sorted(damage[i], reverse=True)
            b -= sum(dmg[0:m])
        if b <= 0:
            print(i)
            break
    if b > 0:
        print('alive')

```



代码运行截图

![image-20240224162316209](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240224162316209.png)



### 230B. T-primes

binary search/implementation/math/number theory, 1300, http://codeforces.com/problemset/problem/230/B



思路：（<5min）

判断这个数的平方根是不是质数即可

##### 代码

```python
n = int(input())
l = list(map(int, input().split()))
N = int(max(l)**.5)+1
c = [True]*N
for i in range(3, N, 2):
    c[i] = False
c[0] = False
for i in range(3, N+1, 2):
    if c[i-1]:
        j = i
        while j*i <= N:
            c[j*i-1] = False
            j += 2
for i in range(0, n):
    if int(l[i]**.5) != l[i]**.5:
        print('NO')
    else:
        if c[int(l[i]**.5)-1]:
            print('YES')
        else:
            print('NO')

```



代码运行截图

![image-20240224164339037](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240224164339037.png)



### 1364A. XXXXX

brute force/data structures/number theory/two pointers, 1200, https://codeforces.com/problemset/problem/1364/A



思路：（~5min）

如果每个元素都可以整除，则输出-1

否则，找到最靠前或者最靠后的不能整除的那个元素，即可得到最长子串

##### 代码

```python
t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    count = 0
    ans = False
    for a in l:
        if a % x != 0:
            ans = True
        count += a % x
    if ans:
        if count % x == 0:
            for j in range(1, n):
                if l[j-1] % x != 0 or l[n-j] % x != 0:
                    n -= j
                    break
        print(n)
    else:
        print('-1')

```



代码运行截图

![image-20240224164903527](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240224164903527.png)



### 18176: 2050年成绩计算

http://cs101.openjudge.cn/practice/18176/



思路：（~5min）

直接按照题目要求计算即可。使用欧拉筛来防止超时

##### 代码

```python
m, n = map(int, input().split())
is_prime = [True] * (10000 + 1)
primes = []
for i in range(2, 10000):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, 10000, i):
            is_prime[j] = False
for _ in range(m):
    l = tuple(map(int, input().split()))
    count = 0
    for a in l:
        if int(a**.5) == a**.5:
            if is_prime[int(a**.5)]:
                count += a
    print('%.2f' % (count/len(l)))

```



代码运行截图

![image-20240224170003511](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240224170003511.png)



## 2. 学习总结和收获

大部分题目上学期都做过。按现在的水平，一题大概不到5分钟。

学习了如何定义类。其实做那道题完全不需要如此定义，但是需要增强可读性或者多次调用的时候，是很必要的。



