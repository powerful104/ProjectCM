import random

"""
get_color_value 함수

매개변수 :

반환값 :
    색 정보를 가진 (0~255)범위의 세개의 정수값이 담긴 두개의 튜플 (튜플은 B, G, R의 형태로 나타낸다.)

기능 :
    gen_image 함수에서 사용될 랜덤한 RGB 정보가 담긴 튜플 두개를 반환한다.
"""

def get_color_value():
    up_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    down_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return up_color, down_color

a, b = get_color_value()
print(a,b)