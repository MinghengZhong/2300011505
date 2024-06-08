# Assignment #3: March月考

Updated 1900 GMT+8 March 6, 2024

2024 spring, Complied by 钟明衡 物理学院



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:
- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

操作系统：Windows_NT x64 10.0.19045

Python编程环境：Visual Studio Code 1.76.1

C/C++编程环境：Visual Studio Code 1.76.1



## 1. 题目

**02945: 拦截导弹**

http://cs101.openjudge.cn/practice/02945/



思路：

对于每一颗导弹，如果拦截了这颗导弹，此时总拦截次数为前面导弹高度高于此导弹的拦截数最大值+1，即：
$$
ans[i]=max(ans[j]+1),(j<i,H[j]>H[i])
$$


##### 代码

```python
n = int(input())
l = list(map(int, input().split()))
ans = [1]*n
for i in range(n):
    for j in range(i):
        if l[j] >= l[i]:
            ans[i] = max(ans[i], ans[j]+1)
print(max(ans))

```



代码运行截图

![image-20240306171538269](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240306171538269.png)



**04147:汉诺塔问题(Tower of Hanoi)**

http://cs101.openjudge.cn/practice/04147



思路：

定义一个$H(n,a,b,c)$函数，其含义为：将一个$n$层的汉诺塔从$a$移动到$c$

这一步，相当于先将$n-1$层的汉诺塔从$a$移到$b$，然后将$n$从$a$移到$c$，再将$n-1$层的汉诺塔从$b$移到$c$

即$H(n,a,b,c)=H(n-1,a,c,b)+(n:a->c)+H(n-1,b,a,c)$

##### 代码

```python
def H(n, a, b, c):
    if n:
        H(n-1, a, c, b)
        print('%d:%s->%s' % (n, a, c))
        H(n-1, b, a, c)


n, a, b, c = input().split()
H(int(n), a, b, c) 

```



代码运行截图

![image-20240306173216177](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240306173216177.png)



**03253: 约瑟夫问题No.2**

http://cs101.openjudge.cn/practice/03253



思路：

使用链表（用一个指针列表实现），当一个元素被删除，就把指向它的指针指向它的指针指向的元素（？什么绕口令）

##### 代码

```python
while True:
    n, p, k = map(int, input().split())
    if n == 0:
        break
    l = []
    next = [i+1 for i in range(n+1)]
    next[-1] = 1
    i = p-1
    for _ in range(n):
        for j in range(k-1):
            i = next[i]
        l.append(next[i])
        next[i] = next[next[i]]
    print(','.join(map(str, l)))
    
```



代码运行截图

![image-20240306174253145](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240306174253145.png)



**21554:排队做实验 (greedy)v0.2**

http://cs101.openjudge.cn/practice/21554



思路：

显然按照从小到大排序即为最佳顺序，输出顺序以及计算平均时间即可

##### 代码

```python
n = int(input())
l = list(map(int, input().split()))
t = sorted([i+1 for i in range(n)], key=lambda i: l[i-1])
ans = 0
l.sort(reverse=True)
for i in range(n):
    ans += i*l[i]
print(' '.join(map(str, t)))
print('%.2f' % (ans/n))

```



代码运行截图

![image-20240306175315173](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240306175315173.png)



**19963:买学区房**

http://cs101.openjudge.cn/practice/19963



思路：

按照要求计算出中位数，然后比较即可

##### 代码

```python
n = int(input())
inp = [i[1:-1] for i in input().split()]
s = [sum(map(int, inp[i].split(','))) for i in range(n)]
inp = list(map(int, input().split()))
l = [inp[i] for i in range(n)]
for i in range(n):
    s[i] = s[i]/l[i]
ss = sorted(s)
ll = sorted(l)
if n % 2 == 0:
    mids = (ss[n//2-1]+ss[n//2])/2
    midl = (ll[n//2-1]+ll[n//2])/2
else:
    mids = ss[n//2]
    midl = ll[n//2]
ans = 0
for i in range(n):
    if s[i] > mids and l[i] < midl:
        ans += 1
print(ans) 

```



代码运行截图

![image-20240306175424636](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240306175424636.png)



**27300: 模型整理**

http://cs101.openjudge.cn/practice/27300



思路：

按照要求输入，然后排序好了输出即可

##### 代码

```python
from collections import defaultdict


def v(s):
    n = float(s[:-1])
    if s[-1] == 'B':
        n *= 1000
    return n


d = defaultdict(lambda: [])
for _ in range(int(input())):
    a, b = input().split('-')
    d[a].append(b)
for a in sorted(list(d.keys())):
    print('%s: %s' %
          (a, ', '.join(map(str, sorted(d[a], key=lambda i: v(i))))))
    
```



代码运行截图

![image-20240306182413584](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240306182413584.png)



## 2. 学习总结和收获

通过汉诺塔问题复习了递归的思想，感觉这题的解法非常优美

defaultdict真是好东西



