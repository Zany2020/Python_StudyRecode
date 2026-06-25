from cmobilephone import CMobilePhone
from gaming_phone import GamingPhone
from cperson import CPerson
from base_device import BaseDevice
from custom_exceptions import DeviceError

# 这里写测试代码、程序启动逻辑
if __name__ == "__main__":
    print("\n===== 1. 类方法：工厂创建手机 =====")
    phone1 = CMobilePhone.create_xiaomi14("alimakana", "13800138000")
    print(phone1)#__str__起作用

    print("\n===== 2. 子类：游戏手机 =====")
    phone2 = GamingPhone(
        brand="黑鲨", model="BlackShark 5 Pro",
        length=16.3, width=7.6, height=0.95,
        user="小明", number="13900139000",
        screen_size=6.67, resolution="2400x1080",
        screen_tech="LCD", screen_manu="天马",
        battery_cap=5000, _cooling_power=10
    )
    phone2.toggle_game_mode()
    phone2.show_info()

    print("\n===== 3. 类属性：统计设备总数 =====")
    print(f"当前设备总数：{BaseDevice.get_total_count()}")

    print("\n===== 4. 多态演示：统一调用show_info =====")
    devices = [phone1, phone2]
    for dev in devices:
        print("---")
        dev.show_info()

    print("\n===== 6. 静态方法：校验手机号 =====")
    try:
        CMobilePhone.validate_number("12345")
    except DeviceError as e:
        print("f{e}")

    print("\n===== 7. 魔法方法演示 =====")
    print(f"phone1 == phone2？ {phone1 == phone2}")
    print(f"phone1长度：{len(phone1)}")

    print("\n===== 8. 电量耗尽异常演示 =====")
    phone1.unlock()
    for i in range(20):
        try:
            phone1.call("王叔叔")
        except DeviceError as e:
            print(f"{i + 1} fail: {e}")
            break
