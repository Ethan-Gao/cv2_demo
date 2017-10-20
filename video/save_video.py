# coding: utf-8

import cv2

# 主函数
if __name__ == "__main__":
    # 打开视频
    cap = cv2.VideoCapture('example.avi')
    # 创建写入器
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    writer = cv2.VideoWriter('example_new.avi',fourcc,20,(640,480),isColor = 0)
    # 判断是否成功
    while cap.isOpened():
        # 一帧一帧读取
        ret, frame = cap.read()
        if ret:
            # 处理图像
            frame = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
            # 写入新文件
            writer.write(frame);
            # 显示图像
            cv2.imshow('frame',frame)
            # 判断退出
            if ( cv2.waitKey(1) & 0xff ) == ord('q'):
                break
        else:
            break

    #释放资源
    cap.release()
    cv2.destroyAllWindows()
