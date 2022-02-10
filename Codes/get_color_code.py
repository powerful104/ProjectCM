"""
get_color_code 함수

매개변수 :
    (up_B, up_G, up_R)의 튜플
        up_B : 위의 색의 Blue 밝기 정수 값 (0~255)의 범위를 가진다.
        up_G : 위의 색의 Green 밝기 정수 값 (0~255)의 범위를 가진다.
        up_R : 위의 색의 Red 밝기 정수 값 (0~255)의 범위를 가진다.
    (down_B, down_G, down_R)의 튜플
        down_B : 아래의 색의 Blue 밝기 정수 값 (0~255)의 범위를 가진다.
        down_G : 아래의 색의 Green 밝기 정수 값 (0~255)의 범위를 가진다.
        down_R : 아래의 색의 Red 밝기 정수 값 (0~255)의 범위를 가진다.

반환값 :
    위의 색정보를 가진 6글자의 문자열
    아래의 색정보를 가진 6글자의 문자열

기능 :
    (0~255)의 범위를 가지는 색 정보들을 16진법으로 변환하여 위의 색정보, 아래의 색정보를 16진법의 형태를 갖는 문자열의 형태로 반환한다.
"""

def get_color_code(up_color, down_color):
    up_code=""
    down_code=""
    for i in range(3):
        up_code = '{0:0>2}'.format(hex(up_color[i])[2:]) + up_code
        down_code = '{0:0>2}'.format(hex(down_color[i])[2:]) + down_code
    return up_code.upper(), down_code.upper()
