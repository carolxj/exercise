'''
古代的称一斤是16两
练习： 在控制台中获取两，
计算是几斤零几两
显示
'''
# weight_liang = int(input("请输入两"))
# jin = weight_liang // 16
# liang = weight_liang % 16
# print(str(jin) + "斤零" + str(liang) + "两")
#
# # 在控制台钟录入距离，时间，初速度，计算加速度。
# # 匀变速直线运动的位移与时间公式：
# # 加速度 = (距离-初速度*时间）*2/时间的平方
# distance = int(input("请输入距离"))
# time = int(input("请输入时间"))
# initial_velocity = int(input("请输入初速度"))
# accelerated_speed = (distance - initial_velocity * time) * 2 / time ** 2
# print("加速度是：" + str(accelerated_speed))

# 在控制台中录入一个四位整数
# 计算每位相加和
# 显示结果
# 方法一
# number = int(input("请输入4位整数"))
# #个位
# unit01 = number % 10
# # 十位   1234 //10  -->123 %10 --> 3
# unit02 = number // 10 % 10
# # 百位1234 //100  -->12 %10 --> 2
# unit03 = number // 1000
# # 千位 1234 //1000  -->1
# unit04 =number // 1000
# result = unit01 + unit02 + unit03 + unit04
# print("结果是:" + str(result))
#
# # 方法二
# result = number % 10
# # 累加个位
# result += number // 10 % 10
# result += number //100 % 10
# result += number // 1000
# print("结果是:" + str(result))

# import getpass
#
# username = input("username")
# password = getpass.getpass("password")
# if username == 'bob' and password == '123456':
#     print("登录成功")
# else:
#     print("登录失败")

score = int(input("score"))

if score >= 90:
    print("优秀")
elif score >= 90 :
    print("好")
elif score >= 70:
    print("良")
elif score >= 60:
    print("及格")
else:
    print("你要努力了")
if score >= 60 and score <= 70:
    print("")
elif 70 <= score < 80:
    print()























































































































































































