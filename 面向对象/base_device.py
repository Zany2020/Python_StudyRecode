#抽象基类（接口规范）
#ABC = Abstract Base Class 抽象基类

from abc import ABC, abstractmethod
#abc：Python 自带的一个标准库模块,专门用来做抽象类、抽象方法。
class BaseDevice(ABC):
    total_device_count = 0
    def __init__ (self, brand: str, model: str):
        self.brand = brand
        self.model = model
        BaseDevice.total_device_count += 1

    @abstractmethod
    def show_info(self):
        pass

    @classmethod
    @abstractmethod
    def get_total_count(cls):
        return cls.total_device_count

    @staticmethod
    @abstractmethod
    def check_serial_number(serial: str):
        return len(serial) == 10 and serial.isdigit()

#抽象类 + 抽象方法（纯虚函数）:
#1.统一规范接口，强制所有子类一套标准行为,只要继承 BaseDevice，三个方法必须全部实现，少一个直接报错
#2.函数接收抽象父类，就能传任意子类对象(调用各自重写的show_info)
#  手机子类重写python运行class Phone(BaseDevice):
#     def show_info(self):
#         print(f"手机：{self.brand} {self.model}")
#  平板子类重写python运行class Pad(BaseDevice):
#     def show_info(self):
#         print(f"平板电脑｜品牌：{self.brand}，型号：{self.model}")





