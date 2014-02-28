#!/usr/bin/env python
import pygame
import curses
import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy


from geometry_msgs.msg import Twist

import sys, select, termios, tty
pygame.init()

pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

msg = """
Reading from the joystick!
"""

def getAxis():
    pygame.event.pump()
    left = joystick.get_axis(1)
    right = joystick.get_axis(3)
    #print (left,right)
    return (left,right)

speed = 10
turn = 5

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    stdscr=curses.initscr()
    stdscr.keypad(1)
    stdscr.nodelay(1)
    stdscr.leaveok(1)

    settings = termios.tcgetattr(sys.stdin)

    pub = rospy.Publisher('cmd_vel', Twist)
    rospy.init_node('teleop_twist_joystick')

    x = 0
    th = 0
    status = 0

    try:
        print msg
        print vels(speed,turn)
        while(1):
            if stdscr.getch()==ord('q'):
                break
            joy = getAxis()
            x = -1 * joy[0]
            th = joy[1]
            twist = Twist()
            twist.linear.x = x*speed; twist.linear.y = 0; twist.linear.z = 0
            twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = th*turn
            pub.publish(twist)
        stdscr.keypad(0)
    except:
        print e

    finally:
       twist = Twist()
       twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
       twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
       pub.publish(twist)

       termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)