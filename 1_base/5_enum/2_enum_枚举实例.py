from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)

car_color = Color.RED
print(car_color.name)
print(car_color.value)
a=[]
a.append(Color.RED.value)
a.append(Color.GREEN.value)
print(a)
