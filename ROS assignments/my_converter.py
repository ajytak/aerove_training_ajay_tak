#!/usr/bin/env python

import rospy
import math
from beginner_tutorials.msg import Quaternions
from beginner_tutorials.msg import Euler

def callback(data):
    a = data.x
    b = data.y
    c = data.z
    d = data.w
    rospy.loginfo('I heard %f', a)
    t0 = +2.0 * (d * a + b * c)
    t1 = +1.0 - 2.0 * (a * a + b * b)
    angle.roll = math.atan2(t0, t1)
    t2 = +2.0 * (d * b - c * a)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    angle.pitch = math.asin(t2)
    t3 = +2.0 * (d * c + a * b)
    t4 = +1.0 - 2.0 * (b * b + c * c)
    angle.yaw = math.atan2(t3, t4)
    rospy.loginfo(angle)
    pub.publish(angle)
    

rospy.init_node('my_converter', anonymous=True)
angle = Euler()
rospy.Subscriber('topic1', Quaternions, callback)
pub = rospy.Publisher('topic2', Euler, queue_size=10)


rospy.spin()

