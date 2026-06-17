class CScreen:
#float 只是注释提示,需要手动判断校验
#self必须是第一个参数，代表当前实例对象本身,
#等价 C++ 的隐式 this 指针,访问成员必须加 self.变量名，不加就是局部变量
    def __init__(self, s: float, res: str, tech_type: str, manufacturer: str, match_model: str):
        #私有属性
        self._size = str(s)
        self._resolution = res
        self._tech_type = tech_type
        self._match_model = match_model
        self._manufacturer = manufacturer

    def show_screen_info(self):
        print(f"屏幕尺寸:{self._size}英寸")
        print(f"分辨率: {self._resolution} 像素")
        print(f"屏幕技术: {self._tech_type}")
        print(f"制造商: {self._manufacturer}")

    def is_compatible_with_phone(self, phone):
        #self：固定第一位，调用时 Python 自动塞进来,不用管
        #phone：第二个自定义形参，手动传入的对象
        if not phone:
            return False
        #return phone.get_model() == self._match_model
        return phone.model == self._match_model

    def get_match_model(self):
        return self._match_model


