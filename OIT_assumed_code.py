#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import rospy
from std_msgs.msg import Empty, String
import read_qr_camera

# OITのコードを想定したコード (OITのコードがFlexBeで実装されている場合は不要)
class Task_1():

    def __init__(self):
        self.pub_next_state = rospy.Publisher("/task_2", Empty, queue_size=10)  #Task2に遷移するためにセット
        self.pub_target_object = rospy.Publisher("/target_object", String, queue_size=10)
        self.next_state = Empty()



if __name__=='__main__':
    task1 = Task_1()
    rospy.init_node('move')
    read_qr = read_qr_camera.ReadQR()
    object_word = read_qr.processing_qr()
    task1.base_time = rospy.Time.now().to_sec()  #初期時刻(s)のセット

    #10分(600s)になるまでタスクを行う
    while rospy.Time.now().to_sec() - task1.base_time < 10:
        rospy.loginfo("Executing Task1....")

    #10分経過すると、次のTask2のコードに向けてメッセージをパブリッシュする
    rospy.loginfo("Finish Task 1")
    print(type(object_word), object_word)
    rospy.loginfo("Target Object:{}".format(object_word))
    task1.pub_target_object.publish(object_word)
    task1.pub_next_state.publish(task1.next_state)
    sleep(1)
    rospy.signal_shutdown("Complete Task1")
