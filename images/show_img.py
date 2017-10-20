# coding:utf-8

import cv2

# 主函数
if __name__ == "__main__":
    img = cv2.imread('example.jpg', cv2.IMREAD_COLOR) # 原图
    cv2.imshow('example', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
