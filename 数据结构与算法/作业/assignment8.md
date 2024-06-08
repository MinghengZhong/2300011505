# Assignment #8: 图论：概念、遍历，及 树算

Updated 1925 GMT+8 Apr 8, 2024

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

### 19943: 图的拉普拉斯矩阵

matrices, http://cs101.openjudge.cn/practice/19943/



思路：

输入$(i,j)$，则给$L_{ii}$和$L_{jj}$加上$1$，给$L_{ij}$和$L_{ji}$减去$1$

代码

```python
n, m = map(int, input().split())
M = [[0]*n for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    M[y][x] = -1
    M[x][y] = -1
    M[x][x] += 1
    M[y][y] += 1
for i in range(n):
    for j in range(n):
        print(M[i][j], end='')
        if j != n-1:
            print(' ', end='')
    print('')
    
```



代码运行截图

![image-20240408141202510](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240408141202510.png)



### 18160: 最大连通域面积

matrix/dfs similar, http://cs101.openjudge.cn/practice/18160



思路：

找到W且未被标记的位置，然后利用dfs来寻找周围所有联通的W并计数，查找过的上标记防止重复，所有搜索中值最大的就是答案

代码

```python
def dfs(i, j):
    global l, used
    count = 1
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if l[x][y] == 'W' and not used[x][y]:
                used[x][y] = True
                count += dfs(x, y)
    return count


t = int(input())
anss = []
for _ in range(t):
    n, m = map(int, input().split())
    used = [[False]*(m+2) for i in range(n+2)]
    l = ['.'*(m+2)]
    ans = 0
    for i in range(n):
        l.append('.'+input()+'.')
    l.append('.'*(m+2))
    for i in range(1, n+1):
        for j in range(1, m+1):
            if l[i][j] == 'W' and not used[i][j]:
                used[i][j] = True
                ans = max(ans, dfs(i, j))
    anss.append(ans)
for ans in anss:
    print(ans)
    
```



代码运行截图

![image-20240408141600029](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240408141600029.png)



### sy383: 最大权值连通块

https://sunnywhy.com/sfbj/10/3/383



思路：

并查集，把同一个连通图里面的所有指针都指向同一个节点

注意，和冰可乐那题不同，这本身是一个无向图，可能存在环，单纯连接会死循环。解决办法是，限制指针只能由大的数指向小的数，这样绝对不会出现死循环

代码

```python
from collections import defaultdict as D
p = D(lambda: -1)


def F(x):
    global p
    if p[x]+1:
        px = F(p[x])
        p[x] = px
        return px
    return x


n, m = map(int, input().split())
l = list(map(int, input().split()))
for _ in range(m):
    x, y = map(int, input().split())
    px, py = F(x), F(y)
    if px != py:
        p[max(px, py)] = min(px, py)
ans = [0]*n
for i in range(n):
    ans[F(i)] += l[i]
print(max(ans))

```



代码运行截图

![image-20240408150056058](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240408150056058.png)



### 03441: 4 Values whose Sum is 0

data structure/binary search, http://cs101.openjudge.cn/practice/03441



思路：

把A和B所有可能的和算出来，然后再用C和D去求和为0的数量

注意不能用defaultdict，会超内存，用普通字典就不会

代码

```python
n = int(input())
L = [tuple(map(int, input().split())) for _ in range(n)]
D = {}
for a, _, _, _ in L:
    for _, b, _, _ in L:
        D[-a-b] = D.get(-a-b, 0)+1
ans = 0
for _, _, c, _ in L:
    for _, _, _, d in L:
        ans += D.get(c+d, 0)
print(ans)

```



代码运行截图

![image-20240408184420005](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240408184420005.png)



### 04089: 电话号码

trie, http://cs101.openjudge.cn/practice/04089/



思路：

将所有电话号码的字符串直接排序，之后利用字符串比大小的特性可以发现，如果出现了前缀的情况，则必定发生在两个相邻电话号码之间，且前一个不比后一个长，如此判断即可

代码

```python
for _ in range(int(input())):
    n = int(input())
    l = sorted([input() for i in range(n)])
    ans = True
    for i in range(1, n):
        if len(l[i]) >= len(l[i-1]):
            if l[i][:len(l[i-1])] == l[i-1]:
                ans = False
        if not ans:
            break
    print('YES' if ans else 'NO')

```



代码运行截图

![image-20240408160703806](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240408160703806.png)



### 04082: 树的镜面映射

http://cs101.openjudge.cn/practice/04082/



思路：

只要能反向构造出原来的树即可。按照“左儿子右兄弟”的原则，用一个指标$h$来代表深度，由于是满二叉树，当出现内部节点则下一个必定为其子节点，$h+1$，出现外部节点则必定为叶节点，$h-1$

每次将字符加到$h$层，注意要反过来，新字符放到最前面，最后按顺序每层输出即可

代码

```python
from collections import defaultdict as D
n = int(input())
d = D(str)
h = 0
ans = ''
for s in input().split():
    if s[0] != '$':
        d[h] = s[0]+d[h]
    if s[1] == '0':
        h += 1
    else:
        h -= 1
for a in d.values():
    ans += a
print(' '.join(ans)) 

```



代码运行截图

![image-20240408161313505](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240408161313505.png)



## 2. 学习总结和收获

01703发现它，抓住它、18250冰阔落、sy383最大权值连通块这三题对于理解并查集很有帮助

我对于并查集的理解，通俗来讲就是“找爸爸”（更严谨的说法是找root）。最基本的想法，每个节点都通过一个指针指向和它在同一个集合中的元素，通过正确构造指针（一般是新来的指向原来的），可以让每个集合最终由一个节点代表，从同一个集合的其他节点沿着指针走，走到头都是这个节点，这个节点就是root，这样的话处理许多问题都会很简化

找root用递归，这样返回时可以更新路上所有的指针，直接让它们全部指向root，后续查询就会更快，基本代码如下：

```python
def F(x):
    if p[x]:  # 如果当前节点不是root（如果爸爸存在）
        p[x] = F(p[x])  # 找到root同时将指针指向root（让小孩随爸爸姓）
        return px
    return x  # 当前节点是root（找到老祖宗了）
```

之所以叫“找爸爸”，是因为这件事和现实中小孩随爸爸姓很像，如果把集合和姓氏对应起来，将连接关系视为父子关系，我们只要$O(1)$的复杂度（看姓氏）就知道这个元属于哪个集合（这个小孩的祖上是谁）

在此基础上，我们可以做很多扩展，比如01703发现它、抓住它这题需要考虑到距离问题

此外还要排除一下死循环问题。毕竟指针带了个方向的意味，在有环图中就容易绕圈圈死循环，找不到root（转了一圈发现自己是自己老祖宗）。18250冰阔落并不会有这个问题，因为“倒可乐”本身是有方向的，也不会形成环。而sy383最大权值连通块就容易出现这个问题，这个题本身是个无向图，如果统一让y指向x，样例数据就会死循环，我的解决办法是统一让大的编号指向小的编号。构造方法视具体情况而定。

还有一个发现，defaultdict虽然省事但是比dict更占内存，03441 4 Values whose Sum is 0这题我就因为一直用defaultdict导致MLE，改回dict就过了。dict用get可以避免KeyError



