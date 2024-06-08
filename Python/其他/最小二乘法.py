# 12号娱乐选手
# 2023/3/14 16:52
import math
import statistics
import turtle

# 输入数据组数
n = int(input("请输入数据组数："))

# 初始化x、y列表
x_list = []
y_list = []

# 依次输入x和y值，并将其添加到列表中
for i in range(n):
    x = float(input("请输入x值："))
    y = float(input("请输入y值："))
    x_list.append(x)
    y_list.append(y)

# 计算x均值和y均值
x_mean = statistics.mean(x_list)
y_mean = statistics.mean(y_list)

# 计算x方差和y方差
x_variance = statistics.variance(x_list)
y_variance = statistics.variance(y_list)

# 计算协方差和相关系数
covariance = sum([(x - x_mean) * (y - y_mean) for x, y in zip(x_list, y_list)]) / (n - 1)
correlation_coefficient = covariance / math.sqrt(x_variance * y_variance)

# 计算回归系数a和b
a = covariance / x_variance
b = y_mean - a * x_mean

# 输出结果
print("拟合直线方程为：y = {}x + {}".format(a, b))
print("相关系数r为：{}".format(correlation_coefficient))

# 绘制散点图和拟合直线
print("散点图和拟合直线如下：")

# 创建画布和画笔
canvas = turtle.Screen()
canvas.bgcolor("white")
pen = turtle.Turtle()

# 设置画笔颜色和形状
pen.color("blue")
pen.shape("circle")

# 绘制每一组(x,y)对应的点
for x, y in zip(x_list, y_list):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.stamp()

# 重置画笔颜色和形状
pen.color("red")
pen.shape("classic")

# 绘制拟合直线
x_min = min(x_list)
x_max = max(x_list)
y_min = a * x_min + b
y_max = a * x_max + b
pen.penup()
pen.goto(x_min, y_min)
pen.pendown()
pen.goto(x_max, y_max)

# 关闭画布
canvas.exitonclick()
