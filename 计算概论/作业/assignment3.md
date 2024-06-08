# Assignment #3: 语法练习

### 钟明衡2300011505

### 2023/9/26

**说明：**

1）第2周课上讲到了计算机相关的历史，介绍了ASCII表。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）同学完成作业的时候，就是这个模版文件中修改补充好。为便于助教批改作业，请尽量不要删除其他文字。

5）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统：Windows_NT x64 10.0.19045

Python编程环境：Visual Studio Code 1.76.1

C/C++编程环境：Visual Studio 2022 Enterprise



## 1. 必做题目

#### 118A. String Task

implementation/strings, 1000, http://codeforces.com/problemset/problem/118/A

Petya started to attend programming lessons. On the first lesson his task was to write a simple program. The program was supposed to do the following: in the given string, consisting if uppercase and lowercase Latin letters, it:

- deletes all the vowels,
- inserts a character "." before each consonant,
- replaces all uppercase consonants with corresponding lowercase ones.

Vowels are letters "A", "O", "Y", "E", "U", "I", and the rest are consonants. The program's input is exactly one string, it should return the output as a single string, resulting after the program's processing the initial string.

Help Petya cope with this easy task.

**Input**

The first line represents input string of Petya's program. This string only consists of uppercase and lowercase Latin letters and its length is from 1 to 100, inclusive.

**Output**

Print the resulting string. It is guaranteed that this string is not empty.

Examples

input

```
tour
```

output

```
.t.r
```

input

```
Codeforces
```

output

```
.c.d.f.r.c.s
```

input

```
aBAcAba
```

output

```
.b.c.b
```





【钟明衡，物理学院，2023年秋】

思路：

首先把输入全部换成小写

然后逐个字符比较，如果不是元音，就输出一个点加上这个字符

##### 代码

```python
s = input().lower()
c = ['a', 'e', 'i', 'o', 'u', 'y']
for i in range(0, len(s)):
    if s[i] not in c:
        print('.'+s[i], end='')

```



代码运行截图

![image-20230926121350215](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230926121350215.png)



#### 263A. Beautiful Matrix

implementation, 800, http://codeforces.com/problemset/problem/263/A

You've got a 5 × 5 matrix, consisting of 24 zeroes and a single number one. Let's index the matrix rows by numbers from 1 to 5 from top to bottom, let's index the matrix columns by numbers from 1 to 5 from left to right. In one move, you are allowed to apply one of the two following transformations to the matrix:

1. Swap two neighboring matrix rows, that is, rows with indexes *i* and *i* + 1 for some integer *i* (1 ≤ *i* < 5).
2. Swap two neighboring matrix columns, that is, columns with indexes *j* and *j* + 1 for some integer *j* (1 ≤ *j* < 5).

You think that a matrix looks *beautiful*, if the single number one of the matrix is located in its middle (in the cell that is on the intersection of the third row and the third column). Count the minimum number of moves needed to make the matrix beautiful.

**Input**

The input consists of five lines, each line contains five integers: the *j*-th integer in the *i*-th line of the input represents the element of the matrix that is located on the intersection of the *i*-th row and the *j*-th column. It is guaranteed that the matrix consists of 24 zeroes and a single number one.

**Output**

Print a single integer — the minimum number of moves needed to make the matrix beautiful.

Examples

input

```
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
```

output

```
3
```

input

```
0 0 0 0 0
0 0 0 0 0
0 1 0 0 0
0 0 0 0 0
0 0 0 0 0
```

output

```
1
```



【钟明衡，物理学院，2023年秋】

思路：

直接输出'1'与中心点横纵坐标之差绝对值的和即可

##### 代码

```python
for i in range(0, 5):
    l = input().split()
    for j in range(0, 5):
        if l[j] == '1':
            ans = abs((i-2))+abs((j-2))
print(ans)

```



代码运行截图

![image-20230926121842167](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230926121842167.png)



#### 281A. Word Capitalization

implementation/strings, 800, http://codeforces.com/problemset/problem/281/A

Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

Note, that during capitalization all the letters except the first one remains unchanged.

**Input**

A single line contains a non-empty word. This word consists of lowercase and uppercase English letters. The length of the word will not exceed 10^3^.

**Output**

Output the given word after capitalization.

Examples

input

```
ApPLe
```

output

```
ApPLe
```

input

```
konjac
```

output

```
Konjac
```





【钟明衡，物理学院，2023年秋】

思路：

如果只有一个字母，就输出它的大写

否则输出首字母大写+后面的所有字母

##### 代码

```python
s = input()
if s[0] <= 'z':
    if len(s) == 1:
        print(s[0].upper())
    else:
        print(s[0].upper()+s[1:])
else:
    print(s)

```



代码运行截图 

![image-20230926122130159](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230926122130159.png)



#### 282A. Bit++

implementation, 800, http://codeforces.com/problemset/problem/282/A

The classic programming language of Bitland is Bit++. This language is so peculiar and complicated.

The language is that peculiar as it has exactly one variable, called *x*. Also, there are two operations:

- Operation ++ increases the value of variable *x* by 1.
- Operation -- decreases the value of variable *x* by 1.

A statement in language Bit++ is a sequence, consisting of exactly one operation and one variable *x*. The statement is written without spaces, that is, it can only contain characters "+", "-", "X". Executing a statement means applying the operation it contains.

A programme in Bit++ is a sequence of statements, each of them needs to be executed. Executing a programme means executing all the statements it contains.

You're given a programme in language Bit++. The initial value of *x* is 0. Execute the programme and find its final value (the value of the variable when this programme is executed).

**Input**

The first line contains a single integer *n* (1 ≤ *n* ≤ 150) — the number of statements in the programme.

Next *n* lines contain a statement each. Each statement contains exactly one operation (++ or --) and exactly one variable *x* (denoted as letter «X»). Thus, there are no empty statements. The operation and the variable can be written in any order.

**Output**

Print a single integer — the final value of *x*.

Examples

input

```
1
++X
```

output

```
1
```

input

```
2
X++
--X
```

output

```
0
```





【钟明衡，物理学院，2023年秋】

思路：

输入为'X++''++X'就加一，否则减一

##### 代码

```python
n = int(input())
ans = 0
for i in range(0, n):
    s = input()
    if s == 'X++' or s == '++X':
        ans += 1
    else:
        ans -= 1
print(ans)

```



代码运行截图

![image-20230926122504191](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230926122504191.png)



#### 339A. Helpful Maths

greedy/implementation/sortings/strings, 800, http://codeforces.com/problemset/problem/339/A

Xenia the beginner mathematician is a third year student at elementary school. She is now learning the addition operation.

The teacher has written down the sum of multiple numbers. Pupils should calculate the sum. To make the calculation easier, the sum only contains numbers 1, 2 and 3. Still, that isn't enough for Xenia. She is only beginning to count, so she can calculate a sum only if the summands follow in non-decreasing order. For example, she can't calculate sum 1+3+2+1 but she can calculate sums 1+1+2 and 3+3.

You've got the sum that was written on the board. Rearrange the summans and print the sum in such a way that Xenia can calculate the sum.

**Input**

The first line contains a non-empty string *s* — the sum Xenia needs to count. String *s* contains no spaces. It only contains digits and characters "+". Besides, string *s* is a correct sum of numbers 1, 2 and 3. String *s* is at most 100 characters long.

**Output**

Print the new sum that Xenia can count.

Examples

input

```
3+2+1
```

output

```
1+2+3
```

input

```
1+1+3+1+3
```

output

```
1+1+1+3+3
```

input

```
2
```

output

```
2
```



【钟明衡，物理学院，2023年秋】

思路：

先读取偶数位上的数字，排序后将原来的加号插回来，输出

##### 代码

```python
s = input()
a = []
for i in range(0, len(s), 2):
    a.append(s[i])
a.sort()
for i in range(1, len(s), 2):
    a.insert(i, s[i])
for b in a:
    print(b, end='')

```



代码运行截图 

![image-20230926123117572](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230926123117572.png)



## 2. 选做题目

#### OJ01017: 装箱问题

greedy, http://cs101.openjudge.cn/practice/01017

一个工厂制造的产品形状都是长方体，它们的高度都是h，长和宽都相等，一共有六个型号，他们的长宽分别为1\*1, 2\*2, 3\*3, 4\*4, 5\*5, 6\*6。这些产品通常使用一个 6\*6*h 的长方体包裹包装然后邮寄给客户。因为邮费很贵，所以工厂要想方设法的减小每个订单运送时的包裹数量。他们很需要有一个好的程序帮他们解决这个问题从而节省费用。现在这个程序由你来设计。

**输入**：输入文件包括几行，每一行代表一个订单。每个订单里的一行包括六个整数，中间用空格隔开，分别为1*1至6*6这六种产品的数量。输入文件将以6个0组成的一行结尾。

**输出**：除了输入的最后一行6个0以外，输入文件里每一行对应着输出文件的一行，每一行输出一个整数代表对应的订单所需的最小包裹数。

解题思路：4\*4, 5\*5, 6\*6这三种的处理方式较简单，就是每一个箱子至多只能有其中1个，根据他们的数量添加箱子，再用2\*2和1\*1填补。1\*1, 2\*2, 3\*3这些就需要额外分情况讨论，若有剩余的3\*3,每4个3\*3可以填满一个箱子，剩下的3\*3用2\*2和1\*1填补装箱。剩余的2\*2，每9个可以填满一个箱子，剩下的与1\*1一起装箱。最后每36个1\*1可以填满一个箱子，剩下的为一箱子。

样例输入

```
0 0 4 0 0 1 
7 5 1 0 0 0 
0 0 0 0 0 0 
```

样例输出

```
2 
1 
```

来源：Central Europe 1996



【钟明衡，物理学院，2023年秋】

思路：

6、5、4的必须占用一个箱子

放入5后还可以放11个1

放入4后还可以放5个2，如果在此过程中2放完了，就用1填补空余位置

一个箱子可以放最多4个3或9个2或36个1，将它们各自取余后进行下一步处理

如果3还剩1个，最多可放7个2，剩下最多放7个1（如果2不足就用4个1代替）：

3 3 3 2 2 1

3 3 3 2 2 1

3 3 3 1 2 2

2 2 2 2 2 2

2 2 2 2 2 2

1 1 1 1 2 2

如果3还剩2个，最多可放3个2，剩下最多放6个1：

3 3 3 3 3 3

3 3 3 3 3 3

3 3 3 3 3 3

2 2 2 2 2 2

2 2 2 2 2 2

1 1 1 1 1 1

如果3还剩3个，最多可放1个2，剩下最多放5个1：

3 3 3 3 3 3

3 3 3 3 3 3

3 3 3 3 3 3

3 3 3 2 2 1

3 3 3 2 2 1

3 3 3 1 1 1

如果还有剩1和2，则判断要多用2还是1个箱子，只需计算剩下所需的格子数是否达到36即可

##### 代码

```python
a = []
while True:
    l = list(map(int, input().split()))
    empty = True
    for i in l:
        if i != 0:
            empty = False
    if empty:
        break
    ans = l[5]
    if l[0] >= l[4]*11:
        ans += l[4]
        l[0] -= l[4]*11
    else:
        ans += l[4]
        l[0] = 0
    if l[1] >= l[3]*5:
        ans += l[3]
        l[1] -= l[3]*5
    elif l[1]*4+l[0] >= l[3]*20:
        ans += l[3]
        l[0] -= l[3]*20-l[1]*4
        l[1] = 0
    else:
        ans += l[3]
        l[1] = 0
        l[0] = 0
    ans += int(l[2]/4)+int(l[1]/9)+int(l[0]/36)
    l[2] %= 4
    l[1] %= 9
    l[0] %= 36
    if l[2] == 1:
        ans += 1
        if l[1] >= 5:
            l[1] -= 5
            if l[0] >= 7:
                l[0] -= 7
            else:
                l[0] = 0
        else:
            if 27-4*l[1] >= l[0]:
                l[1] = 0
                l[0] = 0
            else:
                l[0] -= 27-4*l[1]
                l[1] = 0
    elif l[2] == 2:
        ans += 1
        if l[1] >= 3:
            l[1] -= 3
            if l[0] >= 6:
                l[0] -= 6
            else:
                l[0] = 0
        else:
            if 18-4*l[1] >= l[0]:
                l[1] = 0
                l[0] = 0
            else:
                l[0] -= 18-4*l[1]
                l[1] = 0
    elif l[2] == 3:
        ans += 1
        if l[1] >= 1:
            l[1] -= 1
            if l[0] >= 5:
                l[0] -= 5
            else:
                l[0] = 0
        else:
            if 9 >= l[0]:
                l[0] = 0
            else:
                l[0] -= 9
    if l[0]+4*l[1] > 36:
        ans += 2
    elif 0 < l[0]+4*l[1] <= 36:
        ans += 1
    a.append(ans)
for ans in a:
    print(ans)

```



代码运行截图

![image-20230926123311408](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230926123311408.png)



## 3. 学习总结和收获

之前在做装箱子这题时，将一处操作顺序写反了

```python
        l[0] -= l[3]*20-l[1]*4
        l[1] = 0
```

写成了

```python
        l[1] = 0
        l[0] -= l[3]*20-l[1]*4
```

于是WA了很多次，还以为是装箱逻辑有问题，总是找不出原因

后来仔细读了代码，发现了这个bug，一改好就AC了

下次写代码的时候一定要想清楚每一行都在干什么

