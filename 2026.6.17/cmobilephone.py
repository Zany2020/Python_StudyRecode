from cscreen import CScreen #导入屏幕类（替代C++的#include "CScreen.h"）
class CMobilePhone:
    def __init__(self, name: str, model: str, length: float, width: float, height: float,
    user: str, number: str, s: float, res: str, tech: str, manu: str, model_match: str):
        self._name = name
        self._model = model
        self._length = length
        self._width = width
        self._height = height
        self._user = user
        self._number = number
        self._screen = CScreen(s, res, tech, manu, model_match)

    # ---- 模拟C++的const属性：只读get方法 ----
    @property  #作用：把一个实例方法伪装成对象属性,py特有固定语法标记
    def model(self):
        return self._model
    @property
    def length(self):
        return self._length
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height

    # ---- 普通get/set方法 ----
    def get_name(self):
        return self._name
    def get_user(self):
        return self._user
    def set_user(self, new_user: str):
        self._user = new_user
    def get_model(self):
        return self._model

    # ---- 业务方法 ----
    def show_screen(self):
        print(f"手机名称: {self._name}")
        print(f"型号: {self._model}")
        print(f"尺寸: {self._length} x {self._width} x {self._height}")
        print(f"用户: {self._user}")
        print(f"号码: {self._number}")
        self._screen.show_screen_info()

    def call(self, person):
        if not person:
            print(f"fail to call")
            return
        if not person.get_name():
            print(f"no name")
            return
        print(f"{self._user} is using {self._name} to call {person.get_name()}")



























