# Assignment #9: 图论：遍历，及 树算

Updated 1739 GMT+8 Apr 14, 2024

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

### 04081: 树的转换

http://cs101.openjudge.cn/dsapre/04081/



思路：

用一个指标h来指示当前处于原树的第几层，而利用列表H[h]，记录当前处于转换后的树的第几层，当h增加就接上H[h-1]+1，h减少直接退回，不用额外对H操作

代码

```python
S = input()
h = a = b = 0
H = [0]*len(S)
for s in S:
    if s == 'd':
        h += 1
        H[h] = H[h-1]+1
        a = max(a, h)
        b = max(b, H[h])
    else:
        h -= 1
        H[h] += 1
print('%d => %d' % (a, b))

```



代码运行截图

![image-20240414185746309](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240414185746309.png)



### 08581: 扩展二叉树

http://cs101.openjudge.cn/dsapre/08581/



思路：

记录当前节点的高度，初始为2，当该位上是字母就高度加1，否则减1，当高度为1时，说明前序的左子树已经遍历完了，把前序的“中左右”换成中序的“左中右”或后序的“左右中”再拼起来，就是要输出的结果

代码

```python
def F(s, k):
    if len(s) == 1:
        return ''
    i, c = 1, 2
    while c-1:
        c -= 2*int(s[i] == '.')-1
        i += 1
    l = F(s[1:i], k)
    r = F(s[i:], k)
    if k:
        return l+r+s[0]
    else:
        return l+s[0]+r


s = input()
print(F(s, 0))
print(F(s, 1))

```



代码运行截图

![image-20240414192415583](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240414192415583.png)



### 22067: 快速堆猪

http://cs101.openjudge.cn/practice/22067/



思路：

用辅助栈，每次push时，在辅助栈中加入当前最轻的猪的体重，pop时也同步pop，这样栈顶始终是当前猪堆中最轻的体重，查询时直接输出即可

代码

```python
l, S = [], []
while True:
    try:
        s = input()
    except EOFError:
        break
    if s == 'min':
        if S:
            print(l[-1])
    elif s == 'pop':
        if S:
            S.pop()
            l.pop()
    else:
        n = int(s.split()[1])
        S.append(n)
        if l:
            n = min(l[-1], n)
        l.append(n)

```



代码运行截图

![image-20240414192924359](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240414192924359.png)



### 04123: 马走日

dfs, http://cs101.openjudge.cn/practice/04123



思路：

用dfs暴力搜索，能走的就试试，最后输出成功遍历的次数即可

代码

```python
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]


def dfs(n, m, x, y, gone):
    if len(gone) == n*m:
        return 1
    a = 0
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        idx = nx+ny*n
        if 0 <= nx < n and 0 <= ny < m and idx not in gone:
            gone.add(idx)
            a += dfs(n, m, nx, ny, gone)
            gone.remove(idx)
    return a


for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    print(dfs(n, m, x, y, set([x+y*n])))

```



代码运行截图

![image-20240414194805349](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240414194805349.png)



### 28046: 词梯

bfs, http://cs101.openjudge.cn/practice/28046/



思路：

没有任何优化就会超时，一开始以为是bfs导致的超时，改了各种方法，甚至自己手搓了一个双端bfs，还是超时

后来意识到是建立连接的时候，两两都对比太慢了，于是使用桶的思想，把三个位置字母都相同的放到同一个桶里，最后再内部建立连接

代码

```python
from collections import defaultdict as D
n = int(input())
l = [input() for _ in range(n)]
b, g, p = D(set), D(set), {}
for s in l:
    b['_'+s[1:]].add(s)
    b[s[0]+'_'+s[2:]].add(s)
    b[s[:2]+'_'+s[3]].add(s)
    b[s[:3]+'_'].add(s)
for a in b.values():
    for x in a:
        for y in a:
            if x != y:
                g[x].add(y)
a, b = input().split()
if a == b:
    print(a)
    exit()
l = [a]
gone = set([a])
s, e = 0, 1
while s != e:
    for i in range(s, e):
        for a in g[l[i]]:
            if a not in gone:
                p[a] = l[i]
                gone.add(a)
                l.append(a)
            if a == b:
                ans = [b]
                while True:
                    b = p[b]
                    ans.append(b)
                    if b == l[0]:
                        break
                print(*ans[::-1])
                exit()
    s, e = e, len(l)
print('NO')

```



代码运行截图![image-20240414233354497](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240414233354497.png)



### 28050: 骑士周游

dfs, http://cs101.openjudge.cn/practice/28050/



思路：

一开始用传统的dfs，卡了很久，甚至尝试了打表，都没成功（不优化实在太慢了）

查了一下，有一步优化是优先走下一步能走的格子少的格子，虽然没想明白为什么，但是加上之后速度发生了质的变化😱

代码

```python
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]
n = int(input())
x, y = map(int, input().split())
g = [set() for _ in range(n*n)]
for i in range(n*n):
    for k in range(8):
        if 0 <= i//n+dx[k] < n and 0 <= i % n + dy[k] < n:
            g[i].add(i+dx[k]*n+dy[k])

gone = [False]*(n*n)


def dfs(x, gone, k):
    if not k:
        print('success')
        exit()
    l = []
    for a in g[x]:
        if not gone[a]:
            c = 0
            for b in g[a]:
                if not gone[b]:
                    c += 1
            l.append((a, c))
    l.sort(key=lambda x: x[1])
    for a, _ in l:
        gone[a] = True
        dfs(a, gone, k-1)
        gone[a] = False


gone[x*n+y] = True
dfs(x*n+y, gone, n*n-1)
print('fail')

```



代码运行截图

![image-20240414231903632](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240414231903632.png)

![image-20240414231918689](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240414231918689.png)



## 2. 学习总结和收获

被最后两题的优化卡了很久，可见我已经写惯了最常规的算法，优化思想已经生疏了，还需要多练习



