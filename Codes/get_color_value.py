import random

def get_color_value():
    up_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    down_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return up_color, down_color

a, b = get_color_value()
print(a,b)

"""
튜플은 B, G, R의 형태로 나타낸다.
"""