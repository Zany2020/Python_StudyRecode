from custom_exceptions import BatteryLowError
class CBattery:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__current_level = 100

    #后面可写对应的 .setter
    #如果只写property没写setter那就是起只读作用，不能修改变量
    @property
    def current_level(self):
        return self.__current_level

    def consume(self, percent: int):
        self.__current_level = max(0, self.__current_level - percent)
        if  self.__current_level <= 0:
            raise BatteryLowError

    def charge(self, percent: int):
        self.__current_level = min(100, self.__current_level + percent)

    def show_battery_level(self):
        print(f"电池容量: {self.__capacity}mAh，当前电量: {self.__current_level}%")

    def __str__(self):
        return f"电池[{self.__capacity}mAh, 剩余{self.__current_level}%]"

