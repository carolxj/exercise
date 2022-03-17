'''
数据类型转换
运算符
算法运算符
增强运算符
'''
'''# int   float   str
str_usd = input("请输入美元")
# 类型转换  str --> int
int_usd = int(str_usd)
result = int_usd * 6.9 # 这里不能直接用str_usd乘，因为字符串不能和数字相乘，需要转换成整型
str_result = str(result) # 字符串+ 数值不能直接打印，需要将数值先转换成字符串
# str + 数值 -->  str + 数值
print("结果是：" + str_result)'''
'''
# 2. 运算符
# 地板除（保留整数）
print(5 // 2)# 商2
# 余（求余）
print(5 % 2) # 余1
# 除（结果为浮点数）
print(5 / 2) # 余2.5
# 获取整数的个位
print(27 % 10) # 7
# 幂运算
# 5的2次方：5*5
print(5**2)
# 5的3次方：5*5*5
print(5**3)

# 3. 增强运算符
number01 = 200
print(number01 + 1)
print(number01) #200
number01 = number01 + 1 # 变量加上另外一个数再赋值给自身
number01 += 1 #在自身基础上累加，等同于上一行
print(number01)
'''
'''# 练习1 ： 在控制台中，录入一个商品单价
str_price = input("请输入商品单价")
price = float(str_price)
#再录入一个数量
str_count = input("请输入商品数量")
count = float(str_count)
#最后获得金额，
str_money = input("请输入金额")
money = float(str_money)
# 计算应该找回金额
result = money - price * count
print("应该找回" + str(result))'''

# 练习2 : 在控制台获取分钟
# 再获取小时
# 再获取天
# 计算总秒数
minute = int(input("请输入分钟数"))
hour = int(input("请输入小时"))
day = int(input("请输入天数"))
result = minute*60 + hour*60*60 + day*24*60*60
print("总秒数是" + str(result))