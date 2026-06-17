class CPerson:
    def __init__(self, name: str, age: int, gender: bool, phone= None) :
        self._name = name
        self._age = age
        self._gender = gender
        self._phone = phone

    def whoareyou(self):
        gender_str = "man" if self._gender else "woman"
        print(f"I'm {self._name}, {self._age}age, sex is {gender_str}")

    def callsomeone(self, person):
        target_name = person.get_name() if person else "unknown"
        print(f"{self._name} is calling {target_name}")

        if not self._phone:
            print(f"{self._name} has no phone")
            return

        self._phone.call(person)

    def get_name(self):
        return self._name
    def get_phone(self):
        return self._phone
    def set_phone(self, new_phone):
        self._phone = new_phone


