# coding:utf-8

import cv2
import numpy as np

# 鼠标回调函数
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

if __name__ == "__main__":
    # 列出所有事件
    events = [ i for i in dir(cv2) if 'EVENT' in i ]
    # 创建图像和窗口
    img = np.zeros((512,512,3),np.uint8)
    cv2.namedWindow('image')
    # 注册回调
    cv2.setMouseCallback('image',draw_circle)
    # 循环检查鼠标
    while True:
        cv2.imshow('image',img)
        if ( cv2.waitKey(20) & 0xff ) == 27:
            break;
    # 释放资源
    cv2.destroyAllWindows()
