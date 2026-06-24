#自定义异常

class DeviceError(Exception): #Python内置标准异常父类
    pass

class BatteryLowError(DeviceError):
    def __init__(self, current_battery):
        self.current_battery = current_battery
        super().__init__(f"Battery is low, only {current_battery}%")#只是存着，不会自己输出到控制台。
        #super：调用父类的方法（这里super().__init__() 意思调用父类 DeviceError 的构造函数）
        #继承链：BatteryLowError → DeviceError → Exception

# 自定义异常类,
#到时候# 抛出异常，括号里写文字如raise PhoneLockedError("手机已锁定，无法操作")
class PhoneLockedError(DeviceError):
    pass
class InvalidPhoneNumberError(DeviceError):
    pass
