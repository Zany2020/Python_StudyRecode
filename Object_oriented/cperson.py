from custom_exceptions import DeviceError, PhoneLockedError


class CPerson:
    def __init__(self, name: str, age: int, genter: bool, phone = None):
        self._name = name
        self._phone = phone
        self._age = age
        self._gender = genter

    def introduce(self):
        sex = "man" if self._gender else "woman"
        print(f"I am {self._name}, age is {self._age}, {sex}")

    def call_someone(self, target_name: str):
        if not self._phone:
            print(f"{self._name} has no phone number")
            return
        try:
            self._phone.unlock()
            self._phone.call(target_name)
        except PhoneLockedError as e:
            print(f"fail to call:{e}")

    def set_phone(self, new_phone):
        self._phone = new_phone
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get_gender(self):
        return self._gender


