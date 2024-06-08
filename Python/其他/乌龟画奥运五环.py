# 12号娱乐选手
# 2023/3/14 16:50
import turtle

# 画蓝色圆环
turtle.penup()
turtle.goto(-120, 0) # 移动到左侧
turtle.pendown()
turtle.color("blue")
turtle.circle(50)

# 画黄色圆环
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.color("yellow")
turtle.circle(50)

# 画黑色圆环
turtle.penup()
turtle.goto(120, 0) # 移动到右侧
turtle.pendown()
turtle.color("black")
turtle.circle(50)

# 画绿色圆环
turtle.penup()
turtle.goto(-60, -50) # 移动到左下方
turtle.pendown()
turtle.color("green")
turtle.circle(50)

# 画红色圆环
turtle.penup()
turtle.goto(60, -50) # 移动到右下方
turtle.pendown()
turtle.color("red")
turtle.circle(50)

# 隐藏海龟
turtle.hideturtle()

# 点击关闭窗口退出程序
turtle.exitonclick()