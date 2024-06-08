# 12号娱乐选手
# 2023/3/13 21:18

# 导入turtle模块
import turtle

# 显示turtle
turtle.showturtle()

# 绘制字符串
turtle.write('要绘制的内容')

# 向前移动100像素，输入负数可以向后走
turtle.forward(100)

# 右转90度
turtle.right(90)

# 变成蓝色
turtle.color('blue')

# 抬笔
turtle.penup()

# 传送至(11,45)，不抬笔会画出一条直线
turtle.goto(11, 45)

# 落笔
turtle.pendown()

# 画半径为50,角度为120度的圆弧（左转为正，输入负数角度可以反向移动）
turtle.circle(50, 120)

# 点击退出，如果没有这一条或者下一条画完了会立即退出
turtle.exitonclick()

# 停在这个页面（结束）
# turtle.done()
