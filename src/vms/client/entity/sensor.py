import math
import random


class Sensor:
    _value: float
    name: str
    type: str

    my_day = 311

    def __init__(self, name):
        self.name = name

    def generate_new_value(self):
        pass

    def get_data(self):
        return self._value

    def __str__(self):
        return str({"type": self.type, "name": self.name, "value": self.get_data()})


class Temperature(Sensor):

    def __init__(self, name):
        super().__init__(name)
        self.type = "temperature"

    def generate_new_value(self):
        self._value = random.random() * 10 + self.my_day/100


class Current(Sensor):

    def __init__(self, name):
        super().__init__(name)
        self.type = "current"

    def generate_new_value(self):
        self._value = math.sin(self.my_day/100) * 20
        self.my_day = self.my_day + 15


class Noise(Sensor):

    def __init__(self, name):
        super().__init__(name)
        self.type = "noise"

    def generate_new_value(self):
        self._value = random.random() + self.my_day/100


class Humidity(Sensor):

    def __init__(self, name):
        super().__init__(name)
        self.type = "humidity"

    def generate_new_value(self):
        self._value = random.random() * 10 + self.my_day/50
