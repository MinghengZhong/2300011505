# Assignment #D: May月考

Updated 2013 GMT+8 May 8, 2024

2024 spring, Complied by 钟明衡 物理学院



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统：Windows_NT x64 10.0.19045

Python编程环境：Visual Studio Code 1.76.1

C/C++编程环境：Visual Studio Code 1.76.1



## 1. 题目

### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/



思路：

经典的模拟题，直接把树标记即可

代码

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



代码运行截图

![image-20240508194205698](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240508194205698.png)



### 20449: 是否被5整除

http://cs101.openjudge.cn/practice/20449/



思路：

把数一位位用二进制补上并且判断即可

代码

```python
s = input()
count = 0
for a in s:
    count = (count << 1)+int(a)
    if count % 5 == 0:
        print(1, end='')
    else:
        print(0, end='')

```



代码运行截图

![image-20240508194338268](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240508194338268.png)



### 01258: Agri-Net

http://cs101.openjudge.cn/practice/01258/



思路：

最小生成树，把边按照权重从小到大排序，每次用并查集判断一条边是否有必要添加

代码

```python
p = []


def P(x):
    if p[x] != x:
        p[x] = P(p[x])
    return p[x]


while True:
    try:
        n = int(input())
    except EOFError:
        break
    ans = 0
    M = [list(map(int, input().split())) for _ in range(n)]
    p = [i for i in range(n)]
    l = []
    for i in range(n):
        for j in range(n):
            if i != j:
                l.append((i, j, M[i][j]))
    l.sort(key=lambda x: x[2])
    for i, j, k in l:
        pi, pj = P(i), P(j)
        if pi != pj:
            p[pi] = pj
            ans += k
    print(ans)

```



代码运行截图![image-20240508194627713](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240508194627713.png)



### 27635: 判断无向图是否连通有无回路(同23163)

http://cs101.openjudge.cn/practice/27635/



思路：

用广度优先搜索来标记同一个连通区域，如果标记完了一个连通区域，发现还有点未标记，则说明不连通

判断有无回路，我的方法和之前笔试里的不一样，我的方法是计算一个连通域中总边数和总节点数，如果边数不小于节点数，则存在环

代码

```python
m, n = map(int, input().split())
l = []
g = [set() for _ in range(m)]
f = [0]*m
S = []
for _ in range(n):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)
    l.append(a)
S = set()
a, b = 'yes', 'no'
for i in range(m):
    if not f[i]:
        f[i] = 1
        if S:
            a = 'no'
        S = set([i])
        L = [i]
        s, e = 0, 1
        while s != e:
            for j in range(s, e):
                for k in g[L[j]]:
                    if not f[k]:
                        f[k] = 1
                        L.append(k)
                        S.add(k)
            s, e = e, len(L)
        c = sum(j in S for j in l)
        if c >= len(S):
            b = 'yes'
print('connected:%s\nloop:%s' % (a, b))

```



代码运行截图

![image-20240508194747435](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240508194747435.png)





### 27947: 动态中位数

http://cs101.openjudge.cn/practice/27947/



思路：

注意到每次中位数改变时，都是变为了前一个或者后一个，用两个堆正好能实现这个功能

比当前中位数小的，取负数放入small，大的则放入big，它们的堆顶始终是中位数的前一个或者后一个，另外用一个数来记录两边的非平衡，当计数达到2，就把多的那边堆顶的数取出成为新中位数，原来的中位数放入另一个堆，这样就不会超时了

代码

```python
from heapq import heappush, heappop

for _ in range(int(input())):
    l = list(map(int, input().split()))
    small, big, a = [], [], [l[0]]
    r = 0
    mid = l[0]
    c = 1
    for x in l[1:]:
        c += 1
        if x >= mid:
            heappush(big, x)
            r += 1
        else:
            heappush(small, -x)
            r -= 1
        if c % 2:
            if r == 2:
                heappush(small, -mid)
                mid = heappop(big)
                r = 0
            if r == -2:
                heappush(big, mid)
                mid = -heappop(small)
                r = 0
            a.append(mid)
    print(len(a))
    print(' '.join(map(str, a)))

```



代码运行截图

![image-20240508195939936](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240508195939936.png)



### 28190: 奶牛排队

http://cs101.openjudge.cn/practice/28190/



思路：

$N$只有$10^4$，用$O(N^2)$的算法是能过的

用两个指针搜索头尾，同时用s和b分别记录当前队列中最小和最大的值，当右侧加入的值不大于最左侧，左侧指针右移并重新开始搜索，而当最右侧的值是唯一的最大值，就和当前答案取更大者作为新的答案

代码

```python
n = int(input())
l = [int(input()) for _ in range(n)]
s, b = -1, -1
ans = 0
for i in range(n-1):
    s = b = l[i]
    for j in range(i+1, n):
        if l[j] <= s:
            break
        if l[j] > b:
            b = l[j]
            ans = max(ans, j-i+1)
print(ans)

```



代码运行截图

![image-20240508200454032](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240508200454032.png)



## 2. 学习总结和收获

月考挺难的，要不是有几题做过，真做不完

难题感觉全是计概风格，果然还是计概更难



