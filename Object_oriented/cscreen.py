class CScreen:
    def __init__(self,size: float, resolution: str, tech: str, manufacturer: str, match_model):
        self.__size = str(size)#双下划线:Python会自动改名，外部无法直接访问(隐藏内部成员,和private一样）
        self.__resolution = str(resolution)
        self.__tech_type = str(tech)
        self.__manufacturer = str(manufacturer)
        self.__match_model = str(match_model)

    @property
    def resolution(self):
        return self.__resolution

    @resolution.setter#后缀 .setter 代表这是赋值专用方法
    def resolution(self, value: str):
        if not value or "x" not in value and "*" not in value:#and两个同时成立才为真
            raise ValueError("resolution must be x or *")
        self.__resolution = value

    @property
    def match_model(self):
        return self.__match_model

    def show_screen_info(self):
        print(f"屏幕尺寸{self.__size}")
        print(f"分辨率: {self.__resolution}")
        print(f"屏幕技术: {self.__tech_type}")
        print(f"制造商: {self.__manufacturer}")

    def is_compatible(self, phone_model: str) -> bool:
        return self.__match_model == phone_model
        # ==判断左右两边字符串完全一模一样,本身就会产出 True / False
    #字符串自带底层实现好的 __eq__

    def __eq__(self, other):
        #__eq__ 重载 == 等于运算符方法(用自己自定义的规则判断相等)
        #没写__eq__就是比较地址（除了字符串）
        if not isinstance(other, CScreen):
            #isinstance判断一个对象是不是某个类型
            return False
        return (self.__size == other.__size
                and self.__resolution == other.__resolution
                and self.__tech_type == other.__tech_type)#所有都相等才返回true


    def __str__(self):
        return f"屏幕{self.__size}英寸，{self.__resolution},{self.__tech_type}"
        #强制语法规则：必须 return 一段字符串
    #手动调用如screen.show_screen_info()就不用定义__str__
    #print(screen)这种会自动调用__str__ 要去定义
    #例如screen = CScreen(...)
        #print(screen)        # 自动调用
        #text = str(screen)   # 自动调用
        #print(f"设备：{screen}") # 自动调用


