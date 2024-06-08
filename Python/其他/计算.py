# 12号娱乐选手
# 2023/3/14 16:51
# 定义一个函数，用于计算给定算式的值
def calculate(expression):
    # 将中括号和大括号转换成小括号
    expression = expression.replace('[','(').replace('{','(').replace(']',')').replace('}',')')
    # 循环处理括号内的表达式
    while '(' in expression:
        # 查找最内层的括号对应的位置
        start = expression.rfind('(')
        end = expression.find(')', start)
        # 提取括号内的表达式并计算
        sub_exp = expression[start + 1: end]
        result = str(eval(sub_exp))
        # 将原始表达式中的括号及其内部表达式替换为计算结果
        expression = expression[:start] + result + expression[end + 1:]
    # 返回最终的计算结果
    return eval(expression)

# 测试程序
exp = input("请输入算式：")
result = calculate(exp)
print("计算结果为：", result)