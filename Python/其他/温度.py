# 12号娱乐选手
# 2023/3/13 21:32

# 输出字符串后将输入的量赋给c（input函数默认为str）
c = input('输入摄氏温度：')

# 将c的类型转化为float
c = float(c)

# 计算得到f（会自动识别为类型，由于计算中有float，此处应该为float
f = .8*c+32

# 输出f（字符串相加会直接接上，这里为了消除用逗号连接自动输出的空格）
print('华氏温度为：'+str(f))
