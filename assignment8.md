# Assignment #8: Nov 月考

Updated 0919 GMT+8 Nov 2, 2023

2023 fall, Complied by 钟明衡 物理学院



**说明：**

1）Nov⽉考： AC6。题⽬都在“练习”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统：Windows_NT x64 10.0.19045

Python编程环境：Visual Studio Code 1.76.1

C/C++编程环境：Visual Studio Code 1.76.1



## 1. 必做题目

### 23563: 多项式时间复杂度

string/implementation/math, http://cs101.openjudge.cn/practice/23563





思路：

输入用加号分开，然后对每一项处理，幂次最大且系数部位不为$0$的即为最终的结果

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

![image-20231102185309094](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231102185309094.png)



### 03143: 验证“歌德巴赫猜想”

math, http://cs101.openjudge.cn/practice/03143



思路：

为了节省时间空间，预先打表得到$2000$以内的所有奇数素数

然后判断$n$与素数的差是否还是素数，直到超过$\frac n2$就退出

##### 代码

```python
n = int(input())
if n < 6 or n % 2 != 0:
    print('Error!')
else:
    l = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999]
    for i in l:
        if i > n/2:
            break
        if n-i in l:
            print('%d=%d+%d' % (n, i, n-i))

```



代码运行截图

![image-20231102185520558](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231102185520558.png)



### 23566: 决战双十一

implementation, http://cs101.openjudge.cn/practice/23566



思路：

分别存储每个店买的总价，最后判断是否能优惠即可

注意总的优惠是每$200$就减$30$

##### 代码

```python
n, m = map(int, input().split())
ans = 0
count = [0]*m
for i in range(n):
    s, p = map(int, input().split())
    count[s-1] += p
    ans += p
ans -= (ans//200)*30
for i in range(m):
    q, x = map(int, input().split('-'))
    if count[i] >= q:
        ans -= x
print(ans)

```



代码运行截图

![image-20231102185803392](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231102185803392.png)



### 03670: 计算鞍点

matrice, http://cs101.openjudge.cn/practice/03670



思路：

把矩阵输入之后，存储每一行最大的位置和每一列最小的位置，如果这一列的最小同时也是所在行最大，则输出结果

如果始终没有结果，说明不存在，按要求输出"not found"

##### 代码

```python
l = []
biggest = []
smallest = []
for i in range(5):
    inp = list(map(int, input().split()))
    biggest.append(inp.index(max(inp)))
    l.append(inp)
for j in range(5):
    small = -1
    for k in range(5):
        if l[k][j] <= small or small == -1:
            small = l[k][j]
            smallk = k
    smallest.append(smallk)
ansx = 0
ansy = 0
for i in range(5):
    if smallest[biggest[i]] == i:
        ansx = i+1
        ansy = biggest[i]+1
if ansx == ansy == 0:
    print('not found')
else:
    print('%d %d %d' % (ansx, ansy, l[ansx-1][ansy-1]))

```



代码运行截图

![image-20231102185959877](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231102185959877.png)



### 19948: 因材施教

greedy, http://cs101.openjudge.cn/practice/19948



思路：

首先把输入按从小到大排序

假定第$k$次分割在第$i_k$和第$i_{k+1}$个元之间，$1<=k<=m-1$，则可以直接写出最终总差异
$$
ans=(a_{i_1}-a_1)+(a_{i_2}-a_{i_1+1})+\dots+(a_{i_{m-1}}-a_{i_{m-2}+1})+(a_n-a_{i_{m-1}+1})
$$
即
$$
ans=(a_n-a_1)-[(a_{i_1+1}-a_{i_1})+(a_{i_2+1}-a_{i_2})+\dots+(a_{i_{m-1}+1}-a_{i_{m-1}})]
$$
也就是说，要让结果尽可能小，策略是让$m-1$个分割处两边的差的总和最大

因此，只需要求出所有相邻两个数差值的值，取其中最大的前$m-1$个，从$a_n-a_1$中减去即可得到答案

##### 代码

```python
n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
d = []
for i in range(n-1):
    d.append(l[i+1]-l[i])
d.sort(reverse=True)
ans = l[-1]-l[0]
for a in d:
    m -= 1
    ans -= a
    if m == 1:
        break
print(ans)

```



代码运行截图

![image-20231102190131827](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231102190131827.png)



### 18182: 打怪兽

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/



思路：

在字典中存每个$t$，相应存储所有的$x$，然后按照$t$从小到大排序

之后按顺序计算伤害，如果$t$时技能数太多，就排序取最大的前$m$个计算，当$b$被打完就退出

如果到最后$b$还没被打完，就输出"alive"

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

![image-20231102190941945](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231102190941945.png)



## 2. 学习总结和收获

这次月考总体不难，只是有些细节需要注意，比如决战双十一，每$200$元就减$30$，似乎很多人理解为是最多只减一次

复习了一下字典按照keys排序的方法，以及字典的item可以是list，但是key不能





