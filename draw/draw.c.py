# coding: utf-8

import cv2
from matplotlib import pyplot as plt

# 主函数
if __name__ == "__main__":
    img = cv2.imread('example.jpg',0)
    plt.imshow(img,cmap='gray')
#    plt.xticks([]),plt.yticks([])   # 隐藏坐标
    plt.show()
