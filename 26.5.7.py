# 编写函数，接收任意多个实数，返回一个元组，其中第一个元素为所有参数的平均值，其他元素为
# 所有参数中大于平均值的实数。
import chances
from unicodedata import digit


def l5_1(*arr):
    total = sum(arr)
    aver = total / len(arr)
    result = [aver]

    for i in arr:
        if (aver > i):
            result.append(i)

    return tuple(result)


# 编写函数，接收字符串参数，返回一个元组，其中第一个元素为大写字母个数，第二个元素为小写
# 字母个数

def l5_2(s):
    upper = 0
    lower = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.isupper():
            lower += 1
    return (upper, lower)


# 编写函数，接收包含n个整数的列表lst和一个整数k（0<=k<n）作为参数，返回新列表。处理规则
# 为：将列表lst中下标k（不包括k）之前的元素逆序，下标k（包括k）之后的元素逆序，然后将整个列表lst
# 中的所有元素逆序，返回处理后的新列表。

def l5_3(*lst, k):
    p1 = lst[:k][::-1]
    p2 = lst[k:][::-1]
    r = p1 + p2
    result = r[::-1]
    return result


# 杨辉三角
def l5_4(t):
    t_ = []
    for i in range(t):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = t[i - 1][j - 1] + t_[i - 1][j]
            t_.append(row)
        print(row)


# 编写函数，接收一个正偶数为参数，输出两个素数，并且这两个素数之和等于原来的正偶数。如果
# 存在多组符合条件的素数，则全部输出
def l5_5_1(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def l5_5_2(num):
    global chances
    if num % 2 != 0 or num <= 0:
        return "no"
    res = []
    for i in range(2, num // 2 + 1):
        if l5_5_1(i) and l5_5_1(num - i):
            res.append((i, num - i))
            return res

    ###################################################
    # 编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元
    # 素为最小公倍数
    def l7(a, b):
        m, n = a, b
        while b != 0:
            a, b = b, a % b
        gcb = a
        lcm = m * n // gcb
        return gcb, lcm

    # 编写函数，计算字符串匹配的准确率。以打字练习程序为例，假设参数origin变量保存的事原始字
    # 符串内容，userInput变量保存用户输入的内容，下面的代码用来测试用户输入的准确率。（自定义origin
    # 的内容）
    def c(o, i):
        min_len = min(len(o), len(i))
        n = 0

        for i in range(min_len):
            if o[i] == i[i]:
                n += 1
        if len(o) == 0:
            a = 0
        else:
            a = n / len(o)

        return a

    #####################
    import random
    def g():
        targrt = random.randint(1, 100)
        chances = 5

    while chances > 0:
        guess = int(input(f"剩余{change}次:"))

        if guess == target:
            print("ok")
            return
        elif guess < targrt:
            print("大了")
        else:
            print("小了")
        chances -= 1

    print(f" 机会用完啦！正确数字是 {target}")

    ################################

def sum_ (a, n):
    totle = 0
    current = 0
    for i in range(n):
        current = current * 10 +a
        totle = totle + current
    return totle

a = int(input())
n = int(input())

print(sum_(a, n))

#########################

def black_hole(num):
    while True:
        s = f"{num:04%}"

        digits = list(s)#变数列
        digits.sort()
        min_num = int("".join(digits))#数列变数

        digits.sort(reverse=True)
        max_num = int("".join(digits))

        nums =  max_num - min_num

        if nums == num:
            return num
#####################################

def find(seq):
    max_val = max(seq)
    min_val = min(seq)
    return max_val, min_val
