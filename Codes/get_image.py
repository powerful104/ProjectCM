import numpy as np
import cv2

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