# 12号娱乐选手
# 2023/3/13 21:40

# 标识符只能包含字母数字和下划线，且不可以以数字开头
# 注意不要和文件名、函数之类的重名了

# 变量类型有int float bool str
# 用type()函数查看某个东西的类型（不限于变量）
a = 1
print('a=', a, type(a))
b = 1.2
print('b=', b, type(b))
c = True
print('c=', c, type(c))
d = '草'
print('d=', d, type(d))

# 变量名带着一个指针指向一个值以及这个值的存储代号，存储代号决定于值而非变量，代号用id()查看
# 相同赋值的变量会指向同一个号，如果赋给变量其他值，之前存储的这个值还在那，浪费内存
a = 1
print('a=1的id', id(a))
a = 2
print('a=2的id', id(a))
a = 1
print('再次a=1的id', id(a))


# 可以互相转换，比如b=int(b)是将b转化成整数
# float转int会抹掉小数部分
b = int(b)
print('int(b)=', b)

# float换成int时用round四舍五入
print('6.7四舍五入后为', round(6.7))

# eval可以自动识别并转换字符串，eval(input())比较方便

# + - * / 不用多说
# 另外加号可以把字符串拼起来，比如下面这行可以把输出中间的空格去掉
print('int(b)='+str(b))

# 幂次是**
print('6**2=', 6**2)

# 整除是//
print('5//2=', 5//2)

# 取余是%
print('5%2=', 5 % 2)

# 快速计算，如a=a+1可以写为a+=1
# += -= *= /= **= //= %=

# 保留小数位
a = 6.7777
print(a, '保留两位小数结果为', round(a*100)/100)

# \n换行符 \t制表符
print('aaa:\n\taaaa\n\tbbbbb\n\tcccccc')
