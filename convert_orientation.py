#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import tf

roll = math.radians(30)
pitch = math.radians(42)
yaw = math.radians(58)

print("roll = ", math.degrees(roll), "pitch = ",
      math.degrees(pitch), "yaw = ", math.degrees(yaw))

quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
for item in quaternion:
    print(item)

rpy = tf.transformations.euler_from_quaternion(quaternion)
roll_from_quaternion = rpy[0]
pitch_from_quaternion = rpy[1]
yaw_from_quaternion = rpy[2]

print("roll = ", math.degrees(roll_from_quaternion))
print("pitch = ", math.degrees(pitch_from_quaternion))
print("yaw = ", math.degrees(yaw_from_quaternion))
