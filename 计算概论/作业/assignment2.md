# Assignment #2: 字符串相关

### 钟明衡2300011505

### 2023/9/21

**说明：**

1）第2周课上讲到了计算机相关的历史，介绍了ASCII表。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）同学完成作业的时候，就是这个模版文件中修改补充好。为便于助教批改作业，请尽量不要删除其他文字。

5）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统：Windows_NT x64 10.0.19045

Python编程环境：Visual Studio Code 1.76.1

C/C++编程环境：Visual Studio Code 1.76.1



## 1. 必做题目

#### 71A. Way Too Long Words

strings, 1000, http://codeforces.com/problemset/problem/71/A

Sometimes some words like "*localization*" or "*internationalization*" are so long that writing them many times in one text is quite tiresome.

Let's consider a word *too long*, if its length is **strictly more** than 10 characters. All too long words should be replaced with a special abbreviation.

This abbreviation is made like this: we write down the first and the last letter of a word and between them we write the number of letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.

Thus, "*localization*" will be spelt as "*l10n*", and "*internationalization*" will be spelt as "i18n".

You are suggested to automatize the process of changing the words with abbreviations. At that all too long words should be replaced by the abbreviation and the words that are not too long should not undergo any changes.

**Input**

The first line contains an integer *n* (1 ≤ *n* ≤ 100). Each of the following *n* lines contains one word. All the words consist of lowercase Latin letters and possess the lengths of from 1 to 100 characters.

**Output**

Print *n* lines. The *i*-th line should contain the result of replacing of the *i*-th word from the input data.

Examples

input

```
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
```

output

```
word
l10n
i18n
p43s
```



【钟明衡，物理学院，2023年秋】

思路：

输入字符串，如果长度不大于10，则输出它本身

否则，输它的第一个字符 +（长度 - 2 ）+ 最后一个字符

##### Python3 代码

```python
n = int(input())
i = 1
while i <= n:
    i += 1
    s = input()
    if len(s) <= 10:
        print(s)
    else:
        print(s[0]+str(len(s)-2)+s[-1])

```



Python代码运行截图

![image-20230921201424225](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230921201424225.png)



#### 112A. Petya and Strings

implementation/strings, 800, http://codeforces.com/problemset/problem/112/A

Little Petya loves presents. His mum bought him two strings of the same size for his birthday. The strings consist of uppercase and lowercase Latin letters. Now Petya wants to compare those two strings lexicographically. The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter. Help Petya perform the comparison.

**Input**

Each of the first two lines contains a bought string. The strings' lengths range from 1 to 100 inclusive. It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.

**Output**

If the first string is less than the second one, print "-1". If the second string is less than the first one, print "1". If the strings are equal, print "0". Note that the letters' case is not taken into consideration when the strings are compared.

Examples

input

```
aaaa
aaaA
```

output

```
0
```

input

```
abs
Abz
```

output

```
-1
```

input

```
abcdefg
AbCdEfF
```

output

```
1
```

Note

If you want more formal information about the lexicographical order (also known as the "dictionary order" or "alphabetical order"), you can visit the following site:

- http://en.wikipedia.org/wiki/Lexicographical_order



【钟明衡，物理学院，2023年秋】

思路：

将两个字符串全部换成小写（大写也可以），然后比较，按照要求输出结果即可

##### Python3 代码

```python
a = input().lower()
b = input().lower()
if a > b:
    print(1)
elif a < b:
    print(-1)
else:
    print(0)
```



Python代码运行截图 

![image-20230921201649132](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230921201649132.png)



#### 158A. Next Round

*special problem/implementation, 800, http://codeforces.com/problemset/problem/158/A

"Contestant who earns a score equal to or greater than the *k*-th place finisher's score will advance to the next round, as long as the contestant earns a positive score..." — an excerpt from contest rules.

A total of *n* participants took part in the contest (*n* ≥ *k*), and you already know their scores. Calculate how many participants will advance to the next round.

**Input**

The first line of the input contains two integers *n* and *k* (1 ≤ *k* ≤ *n* ≤ 50) separated by a single space.

The second line contains *n* space-separated integers *a*~1~, *a*~2~, ..., a~n~ (0 ≤ a~i~ ≤ 100), where a~i~ is the score earned by the participant who got the *i*-th place. The given sequence is non-increasing (that is, for all *i* from 1 to *n* - 1 the following condition is fulfilled: a~i~ ≥ a~i~ + 1).

**Output**

Output the number of participants who advance to the next round.

Examples

input

```
8 5
10 9 8 7 7 7 5 5
```

output

```
6
```

input

```
4 2
0 0 0 0
```

output

```
0
```

Note

In the first example the participant on the 5th place earned 7 points. As the participant on the 6th place also earned 7 points, there are 6 advancers.

In the second example nobody got a positive score.



【钟明衡，物理学院，2023年秋】

思路：

一个个比较，如果参赛者的分数比第k位更高，且大于零，则答案+1

注意第k位在列表中的指标k-1

##### Python3 代码

```python
l = list(map(int, input().split()))
a = list(map(int, input().split()))
n = l[0]
k = l[1]
ans = 0
for i in range(0, n):
    if a[i] >= a[k-1] and a[i] > 0:
        ans += 1
print(ans)

```



Python代码运行截图

![image-20230921204120116](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230921204120116.png)



#### 58A. Chat room

greedy/strings, 1000, http://codeforces.com/problemset/problem/58/A

Vasya has recently learned to type and log on to the Internet. He immediately entered a chat room and decided to say hello to everybody. Vasya typed the word *s*. It is considered that Vasya managed to say hello if several letters can be deleted from the typed word so that it resulted in the word "hello". For example, if Vasya types the word "ahhellllloou", it will be considered that he said hello, and if he types "hlelo", it will be considered that Vasya got misunderstood and he didn't manage to say hello. Determine whether Vasya managed to say hello by the given word *s*.

**Input**

The first and only line contains the word *s*, which Vasya typed. This word consisits of small Latin letters, its length is no less that 1 and no more than 100 letters.

**Output**

If Vasya managed to say hello, print "YES", otherwise print "NO".

Examples

input

```
ahhellllloou
```

output

```
YES
```

input

```
hlelo
```

output

```
NO
```





【钟明衡，物理学院，2023年秋】

思路：

依题意，是要删除数个字符后，得到'hello'

那么只需要在原字符串中一个个检索，从'h'开始，检测到后变为检测'e'，以此类推

如果依次检测到了'h' 'e' 'l' 'l' 'o'，则可以输出YES，否则输出NO

##### Python3 代码

```python
s = input()
c = 0
l = ['h', 'e', 'l', 'l', 'o', '012']
for i in range(0, len(s)):
    if s[i] == l[c]:
        c += 1
if c == 5:
    print('YES')
else:
    print('NO')

```



Python代码运行截图

![image-20230928105645305](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230928105645305.png)



#### 04015: 邮箱验证

strings, http://cs101.openjudge.cn/practice/04015

POJ 注册的时候需要用户输入邮箱，验证邮箱的规则包括：
1)有且仅有一个'@'符号
2)'@'和'.'不能出现在字符串的首和尾
3)'@'之后至少要有一个'.'，并且'@'不能和'.'直接相连
满足以上3条的字符串为合法邮箱，否则不合法，
编写程序验证输入是否合法

**输入**

输入包含若干行，每一行为一个代验证的邮箱地址，长度小于100

**输出**

每一行输入对应一行输出
如果验证合法，输出 YES
如果验证非法：输出 NO

样例输入

```
.a@b.com
pku@edu.cn
cs101@gmail.com
cs101@gmail
```

样例输出

```
NO
YES
YES
NO
```





【钟明衡，物理学院，2023年秋】

思路：

首先排除头尾是'.'或'@'的情况

其次从头到尾检查是否为'@'，首次检查到时就排除前后存在'.'的情况，如果检查到第二个'@'，也直接排除

没检查到'@'，或者'@'后面没有出现过'.'，也排除

##### Python3 代码

```python
def check(s):
    if s[0] == '.' or s[0] == '@' or s[-1] == '.' or s[-1] == '@':
        return 'NO'
    at = False
    dot = False
    for i in range(1, len(s)-1):
        if s[i] == '@':
            if at:
                return 'NO'
            else:
                if s[i+1] == '.' or s[i-1] == '.':
                    return 'NO'
                else:
                    at = True
        elif s[i] == '.' and at:
            dot = True
    if dot and at:
        return 'YES'
    else:
        return 'NO'


while True:
    try:
        s = input()
        print(check(s))
    except EOFError:
        break

```



Python代码运行截图

![image-20230921205947017](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230921205947017.png)



## 2. 选做题目

#### OJ01008: Maya Calendar

math, http://cs101.openjudge.cn/practice/01008/

During his last sabbatical, professor M. A. Ya made a surprising discovery about the old Maya calendar. From an old knotted message, professor discovered that the Maya civilization used a 365 day long year, called Haab, which had 19 months. Each of the first 18 months was 20 days long, and the names of the months were pop, no, zip, zotz, tzec, xul, yoxkin, mol, chen, yax, zac, ceh, mac, kankin, muan, pax, koyab, cumhu. Instead of having names, the days of the months were denoted by numbers starting from 0 to 19. The last month of Haab was called uayet and had 5 days denoted by numbers 0, 1, 2, 3, 4. The Maya believed that this month was unlucky, the court of justice was not in session, the trade stopped, people did not even sweep the floor. For religious purposes, the Maya used another calendar in which the year was called Tzolkin (holly year). The year was divided into thirteen periods, each 20 days long. Each day was denoted by a pair consisting of a number and the name of the day. They used 20 names: imix, ik, akbal, kan, chicchan, cimi, manik, lamat, muluk, ok, chuen, eb, ben, ix, mem, cib, caban, eznab, canac, ahau and 13 numbers; both in cycles. Notice that each day has an unambiguous description. For example, at the beginning of the year the days were described as follows: 1 imix, 2 ik, 3 akbal, 4 kan, 5 chicchan, 6 cimi, 7 manik, 8 lamat, 9 muluk, 10 ok, 11 chuen, 12 eb, 13 ben, 1 ix, 2 mem, 3 cib, 4 caban, 5 eznab, 6 canac, 7 ahau, and again in the next period 8 imix, 9 ik, 10 akbal . . . Years (both Haab and Tzolkin) were denoted by numbers 0, 1, . . . , where the number 0 was the beginning of the world. Thus, the first day was: Haab: 0. pop 0 Tzolkin: 1 imix 0 Help professor M. A. Ya and write a program for him to convert the dates from the Haab calendar to the Tzolkin calendar. 

**输入**

The date in Haab is given in the following format:
NumberOfTheDay. Month Year

The first line of the input file contains the number of the input dates in the file. The next n lines contain n dates in the Haab calendar format, each in separate line. The year is smaller then 5000.

**输出**

The date in Tzolkin should be in the following format:
Number NameOfTheDay Year

The first line of the output file contains the number of the output dates. In the next n lines, there are dates in the Tzolkin calendar format, in the order corresponding to the input dates.

样例输入

```
3
10. zac 0
0. pop 0
10. zac 1995
```

样例输出

```
3
3 chuen 0
1 imix 0
9 cimi 2801
```

来源

Central Europe 1995



【钟明衡，物理学院，2023年秋】

思路：

先由第一种历法计算出天数，再反过来求出第二种历法的表示法

##### Python3 代码

```python
n = int(input())
print(n)
for i in range(0, n):
    day1, month1, year1 = input().split(' ')
    l1 = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax',
          'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu', 'uayet']
    l2 = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk',
          'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
    count = int(float(day1))+20*l1.index(month1)+365*int(year1)
    print(str(count % 13+1)+' '+l2[count % 20]+' '+str(int(count/260)))


```



Python代码运行截图

![image-20230921203501229](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230921203501229.png)



## 3. 学习总结和收获

Python的字符串还是很方便的，可以方便地调用其中的每一个字符

此类题目经常要使用if大法，如果不考虑全面很容易WA

两个网站相比起来，我更喜欢CF，因为它有难度分级，可以查看样例，从而避免了很多浪费时间的情况。此外，英文题目也让我的英文阅读能力有所提升
