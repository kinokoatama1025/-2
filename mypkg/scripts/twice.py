#!/usr/bin/env python
#-*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Int32

def cd(message):
    if message.data == 0:
        print('　')
    elif message.data == 1:
        print('上') 
    elif message.data == 2:
        print('田')
    elif message.data == 3:
        print('お')
    elif message.data == 4:
        print('兄')
    elif message.data == 5:
        print('ち')
    elif message.data == 6:
        print('ゃ')
    elif message.data == 7:
        print('ん')
    elif message.data == 8:
        print('大')
    elif message.data == 9:
        print('好')
    elif message.data == 10:
        print('き')
    elif message.data == 11:
        print('♡')
 
  # rospy.loginfo(message.data)

if __name__=='__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cd)
    rospy.spin()

