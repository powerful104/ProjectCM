def get_color_code(up_color, down_color):
    up_code=""
    down_code=""
    for i in range(3):
        up_code = hex(up_color[i])[2:]+ up_code
        down_code = hex(down_color[i])[2:] + down_code
    return up_code, down_code

u, d = get_color_code((185, 117, 97), (178, 215, 224))
print(u, d)

"""
BGR 순의 튜플을 두개 입력받아 RGB 순의 문자열로 출력
"""