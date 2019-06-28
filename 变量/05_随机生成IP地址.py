import random  # 导入random模块

# 随机生成IP地址四个段落的数字
section1 = random.randint(1, 255)
section2 = random.randint(1, 255)
section3 = random.randint(1, 255)
section4 = random.randint(1, 255)


# 组合IP地址
random_ip = str(section1) + '.' + str(section2) + '.' + str(section3) + '.' + str(section4)

print(random_ip)  # 打印结果
