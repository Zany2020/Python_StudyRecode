from cmobilephone import CMobilePhone
from custom_exceptions import  PhoneLockedError

class GamingPhone(CMobilePhone):
    #只要子类自己写了 __init__，就是重写父类的构造函数。覆盖掉父类构造，程序只会执行你子类这个函数
    def __init__(self, brand: str, model: str, length: float, width: float, height: float,
            user: str, number: str, screen_size: float, resolution: str,
            screen_tech: str, screen_manu: str, battery_cap: int,
            cooling_power: int, game_mode: bool = False):

        # 调用父类构造，执行父类全部self.xx = xx
        super().__init__(brand, model, length, width, height, user, number,
                    screen_size, resolution, screen_tech, screen_manu, battery_cap)

        #这次重写时，目的是增加了子类专属的两个参数cooling_power, game_mode
        self.__current_level = 0
        self._game_mode = game_mode

        def toggle_game_mode(self):
            self._game_mode = not self._game_mode
            status = "open" if self._game_mode else "closed"
            print(f"{self.model} Game mode: {status}")

        def play_game(self, game_name: str):
            if self.is_locked():
                raise PhoneLockedError("手机已锁屏，无法玩游戏")

            consum = 15 if self._game_mode else 10
            self._batterty.consum(consum)#这是局部变量,同名没问题
            print(f"{self.user} 正在玩 {game_name}，散热功率 {self._cooling_power}W")

        def show_info(self):
            super().show_info()
            print(f"散热功率: {self._cooling_power}W")
            print(f"游戏模式: {'开启' if self._game_mode else '关闭'}")

#super().__init__()：调用父类构造函数,重写构造函数
#super().show_info()：调用父类普通业务方法



