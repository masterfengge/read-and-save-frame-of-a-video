import cv2
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"
#def getFrame(videoPath, svPath):

cap = cv2.VideoCapture(r"D:\视频图像采集\视频资料1102\视频分析采集\视频\220kV菊同甲线N12塔_设备_SEQNBR288_161102-15-20-09_161102-15-22-28\220kV菊同甲线N12塔_设备_SEQNBR288_161102-15-20-09_161102-15-22-28_0.mp4")
numFrame = 0
while True:
        if cap.grab():
            flag, frame = cap.retrieve()
            if not flag:
                continue
            else:
                # cv2.imshow('video', frame)
                numFrame += 300
                newPath = r"D:\视频图像采集\视频资料1102\视频分析采集\视频\220kV菊同甲线N12塔_设备_SEQNBR288_161102-15-20-09_161102-15-22-28\\" + str(numFrame) + ".jpg"
                cv2.imencode('.jpg', frame)[1].tofile(newPath)
        if cv2.waitKey(10) == 27:
            break
cap.release()
cv2.destroyAllWindows()

#getFrame(r"D:\视频图像采集\视频资料1102\视频分析采集\视频\220kV菊同甲线N12塔_设备_SEQNBR288_161102-15-20-09_161102-15-22-28\220kV菊同甲线N12塔_设备_SEQNBR288_161102-15-20-09_161102-15-22-28_0.mp4" , r"D:\视频图像采集\视频资料1102\视频分析采集\视频\220kV菊同甲线N12塔_设备_SEQNBR288_161102-15-20-09_161102-15-22-28")


