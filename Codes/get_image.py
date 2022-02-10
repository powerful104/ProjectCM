import numpy as np
import cv2

"""
get_image 함수

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
    600* 600의 이미지 정보 (넘파이 배열)

기능 :
    위의 색과 아래의 색의 RGB 정보를 받아 600*600의 정사각형의 위, 아래로 절반씩 색이 나누어진 이미지를 생성하고 반환한다.
    위의 가로 600, 세로 300의 이미지는 위의 RGB 값으로, 아래의 가로 600, 세로 300의 이미지는 아래의 RGB 값으로 설정된 이미지를 반환한다.
"""

def get_image(up_color, down_color):
    img = np.zeros((600,600,3),dtype=np.uint8)
    for r in range(300):
        for c in range(600):
            img[r, c] = up_color
            img[r+300, c] = down_color
    return img

test_img = get_image((185, 117, 97), (178, 215, 224))
print(test_img.shape)
cv2.imshow('img',test_img)
cv2.waitKey()
cv2.destroyAllWindows()