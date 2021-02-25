#!/usr/bin/env python

#By Jordan Gittleman - Assignment 1 - EECE5550 - Fall 2020 - Please enjoy! =) 

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import random
from math import cos, pi, sin, sqrt, atan2, tanh
from turtlesim.srv import TeleportAbsolute, SetPen, Spawn
import time

class TurtleBot:

    def __init__(self):
        rospy.init_node('turtlebot_controller' , anonymous = True)
        #initializing the turtle class, getting names from the launch file and making the corresponding publisher/subscriber
        self.turtle = rospy.get_param('~turtle')

        self.init_pose = Pose()
        self.init_pose.x = rospy.get_param('~pose_x')
        self.init_pose.y = rospy.get_param('~pose_y')
        self.init_pose.theta = rospy.get_param('~pose_theta')



        self.velocity_publisher = rospy.Publisher("/"+str(self.turtle)+"/cmd_vel", Twist, queue_size=1)

        self.pose_subscriber = rospy.Subscriber("/"+str(self.turtle)+"/pose", Pose, self.update_pose)

        self.pose = Pose()

        #the spawn function will call the teleport function if the turtle does not exist
        self.spawn()
                

    def teleport(self):
        #the teleport function takes pose data from the launch file and also removes the pen so it doesnt leave a line when the turtle is teleported
        rospy.wait_for_service('/'+str(self.turtle)+'/teleport_absolute')
        self.line_color_client(1,False)
        try:
            teleport_absolute = rospy.ServiceProxy('/'+str(self.turtle)+'/teleport_absolute',TeleportAbsolute)
            teleport_absolute(self.init_pose.x, self.init_pose.y, self.init_pose.theta)  
        except rospy.ServiceException,e:
            print "Service call failed: %s" %e
    
    def spawn(self):
        #spawn attempts to spawn in a turtle at th launch file's designated pose, if it runs into an error (like the turtle name exists already) it will call the teleport function instead
        #this was the best way I was able to implement checking for if a node was already open in this particular problem
        rospy.wait_for_service('/spawn')
        try:
            spawn_absolute = rospy.ServiceProxy('/spawn',Spawn)
            spawn_absolute(self.init_pose.x, self.init_pose.y, self.init_pose.theta, self.turtle)  
        except rospy.ServiceException,e:
            self.teleport()

    def update_pose(self, data):
        #takes pose data from the turtle/pose topic
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)
        #this part, along with the additional math in the steering angle function serves to work around how the tan2 comand works, in this case, the objective is to remove redundant "rotations" of the absolute pose direction
        if(self.pose.theta < 0):
            self.pose.theta = self.pose.theta + 6.28

    def linear_vel(self, goal_pose, constant=3.5):
        # takes the difference between the current pose and desired location by calling the euclidean distance function and multiplies by a set constant for x velocity
        vel = constant * self.euclidean_distance(goal_pose)
        #this was added in order to ensure velocity never goes over 5 per the assignment instructions, ultimately, this is still throttled by dt when the turtle is very close to the trajectory
        #but this will play an important role if the turtle starts very far away
        if vel < 5:
         return vel

        else:
            return 5

    def steering_angle(self, goal_pose):
        #steering angle takes the atan(dy/dx) and atan2 specifically takes the signs of the values into account. this gives the angle of the ray from the turtle to the desired waypoint 
        steering_rad = atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)
        #this keeps theta within a positive 0-pi axis
        if steering_rad < 0:
            return steering_rad + 6.28
        return steering_rad

    def angular_vel(self, goal_pose, constant=6):
        #sets angular velocity by finding the delta between the ray of the steering angle and the ray of the current turtle heading/theta
        ccw_steering = self.steering_angle(goal_pose)
        ccw_pose_theta = self.pose.theta
        #below ensures atan2 does not flip from positive to negative values trying to equal the same point in the grid. (ie: if atan2 eq from steering angle func returns -270,
        #we would want 90 instead) this stops a massive delta from occuring which causes the turtle to suddenly have massive angular velocity for 1 timestep and overshoot its correction and do a loop-d-loop
        if ccw_pose_theta < 0:
            ccw_pose_theta = (ccw_pose_theta + 3.14)

     

        vel = (ccw_steering - ccw_pose_theta)
        if vel > 3.14:
            vel = vel - 6.28
        elif vel < -3.14:
            vel = vel + 6.28
        return vel * constant


    def euclidean_distance(self, goal_pose):
            #Euclidean distance between current pose and trajectory waypoint
            return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                        pow((goal_pose.y - self.pose.y), 2))
        
    def line_color_client(self, ep, switch):
        #line color parameters of turtle, based on euclidean distance, the farther the turtle from it's goal pose, 
        # we want it to be pure red when the turtle is far and white when it is exactly following
        color = 225-(225*tanh((5*ep)/(11*sqrt(2))))
        
        rospy.wait_for_service("/"+str(self.turtle)+"/set_pen")
        if switch == True:
            try:
                color_change = rospy.ServiceProxy("/"+str(self.turtle)+"/set_pen",SetPen)
                color_change(225,color,color,5,0)
                print("color: "+" r: "+str(225)+" g: "+str(color)+ " b: "+ str(color))

            except:
                print("service call failed =(")
        
        else:
            try:
                color_change = rospy.ServiceProxy("/"+str(self.turtle)+"/set_pen",SetPen)
                color_change(0,0,0,0,1)
                

            except:
                print("service call failed =(")            



    def traj_track(self):
        #tracker function, responsible for commanding turtle movement to follow trajectory
        vel_msg = Twist()
        goal_pose = Pose()


        #settng variables
        trajectory_description = rospy.get_param('~trajectory_description')
        xd = trajectory_description.get("xd")
        yd = trajectory_description.get("yd")
        repeat = trajectory_description.get("repeat")
        timestep = trajectory_description.get("timestep")
        counter=0
       #main loop, dependant on how many repeats of the trajectory are specified in the yaml file
        for i in range(repeat):
            #secondary loop, controls turtle movement at each timestep
            while counter in range(len(xd)):

                print(str(self.turtle+ " reporting for duty! Here's my stats:"))
                self.line_color_client(self.euclidean_distance(goal_pose),True)
                goal_pose.x=xd[counter]
                goal_pose.y=yd[counter]

            #setting angular v and linear v to goal pose
                vel_msg.linear.x = self.linear_vel(goal_pose)
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0

                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = self.angular_vel(goal_pose)


                

                #publishing new velocity data to vel_msg topic
                self.velocity_publisher.publish(vel_msg)


                #troubleshooting prints, these where necessary to understand why earlier control iterations made the turtle loop-d-loop
                print("x: "+ str(self.pose.x) +" y: " + str(self.pose.y)+" theta: "+str(self.pose.theta))
                print("linear v: "+ str(vel_msg.linear.x)+" angular v: "+ str(vel_msg.angular.z))
                print("goal x: "+str(goal_pose.x)+" goal y: "+ str(goal_pose.y)+" steering angle: "+str(self.steering_angle(goal_pose)))
                if goal_pose.x == 3 and goal_pose.y == 3:
                    print("******")
                    print("I'm at a corner!")
                    print("******")
                if goal_pose.x == 5.5 and goal_pose.y == 8:
                    print("******")
                    print("I'm at a corner!")
                    print("******")                
                if goal_pose.x == 8 and goal_pose.y == 3:
                    print("******")
                    print("I'm at a corner!")
                    print("******")
                print("-------")
                time.sleep(timestep) #sleep for the timestep
                counter = 1 + counter
                
            
            

            counter = 0

        
        #command turtle to stop after all loops have been performed
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
       
        #keeps function open until closed manually
        rospy.spin()
#main function call
if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.traj_track()
    except rospy.ROSInterruptException:
        pass