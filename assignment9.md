# Assignment #9: 密集期中考试周

Updated 2130 GMT+8 Nov 6, 2023

2023 fall, Complied by 钟明衡 物理学院



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统：Windows_NT x64 10.0.19045

Python编程环境：Visual Studio Code 1.76.1

C/C++编程环境：Visual Studio Code 1.76.1





## 1. 必做题目

### OJ19943：图的拉普拉斯矩阵

matrix, http://cs101.openjudge.cn/practice/19943/



思路：

先创建一个$n\times n$的全为$0$的矩阵$M$

输入一组$(x,y)$，则将$M[x][y]$、$M[y][x]$改为$-1$，同时将$M[x][x]$和$M[y][y]$加$1$

最后把$M$输出即可

##### 代码

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

![image-20231106214545056](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231106214545056.png)



### OJ19942：⼆维矩阵上的卷积运算v0.2

matrix, http://cs101.openjudge.cn/practice/19942/



思路：



##### 代码

```python
m, n, p, q = map(int, input().split())
M = []
K = []
for i in range(m):
    M.append(list(map(int, input().split())))
for i in range(p):
    K.append(list(map(int, input().split())))
for i in range(m-p+1):
    for j in range(n-q+1):
        ans = 0
        for y in range(p):
            for x in range(q):
                ans += M[i+y][j+x]*K[y][x]
        print(ans, end='')
        if j != n-q+1:
            print(' ', end='')
    print('')

```



代码运行截图

![image-20231106215653947](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231106215653947.png)



### CF313B: Ilya and Queries

dp/implementation, 1100, https://codeforces.com/contest/313/problem/B



思路：

如果直接存每个位置是不是满足要求，最后去数，会超时

因此，把从最前面到每个位置为止的数量记录在列表中，之后直接调用第$l$、$r$个之差，就是结果

##### 代码

```python
s = input()+'a'
L = [0]*(len(s))
for i in range(len(s)-1):
    L[i+1] += L[i]
    if s[i] == s[i+1]:
        L[i+1] += 1
n = int(input())
for i in range(n):
    l, r = map(int, input().split())
    print(L[r-1]-L[l-1])

```



代码运行截图

![image-20231106222244478](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231106222244478.png)



### CF706B: Interesting drink

binary search/dp/implementation, 1100, https://codeforces.com/problemset/problem/706/B



思路：

将价格从小到大排序，然后使用二分查找

##### 代码

```python
def search(n, i, j):
    global l
    if j-i <= 1:
        return i
    else:
        k = (i+j)//2
        if l[k] <= n:
            return search(n, k, j)
        else:
            return search(n, i, k)


n = int(input())
l = sorted([0]+list(map(int, input().split())))
q = int(input())
for i in range(q):
    m = int(input())
    if m >= l[-1]:
        print(n)
    elif m < l[1]:
        print(0)
    else:
        print(search(m, 0, n))

```



代码运行截图

![image-20231106224056848](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231106224056848.png)



## 2. 选做题目

如果耗时太⻓，直接看解题思路，或者源码

### CF466C: Number of Ways

binary search/brute force/data structures/dp/two pointers, 1700

https://codeforces.com/problemset/problem/466/C



思路：

首先，如果总和不是三的倍数，直接输出$0$

否则，从左右两边分别寻找可以让和为总和$\frac13$的位置，输出所有左位置对应的可取右位置个数之和，可取的条件是右比左至少大$2$

查找右位置时采用二分法，防止超时

##### 代码

```python
def search(n, i, j):
    global right
    if j-i == 1:
        return j
    k = (i+j)//2
    if right[k] <= n+1:
        return search(n, k, j)
    else:
        return search(n, i, k)


n = int(input())
l = list(map(int, input().split()))
suml = sum(l)
if suml % 3 != 0:
    print(0)
else:
    suml = suml//3
    count = 0
    left = []
    right = []
    for i in range(n):
        count += l[i]
        if count == suml:
            left.append(i)
        if count == 2*suml and i != n-1:
            right.append(i+1)
    ans = 0
    last = 0
    for a in left:
        if a >= right[-1]-1:
            break
        elif a <= right[last]-2:
            ans += len(right)-last
        else:
            last = search(a, last, len(right)-1)
            ans += len(right)-last
    print(ans)

```



代码运行截图

![image-20231106235138123](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231106235138123.png)



### CF1443C: The Delivery Dilemma

binary search/greedy/sortings, 1400,

https://codeforces.com/problemset/problem/1443/C
提示： 1）结果要⼀起输出，不要分次print，会超时。2）⽤zip函数。



思路：

对于每组数据，结果为$max(送餐时间最大值,取餐时间总和)$，只要求出这个的最小值即可

用zip可以把list绑定后排序，放在前面的优先排序

本题中，先比较送餐时间最短值和取餐时间总和，如果后者更小则直接为答案

否则，从最大的送餐时间开始，将其替换成自己取餐，这样总时间是只会减小的，一旦出现取餐总时间超过送餐最大时间且导致总时间增大，则上一个时间就是最小值

注意不能分次输出，要存到一个表里最后输出，要不然会超时

##### 代码

```python
t = int(input())
output = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum(b) <= min(a):
        output.append(sum(b))
    else:
        a, b = zip(*sorted(zip(a, b), reverse=True))
        ans = a[0]
        count = 0
        for i in range(n-1):
            count += b[i]
            new_ans = max(count, a[i+1])
            if new_ans < ans:
                ans = new_ans
            elif new_ans > ans:
                break
        output.append(ans)
for i in range(t):
    print(output[i])

```



代码运行截图

![image-20231107115000112](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231107115000112.png)



## 3. 学习总结和收获

第一次学会了用zip（之前一直是用字典来实现相同的操作的）。用zip排序会考虑每个组的排序，优先考虑放在前面的组，如果相同则按照后面的组排序。另外，注意到列表、元组都可以用zip，但zip*后的结果是元组。

另外，分次print会比存储以后单次print要慢，无特殊情况应该采用后者。

