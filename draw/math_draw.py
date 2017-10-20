# coding: utf-8

import cv2
import numpy as np

if __name__ == "__main__":
    # 创建一张黑色图像
    img = np.zeros((512,512,3),np.uint8)
    # 画一条5px的线
    cv2.line(img,(0,0),(511,511),(255,0,0),5)
    # 画矩形
    cv2.rectangle(img,(384,0),(510,128),(0,250,0),3)
    # 画圆
    cv2.circle(img,(447,63),63,(0,0,255),-1)
    # 画椭圆
    cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
    # 画多边形
    pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.polylines(img,[pts],True,(0,255,255))
    # 画文字
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2,cv2.LINE_AA)
    # 显示图片
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()