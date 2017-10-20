# coding:utf-8

import cv2

# 主函数
if __name__ == "__main__":
    # 打开视频
    cap = cv2.VideoCapture('example.avi')
    # 捕捉视频
    while True:
        # 一帧一帧读取
        ret, frame = cap.read()
        if ret:
            # 处理图像
            gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
            # 显示图像
            cv2.imshow('frame',gray)
            # 判断退出
            if ( cv2.waitKey(1) & 0xff ) == ord('q'):
                break
        else:
            break

    #释放资源
    cap.release()
    cv2.destroyAllWindows()
