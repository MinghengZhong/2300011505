# Assignment #1: 拉齐大家Python水平

Updated 2220 GMT+8 Feb 19, 2024

2024 spring, Complied by 钟明衡 物理学院



**说明：**

1）数算课程的先修课是计概，由于计概学习中可能使用了不同的编程语言，而数算课程要求Python语言，因此第一周作业练习Python编程。如果有同学坚持使用C/C++，也可以，但是建议也要会Python语言。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统：Windows_NT x64 10.0.19045

Python编程环境：Visual Studio Code 1.76.1

C/C++编程环境：Visual Studio Code 1.76.1





## 1. 题目

### 20742: 泰波拿契數

http://cs101.openjudge.cn/practice/20742/



思路：（2min）

数据量很小，直接算就可以

##### 代码

```python
l = [0, 1, 1]
n = int(input())
if n > 2:
    for i in range(n-2):
        l.append(l[-1]+l[-2]+l[-3])
print(l[n])

```



代码运行截图

![image-20240219213504327](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240219213504327.png)



### 58A. Chat room

greedy/strings, 1000, http://codeforces.com/problemset/problem/58/A



思路：（2min）

把hello的每个字符放到列表中，每次检测到就让指针+1，最终指针在最后一位就为YES

##### 代码

```python
s = input()
c = 0
l = ['h', 'e', 'l', 'l', 'o', '012']
for i in range(0, len(s)):
    if s[i] == l[c]:
        c += 1
if c == 5:
    print('YES')
else:
    print('NO')

```



代码运行截图

![image-20240219213752982](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240219213752982.png)



### 118A. String Task

implementation/strings, 1000, http://codeforces.com/problemset/problem/118/A



思路：（2min）

把字母全部小写，然后去掉元音，在每个字母前加个点输出

##### 代码

```python
s = input().lower()
c = ['a', 'e', 'i', 'o', 'u', 'y']
for i in range(0, len(s)):
    if s[i] not in c:
        print('.'+s[i], end='')

```



代码运行截图

![image-20240219214405559](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240219214405559.png)



### 22359: Goldbach Conjecture

http://cs101.openjudge.cn/practice/22359/



思路：（5min）

用质数筛得到质数表，判断a b是否同为质数即可

##### 代码

```python
n = int(input())
is_prime = [True] * (n + 1)
primes = []
for i in range(2, n + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
for a in primes:
    if is_prime[n-a]:
        print('%d %d' % (a, n-a))
        break

```



代码运行截图

![image-20240219215054492](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240219215054492.png)



### 23563: 多项式时间复杂度

http://cs101.openjudge.cn/practice/23563/



思路：（5min）

把字符串按+和^拆开，找到第一个不为0n开头的项，那么后面的数字就是复杂度的指数

##### 代码

```python
s = input().split('+')
ans = 0
for a in s:
    b = a.split('^')
    if b[0] != '0n':
        if int(b[1]) > ans:
            ans = int(b[1])
print('n^%d' % ans)

```



代码运行截图

![image-20240219215216395](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240219215216395.png)



### 24684: 直播计票

http://cs101.openjudge.cn/practice/24684/



思路：（3min）

用defaultdict统计即可

##### 代码

```python
from collections import defaultdict
dic = defaultdict(int)
l = list(map(int, input().split()))
for n in l:
    dic[n] += 1
maxn = max(dic.values())
ans = []
for a in dic.items():
    if a[1] == maxn:
        ans.append(a[0])
ans.sort()
print(' '.join(list(map(str, ans))))

```



代码运行截图

![image-20240219221140237](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240219221140237.png)



## 2. 学习总结和收获

寒假打了几场CF的比赛，上到了蓝名，之后做项目去了，没继续练习算法。有些语法忘记了，开学后要捡回来。



