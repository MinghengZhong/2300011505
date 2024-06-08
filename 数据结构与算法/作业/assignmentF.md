# Assignment #F: All-Killed 满分

Updated 2217 GMT+8 May 21, 2024

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

### 22485: 升空的焰火，从侧面看

http://cs101.openjudge.cn/practice/22485/



思路：

构建好树后，按照任意顺序遍历树都可以，只要保证右子树比左子树后遍历到即可，为了方便我就用了dfs

记录当前的层数，每次搜索到一个节点，就更新当前层上的结果，这样就可以保证每层越右边的越后搜索到，从而满足要求

代码

```python
l, r = {}, {}
ans = []
for i in range(int(input())):
    l[i+1], r[i+1] = map(int, input().split())


def dfs(x, h):
    global ans
    if h == len(ans):
        ans.append(x)
    else:
        ans[h] = x
    if l[x]+1:
        dfs(l[x], h+1)
    if r[x]+1:
        dfs(r[x], h+1)


dfs(1, 0)
print(*ans)

```



代码运行截图

![image-20240521125710416](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240521125710416.png)



### 28203:【模板】单调栈

http://cs101.openjudge.cn/practice/28203/



思路：

用一个辅助栈，存储还未找到比它更大的数的那些元素，以及这些元素的索引

当每次有新的数进来，就从栈顶比较，弹出所有比当前数更小的元素，并且在它们原来的索引处存储当前新数的索引

辅助栈初始化为全0，这样没找到的数自动就是0了

代码

```python
n = int(input())
s = []
ans = [0]*n
for i, a in enumerate(map(int, input().split())):
    while s and s[-1][0] < a:
        ans[s.pop()[1]] = i+1
    s.append((a, i))
print(*ans)

```



代码运行截图

![image-20240521131458387](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240521131458387.png)



### 09202: 舰队、海域出击！

http://cs101.openjudge.cn/practice/09202/



思路：

有向图判断有无环，即判断是否存在这样的点，能够走回自己

进行dfs，同时存储当前能够到达这个点的所有点（开始新的dfs后，不需要更新，因为我们只关心是不是有环），当下一个点已经走过，但是这个点出现在存储之中，说明这个点能走回自己，就判定为有环

代码

```python
def dfs(x, d):
    global g, next, f
    for a in next[x]:
        if g[a]:
            g[a] = 0
            dfs(a, d | {a})
        else:
            if a in d:
                f = 1
        if f:
            return


def ans():
    global g, next, f
    f = 0
    n, m = map(int, input().split())
    g = [1]*n
    next = {i: set() for i in range(n)}
    for i in range(m):
        a, b = map(int, input().split())
        next[a-1].add(b-1)
    for i in range(n):
        if g[i]:
            g[i] = 0
            dfs(i, {i})
            if f:
                return 'Yes'
    return 'No'


for _ in range(int(input())):
    print(ans())

```



代码运行截图

![image-20240521134907966](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240521134907966.png)



### 04135: 月度开销

http://cs101.openjudge.cn/practice/04135/



思路：

划分方法是否合法，是可以通过大小判断出来的，因此这个问题可以用二分法解决，搜索到满足要求的最小的月度开销即为答案

代码

```python
def check(l, m, k):
    count = 0
    for a in l:
        if count+a > k:
            m -= 1
            count = 0
        count += a
    return m >= 1


n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(int(input()))
left, right = max(l)-1, sum(l)
while right-left > 1:
    middle = (left+right)//2
    if check(l, m, middle):
        right = middle
    else:
        left = middle
print(right)

```



代码运行截图

![image-20240521180452342](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240521180452342.png)



### 07735: 道路

http://cs101.openjudge.cn/practice/07735/



思路：

要用到一种特殊的Dijkstra，因为有可能出现路更长，但是花费更小的可行情况

不能走的条件是走了重复路线，一个很简单的判别方法是记录当前已经走过的道路数量，当超过N-1则一定走了重复的路

一开始我用路程或者花费变小来剪枝，这样会错，会漏掉情况，而上述剪枝方法由于和Dijkstra连用，不需要担心路径变长的问题

代码

```python
from heapq import heappop, heappush
K = int(input())
N = int(input())
g = [[] for _ in range(N)]
for _ in range(int(input())):
    S, D, L, T = map(int, input().split())
    g[S-1].append((D-1, L, T))
q = []
heappush(q, (0, 0, 0, 0))
while q:
    x, y, n, a = heappop(q)
    if a == N-1:
        print(x)
        exit()
    for b, l, t in g[a]:
        if n+1 < N and y+t <= K:
            heappush(q, (x+l, y+t, n+1, b))
print(-1)

```



代码运行截图

![image-20240521191454427](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240521191454427.png)



### 01182: 食物链

http://cs101.openjudge.cn/practice/01182/



思路：

并查集，但要注意每个元素存三次，分别表示这个元素作为A/B/C时的情况

当输入x和y是同类，先判断，如果是真的，则将三种情况都归为同类

当输入x吃y，先判断，如果是真的，则同时有y吃x的天敌，x的天敌吃x

代码

```python
def F(x):
    global p
    if p[x] != x:
        p[x] = F(p[x])
    return p[x]


def U(x, y):
    global p
    x = F(x)
    y = F(y)
    p[x] = y


n, k = map(int, input().split())
p = [i for i in range(3*n+1)]
ans = 0
for _ in range(k):
    d, x, y = map(int, input().split())
    if x > n or y > n:
        ans += 1
        continue
    if d == 1:
        if F(x+n) == F(y) or F(x+2*n) == F(y):
            ans += 1
            continue
        U(x, y)
        U(x+n, y+n)
        U(x+2*n, y+2*n)
    else:
        if F(x) == F(y) or F(x+2*n) == F(y):
            ans += 1
            continue
        U(x, y+2*n)
        U(x+n, y)
        U(x+2*n, y+n)
print(ans)

```



代码运行截图

![image-20240521215002483](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240521215002483.png)



## 2. 学习总结和收获

这次的作业覆盖面很广，有树、栈、图、二分查找、Dijkstra和并查集，有几题都不简单，是很好的复习

不知不觉，数算已经快学完了，也断断续续刷了挺多题，明显感觉到代码能力提升

笔试还有一些知识盲区，要好好补补了





