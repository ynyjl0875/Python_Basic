"""
需求: 1.苹果的价格、重量是收营员手动输入的；2.数据类型为小数
"""

price = float(input("请输入苹果的价格："))
weight = float(input("请输入苹果的重量："))
money = price*weight
print(money)

# 变量格式化输出  %格式化操作符
"""
%s 字符串
%d 十进制整数 %06d 表示整数显示的位数，不足的地方0补全
%f 浮点数 %.02f 显示后两位
%% 输出%
"""

# 苹果单价9.00元/斤，购买了5.00斤，需要支付45.00元
print("苹果单价%.03f元/斤，购买了%.03f斤，需要支付%.03f元" % (price, weight, money))
