from abc import ABC

from base_device import BaseDevice
from cscreen import CScreen
from cbattery import CBattery
from custom_exceptions import PhoneLockedError, InvalidPhoneNumberError
import re
# 严格格式校验就用import re

class CMobilePhone(BaseDevice, ABC):
    def __init__(self, brand: str, model: str, length: float, width: float, height: float,
            user: str, number: str, screen_size: float, resolution: str,
            screen_tech: str, screen_manu: str, battery_cap: int):
        super().__init__(brand, model)
        self._length = length
        self._width = width
        self._height = height
        self._user = user
        self._number = number
        self._is_locked = True

        self._screen = CScreen(screen_size, resolution, screen_tech, screen_manu, model)
        self._battery = CBattery(battery_cap)

    #只读
    # @property
    # def model(self):
    #     return self._model

    @property
    def user(self):
        return self._user
    @user.setter
    def user(self, new_user: str):
        if not new_user.strip():
            # not "" 结果为 True
            # 字符串.strip()：删掉字符串首尾所有空白字符
            raise ValueError("用户名不能为空")  # 内置,表示-类型没错，但内容不对
        self._user = new_user

    @property
    def is_locked(self):
        return self._is_locked

    def show_info(self):
        """重写父类抽象方法，展示手机完整信息"""
        print(f"品牌: {self.brand}")
        print(f"型号: {self.model}")
        print(f"尺寸: {self._length} x {self._width} x {self._height} cm")
        print(f"机主: {self._user}")
        print(f"号码: {self._number}")
        self._screen.show_screen_info()
        self._battery.show_battery_level()
        print(f"状态: {'已锁屏' if self._is_locked else '已解锁'}")

    def power_on(self):
        self._is_locked = True
        print(f"{self._brand} {self._model} 已开机，默认锁屏")

    def unlock(self):
        self._is_locked = False
        print(f"{self.model} 已解锁")

    def lock(self):
        self._is_locked = True
        print(f"{self._model} 已锁屏")

    def call (self, target_name: str):
        if self.is_locked:
            raise PhoneLockedError("手机已锁屏，请先解锁再打电话")
        self._battery.consume(5)
        print(f"{self._user} 正在给 {target_name} 打电话...")

    #只是一个工具计算、格式校验、转换、判断就用静态方法@staticmethod
    @staticmethod
    def validate_number(number: str) -> bool:
        if not re.match(r"^[1-9]\d*$", number):
            raise InvalidPhoneNumberError("手机号必须是11位有效号码")
        return True


    #1-操作、修改类的共享变量
    #2-提供多种创建对象的方式
    @classmethod
    def create_xiaomi14(cls, user: str, number: str):
        #cls必带，cls(参数列表) 等价于 CMobilePhone(参数列表)
        #cls(参数) 等价于 类(参数)的时候，调用__init__，这就是为什么结束后回到上面的__init__
        return cls(
            brand="Xiaomi",
            model="Xiaomi14",
            length=15.26, width=7.13, height=0.82,
            user=user, number=number,
            screen_size=6.36, resolution="2670x1200",
            screen_tech="AMOLED", screen_manu="三星",
            battery_cap=4610
            )

    # ========== 补充实现 BaseDevice 的抽象方法 ==========
    # #
    # @classmethod
    # def get_total_count(cls):
    #     """实现父类抽象类方法：返回设备总数"""
    #     return cls.total_device_count
    #
    # @staticmethod
    # def check_serial_number(serial: str):
    #     """实现父类抽象静态方法：校验序列号"""
    #     return len(serial) == 10 and serial.isdigit()
    #====================================================

    def __str__(self):
        return f"手机[{self.brand} {self.model}, 机主：{self._user}]"
    def __eq__(self, other):
        if not isinstance(other, CMobilePhone):
            return False
        return self.brand == other.brand and self.model == other.model
        #base_device.py：里定义的
    def __len__(self):
        return int(self._length)#必须返回整数
    def __del__(self):
        #析构函数，对象销毁时自动调用
        print(f"【销毁】 {self.brand} {self.model} 设备已回收")
        BaseDevice.total_device_count -= 1














