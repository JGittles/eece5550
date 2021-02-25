#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import random

class TurtleBot:

    def __init__(self):
        rospy.init_node('turtlebot_controller' , anonymous = True)

        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)

        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)

        self.pose = Pose()
        self.rate = rospy.Rate(1)

    def update_pose(self, data):

        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)
        

    def random_move(self):

        vel_msg = Twist()

        while True:

            vel_msg.linear.x = round(random.uniform(-1, 1), 4)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = round(random.uniform(-1, 1), 4)

            self.velocity_publisher.publish(vel_msg)

            self.rate.sleep()
            #I put the print statement after sleep because I wanted to see new turtle location at its "pivot" point
            print("x: "+ str(self.pose.x) +"y: " + str(self.pose.y))

        rospy.spin()

if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.random_move()
    except rospy.ROSInterruptException:
        pass