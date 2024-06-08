# Optional Assignment: 课程总结

Updated 2117 GMT+8 Dec 29, 2023

2023 fall, Complied by 钟明衡 物理学院



**说明：**

1）12月28日期末机考： AC5 。

2）本次作业可选，不计分。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。





## 1. 期末机考题目



### 27273: 简单的数学题

implementation, math, http://cs101.openjudge.cn/practice/27273



思路：

把和减去2的所有次幂的和的两倍即可

##### 代码

```python
from math import log2
t=int(input())
ans=[0]*t
for _ in range(t):
    n=int(input())
    a=n*(n+1)//2
    b=int(log2(n))
    a-=2*((2<<b)-1)
    ans[_]=a
for a in ans:
    print(a)

```



代码运行截图

![image-20231229202445755](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231229202445755.png)



### 27301: 给植物浇水

Implementation, two pointers, http://cs101.openjudge.cn/practice/27301



思路：

双指针，分别指向a b的位置，然后模拟即可

##### 代码

```python
n,a,b=map(int,input().split())
l=list(map(int,input().split()))
aa,bb=a,b
ans=0
for i in range((n+1)//2):
    if i==n-i-1:
        if max(aa,bb)<l[i]:
            ans+=1
        break
    if aa<l[i]:
        ans+=1
        aa=a
    if bb<l[n-i-1]:
        ans+=1
        bb=b
    aa-=l[i]
    bb-=l[n-i-1]
print(ans)

```



代码运行截图

![image-20231229202658030](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231229202658030.png)



### 27274: 字符串提炼

implementation, http://cs101.openjudge.cn/practice/27274



思路：

按要求提取字符串，然后首一个尾一个地输出即可

##### 代码

```python
from math import log2
s=input()
m=int(log2(len(s)))
ans=''
for i in range(m+1):
    ans+=s[(1<<i)-1]
for i in range(len(ans)//2):
    print(ans[i]+ans[-i-1],end='')
if len(ans)%2==1:
    print(ans[len(ans)//2])
else:
    print('')

```



代码运行截图

![image-20231229202747021](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231229202747021.png)



### 27310: 积木

implementation, brute force, http://cs101.openjudge.cn/practice/27310



思路：

存储每一块积木上面的字母，然后暴力枚举

##### 代码

```python
n=int(input())
l=[[False]*26 for i in range(4)]


def check(s,step,used):
    global l,ans
    if step==len(s):
        ans = True
        return
    for i in range(4):
        if not used[i] and l[i][ord(s[step])-65]:
            used[i]=True
            check(s,step+1,used)
            used[i]=False
            if ans:
                break
    return
          

for i in range(4):
    s=input()
    ss=set()
    for a in s:
        ss.add(a)
    for a in ss:
        l[i][ord(a)-65]=True
for i in range(n):
    news=input()
    ans=False
    check(news,0,[False]*4)
    if ans:
        print('YES')
    else:
        print('NO')

```



代码运行截图

![image-20231229203013686](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231229203013686.png)



### 27237: 体育游戏跳房子

bfs, http://cs101.openjudge.cn/practice/27237



思路：

用bfs，找到到达每个位置最快的方式并存储

为了使字典序最小，先走H再走O

##### 代码

```python
while True:
    n,m=map(int,input().split())
    if m==n==0:
        break
    elif m==n:
        print(0)
        print('')
        continue
    l=[n]
    anss=['']*2500000
    start,end=0,0
    ans=1
    flag=False
    while end!=len(l):
        start,end=end,len(l)
        for i in range(start,end):
            nn=l[i]
            if nn*3<len(anss) and not anss[nn*3]:
                anss[nn*3]=anss[nn]+'H'
                l.append(nn*3)
                if nn*3==m:
                    flag=True
                    break
            if nn//2>0 and not anss[nn//2]:
                anss[nn//2]=anss[nn]+'O'
                l.append(nn//2)
                if nn//2==m:
                    flag=True
                    break
        if flag:break
        ans+=1
    print(ans)
    print(anss[m])

```



代码运行截图

![网页捕获_29-12-2023_203227_cs101.openjudge.cn](D:\Users\Administrator\Pictures\Saved Pictures\网页捕获_29-12-2023_203227_cs101.openjudge.cn.jpeg)



### 27373: 最大整数

dp, greedy, string, sort, http://cs101.openjudge.cn/practice/27373



思路：

背包问题，对整数长度做dp，为了保证数字最大，把“放在前面数字就会更大”的字符串排序到前面（这里用了一个快排）

##### 代码

```python
def bigger(a, b):
    return a+b > b+a


def Sorted(l):
    if len(l) <= 1:
        return l
    mid = l[len(l)//2]
    left, middle, right = [], [], []
    for a in l:
        if a == mid:
            middle.append(a)
        elif bigger(a, mid):
            left.append(a)
        else:
            right.append(a)
    return Sorted(left)+middle+Sorted(right)


m = int(input())
n = int(input())
l = Sorted(input().split())
dp = ['']*(m+1)
for i in range(n):
    ll = len(l[i])
    for j in range(m, ll-1, -1):
        if not dp[j] or int(dp[j-ll]+l[i]) > int(dp[j]):
            dp[j] = dp[j-ll]+l[i]
print(dp[m])

```



代码运行截图

![image-20231229203539734](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231229203539734.png)







## 2. 课程总结

AC5，最后一题写dp时搞错了方向，卡了一个多小时没做出来，小有遗憾。

不知不觉这门课就结束了……我还记得选课还没扩名额的时候，偶然打开选课网，看见12班突然空出了一个名额，于是就选上了这个班。班级群里的讨论氛围真的很好，虽然我一直都是潜水状态，但也学到了很多。

学python给我的感觉就是，刷题真的很有用。之前看了很多python讲解视频，但是一上手刷题，感觉就完全不一样了，尤其是基本语法，去CF上面刷个十几道*800~1000的题，基本就掌握了。之后的许多算法，刷题以后也感觉理解得更深了。

老师推荐的Codeforces这个网站特别好，我个人最喜欢在这上面刷题。相比洛谷，CF上面的题干不会特别奇怪，而且难度分级比洛谷清楚很多，而相比OJ，CF看题解、测试数据都更方便，非常适合练习。此外，全英文也对英语学习有帮助。

CF上面比赛很多，我最近也打了几把，感觉上分机制很好玩，不愧是“电子竞技网站”😋

最后，希望闫老师的班越来越好吧！也希望明年又有这样一批活跃的学生~

[codeforces.com/profile/MinghengZhong](https://codeforces.com/profile/MinghengZhong)

