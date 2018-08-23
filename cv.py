# created by Huang Lu
# 27/08/2016 17:05:45
# Department of EE, Tsinghua Univ.

import os
import cv2
import time
import argparse
import numpy as np
import tensorflow as tf

from queue import Queue
from threading import Thread
'''from utils.app_utils import FPS, WebcamVideoStream, draw_boxes_and_labels
from object_detection.utils import label_map_util
#cap=cv2.VideoCapture("F:/a.mp4")'''
cap = cv2.VideoCapture(r"D:\视频图像采集\视频资料1102\视频分析采集\视频\220kV菊同甲线N12塔_设备_SEQNBR288_161102-15-20-09_161102-15-22-28\220kV菊同甲线N12塔_设备_SEQNBR288_161102-15-20-09_161102-15-22-28_0.mp4")
c=1
if cap.isOpened():
    print(11)
    rval, frame=cap.read()
else:
    rval=False
timeF=15
while(1):
    rval,frame=cap.read()
    if(c%timeF==0):
        cv2.imwrite('D:\\img\\'+str(c)+'.jpg',frame)
        c=c+1
        time.sleep(1)
cap.release()
