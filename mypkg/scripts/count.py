#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import Int32

if __name__=='__main__':
    rospy.init_node('count')
    pub = rospy.Publisher('count_up',Int32,queue_size=1)
   #rate = rospy.Rate(1)
    n=0
    while not rospy.is_shutdown():
        for n in range(12):
            pub.publish(n)
            print(n)
            time.sleep(1)
       #rate.sleep()

