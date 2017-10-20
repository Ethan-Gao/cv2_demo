# coding: utf-8

import cv2

# 主函数
if __name__ == "__main__":
    img1 = cv2.imread('example.jpg', cv2.IMREAD_COLOR)      # 彩图
    img2 = cv2.imread('example.jpg', cv2.IMREAD_GRAYSCALE)  # 灰图
#   if img1 == None or img2 == None:
#   https://stackoverflow.com/questions/23628325/cv2-imread-checking-if-image-is-being-read
#   http://blog.csdn.net/imzoer/article/details/8637408
#   ==检查value,is检查id
    if img1 is None or img2 is None:
        print 'imread error'
        exit()
    cv2.imshow('example1', img1)
    cv2.imshow('example2', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
