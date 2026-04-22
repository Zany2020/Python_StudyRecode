complex1 = 2 + 2j
#表示负数，j前面要有数字,cmplex后最好也有数字
str1 = 'hell'
str2 = "hhh"
str4 = '''sss'''
#同理
list1 = [complex1, str1, str2, str4]
#list 可变，有序，可多不同元素，是序列
tuple1 = (complex1, str1, str2, str4)
#tuple与list的不同是用（）而且不可变
set1 = {complex1, str1, str2, str4}
#set无序且唯一，用{}，是集合
frozenset = frozenset(complex1, str1, str2, str4)
#不可变的集合
dit1 = {"sss" : "mama", "hhh" : "baba"}
#无序的键值对

name = "jj"
age = 1
s = f"{name} {age}"
print(s)
#有变量在括号内就用f“”

#转换格式直接在前面加 ---(   )

print(type(s))
#打印出其类型
print(isinstance(s, str))
#判断是否是这个类型

#‘/’是浮点数的除法，‘//’才是整除， ‘**’是幂运算

#'and'->逻辑与，全真
#‘or’ 逻辑或， 有一个真
#not 逻辑非 与条件相反

i = 3
result_1 = i in list1
result_2 = i is tuple1
#in 在---里， is 是否为同一个


#<< , >> 按位移动，二进制计算， 如 2 << 2， 2的二进制左移2位为8
#& 二进制及逆行按位与运算 ， ^按位异或运算， |按位或运算
