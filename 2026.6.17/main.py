from cmobilephone import CMobilePhone
from cperson import CPerson

if __name__ == '__main__':
    phoneA = CMobilePhone(
        "小手机A",
        "Xiaomi 14",
        15.26,
        7.13,
        0.82,
        "小强",
        "13800138000",
        6.36,
        "2670x1200",
        "AMOLED",
        "小米",
        "Xiaomi 14"
    )

xiaoqiang = CPerson("张小强", 18, True, phoneA)
uncle = CPerson("王叔叔", 45, True, None)

print("\n")
xiaoqiang.callsomeone(uncle)
print("\n")
print("张小强把手机A送给王叔叔。")
uncle.set_phone(xiaoqiang.get_phone())
xiaoqiang.set_phone(None)
phoneA.set_user("王叔叔")

phoneB = CMobilePhone(
    "华为手机B",
    "Huawei Pura80",
    16.35,
    7.48,
    0.82,
    "张小强",
    "13900139000",
    6.7,
    "3200*1440",
    "OLED",
    "华为",
    "Huawei Pura80"
)

print("\n")
print("张小强新买了一个华为手机B。")
xiaoqiang.set_phone(phoneB)  # 张小强绑定手机B

print("\n")
xiaoqiang.callsomeone(uncle)
uncle.callsomeone(xiaoqiang)
