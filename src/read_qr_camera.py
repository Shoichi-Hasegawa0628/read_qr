#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ROSのTopic経由でQRコードを読み取るプログラム

from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
import cv2
import rospy
import numpy as np
import time
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class ReadQR():

    def __init__(self):
        rospy.Subscriber('/hsrb/head_rgbd_sensor/rgb/image_raw', Image, self.image_callback, queue_size=10)
        self.image = 0
        self.cv_bridge = CvBridge()
        time.sleep(1)
        self.processing_qr()


    def processing_qr(self):
        while self.image == 0:
            rospy.loginfo("waiting...")
            continue

        num0 = 0
        while num0 == 0:
            img = self.rgb_image_ros_to_opencv(self.image)
            gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            image = self.edit_contrast(gray_scale, 5)
            codes = decode(image)
            if len(codes) > 0:
                input = codes[0][0].decode('utf-8', 'ignore')
                num0 = input
                print(num0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, str(input), (10,300), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
            
            #time.sleep(0.1)
        cv2.imshow('frame',img)
        cv2.waitKey(0)
        rospy.loginfo("finished")
    

    def image_callback(self, img):
        self.image = img


    def rgb_image_ros_to_opencv(self, img):
        try:
            object_image = img
            object_image = self.cv_bridge.imgmsg_to_cv2(object_image, 'passthrough')
        except CvBridgeError as e:
            rospy.logerr(e)

        object_image = cv2.cvtColor(object_image, cv2.COLOR_BGR2RGB)
        return object_image


    def edit_contrast(self, image, gamma):
        """コントラスト調整"""
        look_up_table = [np.uint8(255.0 / (1 + np.exp(-gamma * (i - 128.) / 255.)))
            for i in range(256)]
        result_image = np.array([look_up_table[value]
                                for value in image.flat], dtype=np.uint8)
        result_image = result_image.reshape(image.shape)
        return result_image


if __name__ == "__main__":
    rospy.init_node('read_qr')
    node = ReadQR()
    rospy.spin()
