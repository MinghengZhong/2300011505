# Assignment #4: 国庆节月考

### 钟明衡2300011505

### 2023/9/26

**说明：**

1）国庆节⽉考：AC8。摸底题⽬都在“练习”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统：Windows_NT x64 10.0.19045

Python编程环境：Visual Studio Code 1.76.1

C/C++编程环境：Visual Studio Code 1.76.1

## 1. 必做题目

#### 02701: 与7无关的数

math, http://cs101.openjudge.cn/practice/02701

一个正整数,如果它能被7整除,或者它的十进制表示法中某一位上的数字为7,则称其为与7相关的数.现求所有小于等于n(n < 100)的与7无关的正整数的平方和.

**输入**

输入为一行,正整数n(n < 100)

**输出**

输出一行，包含一个整数，即小于等于n的所有与7无关的正整数的平方和。

样例输入

```
21
```

样例输出

```
2336
```

来源

计算概论05





【钟明衡，物理学院，2023年秋】

思路：

由于n上限仅为100，可以直接列出和7有关的数，然后累加时跳过这些数即可

##### 代码

```python
n = int(input())
l = [7, 14, 17, 21, 27, 28, 35, 37, 42, 47, 49, 56, 57, 63,
     67, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 84, 87, 91, 97, 98]
ans = 0
for i in range(1, n+1):
    if i not in l:
        ans += i**2
print(ans)

```



代码运行截图

![image-20231005213910196](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231005213910196.png)



#### 02712: 细菌繁殖 

math, http://cs101.openjudge.cn/practice/02712

一种细菌的繁殖速度是每天成倍增长。例如：第一天有10个，第二天就变成20个，第三天变成40个，第四天变成80个，……。现在给出第一天的日期和细菌数目，要你写程序求出到某一天的时候，细菌的数目。

**输入**

第一行有一个整数n，表示测试数据的数目。其后n行每行有5个整数，整数之间用一个空格隔开。第一个数表示第一天的月份，第二个数表示第一天的日期，第三个数表示第一天细菌的数目，第四个数表示要求的那一天的月份，第五个数表示要求的那一天的日期。已知第一天和要求的一天在同一年并且该年不是闰年，要求的一天一定在第一天之后。数据保证要求的一天的细菌数目在长整数（long）范围内。

**输出**

对于每一组测试数据，输出一行，该行包含一个整数，为要求的一天的细菌数。

样例输入

```
2
1 1 1 1 2
2 28 10 3 2
```

样例输出

```
2
40
```

来源

2005~2006医学部计算概论期末考试





【钟明衡，物理学院，2023年秋】

思路：

直接计算目标日期之间相差的天数，然后将初始细菌数乘以2的这个天数次幂即可

##### 代码

```python
n = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(n):
    m1, d1, ans, m2, d2 = map(int, input().split())
    count = d2-d1
    for j in range(m1-1, m2-1):
        count += days[j]
    print(ans*(2**count))

```



代码运行截图

![image-20231005214613229](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231005214613229.png)



#### 02753: 菲波那契数列

math, http://cs101.openjudge.cn/practice/02753

菲波那契数列是指这样的数列: 数列的第一个和第二个数都为1，接下来每个数都等于前面2个数之和。
给出一个正整数a，要求菲波那契数列中第a个数是多少。
**输入**
第1行是测试数据的组数n，后面跟着n行输入。每组测试数据占1行，包括一个正整数a(1 <= a <= 20)
**输出**
输出有n行，每行输出对应一个输入。输出应是一个正整数，为菲波那契数列中第a个数的大小
样例输入

```
4
5
2
19
1
```

样例输出

```
5
1
4181
1
```





【钟明衡，物理学院，2023年秋】

思路：

直接将斐波那契数列的前20项存到列表中，然后输出即可

##### 代码

```python
n = int(input())
l = [1, 1]
for i in range(18):
    l.append(l[-1]+l[-2])
for i in range(n):
    print(l[int(input())-1])

```



代码运行截图

![image-20231005215009699](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231005215009699.png)



#### 02810: 完美立方

bruteforce, http://cs101.openjudge.cn/practice/02810

形如$a^3= b^3 + c^3 + d^3$的等式被称为完美立方等式。例如$12^3= 6^3 + 8^3 + 10^3$ 。编写一个程序，对任给的正整数N (N ≤ 100)，寻找所有的四元组 (a, b, c, d)，使得 $a^3 = b^3 + c^3 + d^3$，其中 a,b,c,d 大于 1, 小于等于N，且 b ≤ c ≤ d。

**输入**

一个正整数N (N≤100)。

**输出**

每行输出一个完美立方。输出格式为：
Cube = a, Triple = (b,c,d)
其中a,b,c,d所在位置分别用实际求出四元组值代入。

请按照a的值，从小到大依次输出。当两个完美立方等式中a的值相同，则b值小的优先输出、仍相同则c值小的优先输出、再相同则d值小的先输出。

样例输入

```
24
```

样例输出

```
Cube = 6, Triple = (3,4,5)
Cube = 12, Triple = (6,8,10)
Cube = 18, Triple = (2,12,16)
Cube = 18, Triple = (9,12,15)
Cube = 19, Triple = (3,10,18)
Cube = 20, Triple = (7,14,17)
Cube = 24, Triple = (12,16,20)
```





【钟明衡，物理学院，2023年秋】

思路：

数据量不大，直接枚举即可

利用b<=c<=d可以略微优化

##### 代码

```python
n = int(input())
for a in range(2, n+1):
    for b in range(2, a):
        for c in range(b, a):
            for d in range(c, a):
                if a**3 == b**3+c**3+d**3:
                    print('Cube = %d, Triple = (%d,%d,%d)' % (a, b, c, d))

```



代码运行截图

![image-20231005220540580](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231005220540580.png)



#### 04138: 质数的和与积

math, http://cs101.openjudge.cn/practice/04138

两个质数的和是S，它们的积最大是多少？

**输入**

一个不大于10000的正整数S，为两个质数的和。

**输出**

一个整数，为两个质数的最大乘积。数据保证有解。

样例输入

```
50
```

样例输出

```
589
```

来源

《奥数典型题举一反三（小学五年级）》 (ISBN 978-7-5445-2882-5) 第三章 第二讲 例1





【钟明衡，物理学院，2023年秋】

思路：

先写一个函数来判断是否为质数

然后从n/2到2来判断是否是两个质数的和，从数学上可知，第一个判断出的结果就是最大的

##### 代码

```python
def check(n):
    if n == 2 or n == 3 or n == 5:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True


n = int(input())
for i in range(int(n/2)+1, 1, -1):
    if check(i):
        if check(n-i):
            print(i*(n-i))
            break

```



代码运行截图

![image-20231005223201259](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231005223201259.png)



#### 04146: 数字方格

math, http://cs101.openjudge.cn/practice/04146

![img](https://raw.githubusercontent.com/GMyhf/img/main/img/2747_1.jpg)
如上图，有3个方格，每个方格里面都有一个整数a1，a2，a3。已知0 <= a1, a2, a3 <= n，而且a1 + a2是2的倍数，a2 + a3是3的倍数， a1 + a2 + a3是5的倍数。你的任务是找到一组a1，a2，a3，使得a1 + a2 + a3最大。

输入

一行，包含一个整数n (0 <= n <= 100)。

输出

一个整数，即a1 + a2 + a3的最大值。

样例输入

```
3
```

样例输出

```
5
```





【钟明衡，物理学院，2023年秋】

思路：

直接枚举即可

##### 代码

```python
n = int(input())
ans = 0
for a1 in range(n, -1, -1):
    for a2 in range(n, -1, -1):
        for a3 in range(n, -1, -1):
            if a1+a2+a3 > ans:
                if (a1+a2) % 2 == 0 and (a2+a3) % 3 == 0 and (a1+a2+a3) % 5 == 0:
                    ans = a1+a2+a3
print(ans)

```



代码运行截图

![image-20231005224634275](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231005224634275.png)



## 2. 选做题目

#### 02746: 约瑟夫问题

implementation, http://cs101.openjudge.cn/practice/02746

约瑟夫问题：有ｎ只猴子，按顺时针方向围成一圈选大王（编号从１到ｎ），从第１号开始报数，一直数到ｍ，数到ｍ的猴子退出圈外，剩下的猴子再接着从1开始报数。就这样，直到圈内只剩下一只猴子时，这个猴子就是猴王，编程求输入ｎ，ｍ后，输出最后猴王的编号。

**输入**

每行是用空格分开的两个整数，第一个是 n, 第二个是 m ( 0 < m,n <=300)。最后一行是：

0 0

**输出**

对于每行输入数据（最后一行除外)，输出数据也是一行，即最后猴王的编号

样例输入

```
6 2
12 4
8 3
0 0
```

样例输出

```
5
1
7
```





【钟明衡，物理学院，2023年秋】

思路：

直接模拟就可以了，利用取整来实现闭环的效果

注意使用pop以减少时间复杂度

##### 代码

```python
while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    elif m == 1:
        print(n)
        continue
    l = []
    for i in range(n):
        l.append(i+1)
    i = m-1
    while n > 1:
        if i > n-1:
            i = i % n
        n -= 1
        l.pop(i)
        i += m-1
    print(l[0])

```



代码运行截图

![image-20231005235435628](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231005235435628.png)



#### CF1364A: A. XXXXX

brute force/data structures/number theory/two pointers, 1200, https://codeforces.com/problemset/problem/1364/A

Ehab loves number theory, but for some reason he hates the number 𝑥. Given an array 𝑎, find the length of its longest subarray such that the sum of its elements **isn't** divisible by 𝑥, or determine that such subarray doesn't exist.

An array 𝑎 is a subarray of an array 𝑏 if 𝑎 can be obtained from 𝑏 by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

**Input**

The first line contains an integer 𝑡 (1≤𝑡≤5) — the number of test cases you need to solve. The description of the test cases follows.

The first line of each test case contains 2 integers 𝑛 and 𝑥 (1≤𝑛≤10^5^, 1≤𝑥≤10^4^) — the number of elements in the array 𝑎 and the number that Ehab hates.

The second line contains 𝑛 space-separated integers $𝑎_1, 𝑎_2, ……, 𝑎_𝑛 (0≤𝑎_𝑖≤10^4)$ — the elements of the array 𝑎.

**Output**

For each testcase, print the length of the longest subarray whose sum isn't divisible by 𝑥. If there's no such subarray, print −1.

Example

input

```
3
3 3
1 2 3
3 4
1 2 3
2 2
0 6
```

output

```
2
3
-1
```

Note

In the first test case, the subarray \[2,3\] has sum of elements 5, which isn't divisible by 3.

In the second test case, the sum of elements of the whole array is 6, which isn't divisible by 4.

In the third test case, all subarrays have an even sum, so the answer is −1.



【钟明衡，物理学院，2023年秋】

思路：

重要的的是子序列之和与x的整除，因此将所有余数加起来，讨论以下情况：

如果所有数都能整除x，则不存在，输出-1

如果所有数之和不能整除x，则答案就是n

如果能整除，但是不是每个数都能整除，就找出最靠前或者最靠后的一个不能整除x的数，这个数所在离两头最近的次序要从答案的n中减去

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

![image-20231006001557251](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231006001557251.png)



## 3. 学习总结和收获

数据量较少的时候，可以完全使用计算机思维，把所有情况都尝试一遍

但是如果数据较多，这样很可能会超时，因此需要优化算法，比如剪枝，或者采用数学方法

如果使用的算法不对从而TLE，就算从Python改成Pypy或者C++，也会超时，只有改变算法才有可能AC



