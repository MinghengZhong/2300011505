# Assignment #7: April 月考

Updated 1650 GMT+8 Apr 3, 2024

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

### 27706: 逐词倒放

http://cs101.openjudge.cn/practice/27706/



思路：

split以后反过来输出即可

代码

```python
print(' '.join(input().split()[::-1]))

```



代码运行截图

![image-20240403162104272](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240403162104272.png)



### 27951: 机器翻译

http://cs101.openjudge.cn/practice/27951/



思路：

用一个set和list来模拟内存，set用来以O(1)的复杂度查询，list用来处理从set中的删除操作

代码

```python
m, n = map(int, input().split())
l, s, ans, head = [], set(), 0, 0
for i in list(map(int, input().split())):
    if i not in s:
        ans += 1
        s.add(i)
        l.append(i)
        if len(l)-head > m:
            s.remove(l[head])
            head += 1
print(ans)

```



代码运行截图

![image-20240403162135763](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240403162135763.png)



### 27932: Less or Equal

http://cs101.openjudge.cn/practice/27932/



思路：

被坑了，注意到x只能在1到1e9之间，除了最基本的排除$l[k-1]==l[k]$情况，还要排除x无法取在范围内的情况

代码

```python
n, k = map(int, input().split())
l = sorted(list(map(int, input().split())))
if k == n:
    print(l[-1] if l[-1] <= 1e9 else -1)
elif 0 < k < n:
    if l[k-1] == l[k] or l[k] <= 1:
        print(-1)
    else:
        print(max(1, l[k-1]))
elif k == 0:
    print(1 if l[0] > 1 else -1)
else:
    print(-1)

```



代码运行截图

![image-20240403162704546](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240403162704546.png)



### 27948: FBI树

http://cs101.openjudge.cn/practice/27948/



思路：

按照正常顺序遍历，然后从底层开始输出，正好能满足后序的要求。如果是叶子节点，就0/1输出B/I，之后的输出对比左右两个子树的返回值，如果相同就输出并返回这个值，否则为F（两个都是F则自动也是F，不影响）

代码

```python
def suf(s, n):
    if s == '1':
        print('I', end='')
        return 'I'
    if s == '0':
        print('B', end='')
        return 'B'
    a, b = suf(s[0:1 << (n-1)], n-1), suf(s[1 << (n-1):], n-1)
    if a == b:
        print(a, end='')
        return a
    else:
        print('F', end='')
        return 'F'


n = int(input())
s = input()
k = suf(s, n)

```



代码运行截图

![image-20240403163041130](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240403163041130.png)



### 27925: 小组队列

http://cs101.openjudge.cn/practice/27925/



思路：

用链表来代表队列，记录队列的头、尾以及每个分组的尾，然后按照要求插入、输出即可

代码

```python
from collections import defaultdict as D
t = int(input())
num = {}
tail_list = ['' for _ in range(t)]
next, head, tail = D(str), '', ''
for i in range(t):
    for new in input().split():
        num[new] = i
while (s := input()) != 'STOP':
    if s[0] == 'D':
        print(head)
        if tail_list[num[head]] == head:
            tail_list[num[head]] = ''
        head = next[head]
    else:
        new = s[8:]
        if not head:
            head = new
            tail = new
        else:
            Tail = tail_list[num[new]]
            if Tail:
                next[new], next[Tail] = next[Tail], new
                if Tail == tail:
                    tail = new
            else:
                next[tail] = new
                tail = new
        tail_list[num[new]] = new
        
```



代码运行截图

![image-20240403173655255](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240403173655255.png)



### 27928: 遍历树

http://cs101.openjudge.cn/practice/27928/



思路：

按照父子节点大小关系，把子节点分为左边和右边，最后按照中序遍历输出就是结果（左右子树都按照从小到大排序）

代码

```python
from collections import defaultdict as D
l, r = D(lambda: []), D(lambda: [])


def mid(x):
    for a in sorted(l[x]):
        mid(a)
    print(x)
    for a in sorted(r[x]):
        mid(a)
    return


n = int(input())
not_root, is_root = set(), set()
for _ in range(n):
    L = list(map(int, input().split()))
    is_root.add(L[0])
    for i in range(1, len(L)):
        not_root.add(L[i])
        if L[i] < L[0]:
            l[L[0]].append(L[i])
        else:
            r[L[0]].append(L[i])
for a in is_root:
    if a not in not_root:
        mid(a)

```



代码运行截图

![image-20240403163929071](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240403163929071.png)



## 2. 学习总结和收获

月考题做起来还比较舒适，除了Less or Equal有点坑，感觉其他题目还是比较直白的，很适合练习数据结构

小组队列一开始没看题就做了，可惜OJ数据太弱让我给过了，后来重新写了一个，感谢万能的群友🙏





