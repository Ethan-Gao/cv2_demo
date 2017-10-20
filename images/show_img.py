# coding:utf-8

import cv2

# 主函数
if __name__ == "__main__":
    img1 = cv2.imread('example.jpg', cv2.IMREAD_COLOR) # 原图
    img2 = cv2.imread('example.jpg', cv2.IMREAD_GRAYSCALE) # 灰度图
    cv2.imshow('example1', img1)
    cv2.imshow('example2', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
