# Assignment #5: 排序和超时

### 钟明衡2300011505

### 2023/10/10

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统：Windows_NT x64 10.0.19045

Python编程环境：Visual Studio Code 1.76.1

C/C++编程环境：Visual Studio Code 1.76.1

## 1. 必做题目

#### 69A. Young Physicist

implementation/math, 1000, https://codeforces.com/problemset/problem/69/A

A guy named Vasya attends the final grade of a high school. One day Vasya decided to watch a match of his favorite hockey team. And, as the boy loves hockey very much, even more than physics, he forgot to do the homework. Specifically, he forgot to complete his physics tasks. Next day the teacher got very angry at Vasya and decided to teach him a lesson. He gave the lazy student a seemingly easy task: You are given an idle body in space and the forces that affect it. The body can be considered as a material point with coordinates (0; 0; 0). Vasya had only to answer whether it is in equilibrium. "Piece of cake" — thought Vasya, we need only to check if the sum of all vectors is equal to 0. So, Vasya began to solve the problem. But later it turned out that there can be lots and lots of these forces, and Vasya can not cope without your help. Help him. Write a program that determines whether a body is idle or is moving by the given vectors of forces.

**Input**

The first line contains a positive integer *n* (1 ≤ *n* ≤ 100), then follow *n* lines containing three integers each: the *x~i~* coordinate, the *y~i~* coordinate and the *z~i~* coordinate of the force vector, applied to the body ( - 100 ≤ *x~i~*, *y~i~*, *z~i~* ≤ 100).

**Output**

Print the word "YES" if the body is in equilibrium, or the word "NO" if it is not.

Examples

input

```
3
4 1 7
-2 4 -1
1 -5 -3
```

output

```
NO
```

input

```
3
3 -1 7
-5 2 -4
2 -1 -3
```

output

```
YES
```





【钟明衡，物理学院，2023年秋】

思路：

直接把输入给累加起来，检查结果是否为0即可

##### 代码

```python
n = int(input())
x = 0
y = 0
z = 0
for i in range(0, n):
    s = input().split()
    x += int(s[0])
    y += int(s[1])
    z += int(s[2])
if x == 0 and y == 0 and z == 0:
    print('YES')
else:
    print('NO')

```



代码运行截图

![image-20231010145615838](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231010145615838.png)



#### 96A. Football

implementation/strings, 900, http://codeforces.com/problemset/problem/96/A

Petya loves football very much. One day, as he was watching a football match, he was writing the players' current positions on a piece of paper. To simplify the situation he depicted it as a string consisting of zeroes and ones. A zero corresponds to players of one team; a one corresponds to players of another team. If there are at least 7 players of some team standing one after another, then the situation is considered dangerous. For example, the situation 00100110111111101 is dangerous and 11110111011101 is not. You are given the current situation. Determine whether it is dangerous or not.

**Input**

**The first input lin**e contains a non-empty string consisting of characters "0" and "1", which represents players. The length of the string does not exceed 100 characters. There's at least one player from each team present on the field.

**Output**

Print "YES" if the situation is dangerous. Otherwise, print "NO".

Examples

input

```
001001
```

output

```
NO
```

input

```
1000000001
```

output

```
YES
```





【钟明衡，物理学院，2023年秋】

思路：

从index为1的开始检查，如果和上一个相同n就加一，否则n回到1，n达到7就直接跳出循环

##### 代码

```python
s = input()
n = 1
b = False
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        n += 1
    else:
        n = 1
    if n == 7:
        b = True
        break
if b:
    print('YES')
else:
    print('NO')

```



代码运行截图

![image-20231010145921125](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231010145921125.png)



#### 270A. Fancy Fence

geometry/implementation/math, 1100, x23265, https://codeforces.com/problemset/problem/270/A

Emuskald needs a fence around his farm, but he is too lazy to build it himself. So he purchased a fence-building robot.

He wants the fence to be a regular polygon. The robot builds the fence along a single path, but it can only make fence corners at a single angle *a*.

Will the robot be able to build the fence Emuskald wants? In other words, is there a regular polygon which angles are equal to *a*?

**Input**

The first line of input contains an integer *t* (0 < *t* < 180) — the number of tests. Each of the following *t* lines contains a single integer *a* (0 < *a* < 180) — the angle the robot can make corners at measured in degrees.

**Output**

For each test, output on a single line "YES" (without quotes), if the robot can build a fence Emuskald wants, and "NO" (without quotes), if it is impossible.

Examples

input

```
3
30
60
90
```

output

```
NO
YES
YES
```

Note

In the first test case, it is impossible to build the fence, since there is no regular polygon with angle ![img](https://espresso.codeforces.com/df5f4b07dd5316fde165b43657b2696e2919e791.png).

In the second test case, the fence is a regular triangle, and in the last test case — a square.





【钟明衡，物理学院，2023年秋】

思路：

正多边形的外角和为360度，因此只需要判断360能否整除（180 - 输入角度）即可

##### 代码

```python
n = int(input())
for i in range(n):
    a = int(input())
    if 360 % (180-a) == 0:
        print('YES')
    else:
        print('NO')

```



代码运行截图

![image-20231010161715729](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231010161715729.png)



#### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A


Imagine that you have a twin brother or sister. Having another person that looks exactly like you seems very unusual. It's hard to say if having something of an alter ego is good or bad. And if you do have a twin, then you very well know what it's like.

Now let's imagine a typical morning in your family. You haven't woken up yet, and Mom is already going to work. She has been so hasty that she has nearly forgotten to leave the two of her darling children some money to buy lunches in the school cafeteria. She fished in the purse and found some number of coins, or to be exact, *n* coins of arbitrary values $a_1, a_2, ..., a_n$. But as Mom was running out of time, she didn't split the coins for you two. So she scribbled a note asking you to split the money equally.

As you woke up, you found Mom's coins and read her note. "But why split the money equally?" — you thought. After all, your twin is sleeping and he won't know anything. So you decided to act like that: pick for yourself some subset of coins so that the sum of values of your coins is **strictly larger** than the sum of values of the remaining coins that your twin will have. However, you correctly thought that if you take too many coins, the twin will suspect the deception. So, you've decided to stick to the following strategy to avoid suspicions: you take the **minimum number of coins**, whose sum of values is strictly more than the sum of values of the remaining coins. On this basis, determine what **minimum** number of coins you need to take to divide them in the described manner.

**Input**

The first line contains integer *n* (1 ≤ *n* ≤ 100) — the number of coins. The second line contains a sequence of *n* integers $a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100) $ — the coins' values. All numbers are separated with spaces.

**Output**

In the single line print the single number — the minimum needed number of coins.

Examples

input

```
2
3 3
```

output

```
2
```

input

```
3
2 1 2
```

output

```
2
```

Note

In the first sample you will have to take 2 coins (you and your twin have sums equal to 6, 0 correspondingly). If you take 1 coin, you get sums 3, 3. If you take 0 coins, you get sums 0, 6. Those variants do not satisfy you as your sum should be strictly more that your twins' sum.

In the second sample one coin isn't enough for us, too. You can pick coins with values 1, 2 or 2, 2. In any case, the minimum number of coins equals 2.



【钟明衡，物理学院，2023年秋】

思路：

为了取尽可能少的硬币，将所有硬币面值按从大到小排序之后取，如果总和严格大于一半就停手

##### 代码

```python
n = int(input())
a = list(map(int, input().split()))
count = 0
sum = 0
for i in range(0, n):
    sum += a[i]
sum = int(sum/2)+1
a.sort(reverse=True)
for i in range(0, n):
    count += a[i]
    if count >= sum:
        print(i+1)
        break

```



代码运行截图

![image-20231010150442741](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231010150442741.png)



## 2. 选做题目

#### 12559: 最大最小整数 v0.3

greedy/strings/sortings, http://cs101.openjudge.cn/practice/12559



假设有n个正整数，将它们连成一片，将会组成一个新的大整数。现需要求出，能组成的最大最小整数。

比如，有4个正整数，23，9，182，79，连成的最大整数是97923182，最小的整数是18223799。

**输入**

第一行包含一个整数n，1<=n<=1000。
第二行包含n个正整数，相邻正整数间以空格隔开。

**输出**

输出为一行，为这n个正整数能组成的最大的多位整数和最小的多位整数，中间用空格隔开。

样例输入

```
Sample1 in:
4
23 9 182 79

Sample1 out:
97923182 18223799
```

样例输出

```
Sample2 in:
2
11 113

Sample2 out:
11311 11113
```





【钟明衡，物理学院，2023年秋】

思路：

不能直接使用sort，因为string排序出来的顺序并不一定使结果最大（小）

依然采用快速排序，但是要手写一个，然后自己写一个比较大小的逻辑：s1和s2比较，谁放在前面拼出来的数大，谁就“更大”

排序以后倒序、顺序输出即可

##### 代码

```python
def compare(s1, s2):
    if int(s1+s2) > int(s2+s1):
        return 1
    elif int(s1+s2) < int(s2+s1):
        return -1
    else:
        return 0


def quicksort(l):
    if len(l) <= 1:
        return l
    ll = l[int(len(l)/2)]
    left = [x for x in l if compare(x, ll) == -1]
    middle = [x for x in l if compare(x, ll) == 0]
    right = [x for x in l if compare(x, ll) == 1]
    return quicksort(left) + middle + quicksort(right)


n = int(input())
l = quicksort(input().split())
for i in range(n-1, -1, -1):
    print(l[i], end='')
print(' ', end='')
for i in range(n):
    print(l[i], end='')
print('')

```



代码运行截图

![image-20231010155958827](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231010155958827.png)



#### 230B. T-primes

binary search/implementation/math/number theory, 1300, http://codeforces.com/problemset/problem/230/B

We know that prime numbers are positive integers that have exactly two distinct positive divisors. Similarly, we'll call a positive integer *t* Т-prime, if *t* has exactly three distinct positive divisors.

You are given an array of *n* positive integers. For each of them determine whether it is Т-prime or not.

**Input**

The first line contains a single positive integer, *n* (1 ≤ *n* ≤ 10^5^), showing how many numbers are in the array. The next line contains *n* space-separated integers *x~i~* (1 ≤ *x~i~* ≤ 10^12^).

Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is advised to use the cin, cout streams or the %I64d specifier.

**Output**

Print *n* lines: the *i*-th line should contain "YES" (without the quotes), if number *x~i~* is Т-prime, and "NO" (without the quotes), if it isn't.

Examples

input

```
3
4 5 6
```

output

```
YES
NO
NO
```

Note

The given test has three numbers. The first number 4 has exactly three divisors — 1, 2 and 4, thus the answer for this number is "YES". The second number 5 has two divisors (1 and 5), and the third number 6 has four divisors (1, 2, 3, 6), hence the answer for them is "NO".





【钟明衡，物理学院，2023年秋】

思路：

题目本身不难，就是判断一个数是不是质数的平方

但是本身是很容易超时的，关键在于怎么优化

我的方案是把可能用到的所有质数先存起来，然后直接在里面找

存质数的时候，先存一个2，然后从3开始以2为步长找，判断方法是在已经找到的质数中逐个取余，以平方根截止，如果是质数就存进来

找的时候不能用in来搜，因为数据量也很大，会超时，我用了一个全是False的列表，将其中质数的位置改成True，这样最后找的时候就不会超时

##### 代码

```python
n = int(input())
l = list(map(int, input().split()))
a = [2]
c = [False]*(int(max(l)**.5)+1)
c[1] = True
for i in range(3, len(c), 2):
    b = True
    for j in a:
        if i % j == 0:
            b = False
            break
        if j**2 > i:
            break
    if b:
        a.append(i)
        c[i-1] = True
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

![image-20231010184841875](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231010184841875.png)



## 3. 学习总结和收获

很多时候，优化的难度远远高于写出程序本身，要通过缩减for循环的范围、增大步长、优化算法降复杂度的方式来避免TLE

最后一题T-Primes仍可以优化，使用欧拉筛来找质数，代码如下：

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

![image-20231011131357902](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231011131357902.png)
