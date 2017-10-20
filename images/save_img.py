# coding: utf-8

import numpy as np
import cv2

# 主函数
if __name__ == "__main__":
    img = cv2.imread('example.jpg',0)
    cv2.imshow('example',img)
    k = cv2.waitKey(0)
    if k == 27: # ESC退出
        cv2.destroyAllWindows()
    elif k == ord('s'): # s保存
        cv2.imwrite('example_new.jpg',img)
        cv2.destroyAllWindows()
