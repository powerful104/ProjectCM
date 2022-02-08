import random

def get_color_value():
    up_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    down_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return up_color, down_color

a, b = get_color_value()
print(a,b)