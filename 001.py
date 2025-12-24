# print("Hello World")
# print("I Love Rem'rem'\n")
# print('I Love Rem"rem"')
# print('I Love Rem\'rem"')#
# my_love = "rem"
# print("masahiro" + my_love)
#
# import math
# result = math.log2(8)
# print(result)
#
# lalalai = 'Raftaria'[2]
# lalalaii = "Raftaria"[2]
# print(lalalai)
# print(lalalaii)
# print(type(my_love))
#
# jiji = input("请输入你喜欢的人的名字：")W
# print(jiji)
# print(input)#错误

# rem_hight = float(input("请输入rem的身高："))
# rem_weigth = float(input("请输入rem的体重："))
# rem_bmi = rem_weigth / (rem_hight) ** 2
# # print("rem的BMI为：" + rem_bmi)
# print("rem的BMI为：" + str(rem_bmi))
# #这里要转化成字符串类型才可以打印

# rem = 2020
# if (rem == 2020):
#     print("rem")
# if rem == 2020:
#     print("rem")

#
# shoping_list = []
# shoping_list.append("手办")
# shoping_list.append("谷子")
# print(shoping_list)
# print(len(shoping_list))
# print(shoping_list[1])
#
# shoping_list.remove("谷子")
# print(shoping_list)
# print(len(shoping_list))

# prince = [233, 520, 202, 710]
# max_price = max(prince)
# min_price = min(prince)
# sorted_prince = sorted(prince)
# print(sorted_prince)
# print(max_price)
# print(min_price)


# love_girl = {"rem": "2020", "Arima Kana": "2025.12"}
# love_girl["Kurokawa Akane"] = "2025"
# print(love_girl)
#
# Girl = input("请输入她的名字")
# if Girl in love_girl:
#     print(Girl + "你于" + love_girl[Girl] + "相遇")
#     print("目前里面有" + str(len(love_girl)) + "条。")
#

# temperature_dict = {"rem": 37.2, "Akane": 36.8, "Kana": 36.5}
# # temperature_dict.keys() -> 所有键
# # temperature_dict.values() -> 所有值
# # temperature_dict.items() -> 所有键值对
# for(name, temperature) in temperature_dict.items():
#     if temperature >= 37:
#         print(name)
# # range(起始值， 结束值<不包括>, 步长)#没有起始值则默认为零
# i = 0
# for name in range(1, 101):
#     i = i + name
# print(name, i)
# #无 “临时局部” 概念：除非变量定义在函数内（函数级局部变量），否则模块级的变量全程可访问
# #但第二个循环里 name 会覆盖第一个循环的 name
# #name生命周期不绑定循环：循环结束后，变量不会销毁，而是保留最后一次迭代的值


# year = "龙"
# name = "小明"
# 1.
# # 无 f：{year} 不会替换，只是字面字符
# content = """
# 律回春渐，新元肇启。
# 金{year}贺岁，欢乐祥瑞。
# 给{name}拜年！"""
# print(content)
# print("\n")
#
# 2.
# # 加 f：{year}/{name} 会被替换成变量值
# content = f"""
# 律回春渐，新元肇启。
# 金{year}贺岁，欢乐祥瑞。
# 给{name}拜年！"""
# print(content)
# print("\n")
#
# 3.
# content = """
# 律回春渐，新元肇启。
# 金{0}贺岁，欢乐祥瑞。
# 给{1}拜年！""".format(year, name)
# # 或者：
# # 金{year_}贺岁，欢乐祥瑞s。
# # 给{name_}拜年！.format(year_ = year, name_ = name)
# print(content)
# print("\n")
#

# high_girl = {"Kana" : 150, "Ruby" : 158, "Akane" : 163}
# for name, high in high_girl.items():
#     print("{0}, {1:.2f}".format(name, high))
#     print(f"{name} {high:.2f}")
#     #：.nf表示保留n位小数； 前面的f就是索取变量上面的数值


# def ding_yi_han_shu():

# # 1.引入后要写出其变量名
# import statistics
# print(statistics.median([1,2,3,4,5]))
# print(statistics.mean([1,2,3,4,5]))
#
# # 2.后面专门接要用到的内函数就好
# from statistics import median, mean
# print(mean([1,2,3,4,5]))
# print(median([1,2,3,4,5]))
#
# # 3. *是指的全部包含但不推荐怕重名。
# from statistics import *
# print(median([1,2,3,4,5]))
# print(mean([1,2,3,4,5]))


class CuteGirl:
    def __init__(self, name, high):
        self.name = name
        self.high = high
    def color(self, color):
        self.color = color

Akane = CuteGirl("Akane", 163)
Kana = CuteGirl("Kana", 150)
Ruby = CuteGirl("Ruby", 158)
Akane.color("Blue")
Kana.color("Red")
Ruby.color("Yellow")
print(Akane.name, Akane.high, Akane.color)
print(Kana.name, Kana.high, Kana.color)
print(Ruby.name, Ruby.high, Ruby.color)




































