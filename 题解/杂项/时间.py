# 12号娱乐选手
# 2023/3/14 9:48

# 调用时间、日期
import time
import datetime

# 显示1970年1月1日0：00到现在已经过的时间（秒）
print(time.time())

# 显示当前日期（此处now可换成today）
print(datetime.date.today())

# 显示当前日期和时间，时间会精确到毫秒
print(datetime.datetime.now())

# 自定义输出格式strftime()
# %Y年 %y年后两位
# %m月 %b,%h月英文简写 %B月英文全称
# %a星期简写 %A星期全称
# %d日 %D输出mm/dd/yy
# %H小时 %M分钟 %S秒
# %c会输出“星期简写 月简写 日 时：分：秒 年”
print(datetime.datetime.now().strftime('%c'))

# datetime包含了所有日期和时间信息，其类型为datetime.datetime（前面那个就是date）
# 在datetime类型变量后面.strftime('')可以从中以引号内的格式调出str类型的值
# 用strptime可以以一定格式设定一个时间
# datetime之间可以做减法得到时间差
future = datetime.datetime.strptime('2077/04/04 0:00:00', '%Y/%m/%d %H:%M:%S')
# 默认的输出日期用短线连接
print(future)

# datetime.timedelta()括号内是时间差，可以和datetime.datetime类型加减
print('十天后', (datetime.datetime.now()+datetime.timedelta(days=10)).strftime('%c'))
