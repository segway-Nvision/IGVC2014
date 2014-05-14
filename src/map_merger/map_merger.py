#!/usr/bin/env python
import math
import rospy
import tf
from tf.transformations import euler_from_quaternion
from tf.transformations import quaternion_from_euler
import tf.msg
import geometry_msgs.msg
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Image
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import MapMetaData
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion
from frame_grabber_node.msg import ImageWithTransform
from vision_control.msg import detectedvision

image_resolution = 0 #??????????!!!!!!!!?!?!?!?!?!?!?!?!?!?!

def callback_laser_map(msg_in):
    global pub_merged_map
    global image_map
    global Resolution
    global Height
    global Width
    global Origin
    global origin_angles
    global initialized

    if(not initialized):
        rospy.Subscriber("/flags_and_lanes", detectedvision, callback_image_map)
        initialized = True
        Width = msg_in.info.width
        Height = msg_in.info.height
        Resolution = msg_in.info.resolution
        Origin = msg_in.info.origin
        origin_quat = [Origin.orientation.x,
                      Origin.orientation.y,
                      Origin.orientation.z,
                      Origin.orientation.w]
        origin_angles = euler_from_quaternion(origin_quat)


    combined_map = OccupancyGrid()
    combined_map.info = msg_in.info
    combined_map.header = msg_in.header
    combined_map.data = [0]*(Width*Height)

    for i in range (0, (Width*Height)-1):
        combined_map.data[i] = max(msg_in.data[i], image_map[i])

    pub_merged_map.publish(combined_map)

def callback_image_map(msg_in):
    global image_map

    image_height = msg_in.image.all.height
    image_width = msg_in.image.all.width
    image_data = msg_in.image.all.data
    image_tf = msg_in.tf

    for x in range (0, image_width):
        for y in range(0, image_height):
            index = ((y*width)+x)
            if image_data[index] = 0: #How are image values stored in ros imag??????????
                x_temp = ((x-(image_width/2))*image_resolution)
                y_temp = ((y-(image_width/2))*image_resolution)

                r = math.sqrt(math.pow(x_temp, 2) + math.pow(y_temp, 2))
                image_quat = [image_tf.rotation.x,
                          image_tf.rotation.y,
                          image_tf.rotation.z,
                          image_tf.rotation.w]
                image_angles = euler_from_quaternion(image_quat)

                mapx = image_tf.translation.x - Origin.position.x
                mapx = mapx + (r*math.cos(image_angles[2]-origin_angles[2]))
                mapy = image_tf.translation.y - Origin.position.y
                mapy = mapy + (r*math.sin(image_angles[2]-origin_angles[2]))

                x = int(round(mapx*(1/Resolution)))
                y = int(round(mapy*(1/Resolution)))

                if x<0 or x>(Width-1) or y<0 or y>(Height-1):
                    print "Outside map bounds!!!!"

                else:
                    index = ((y*Width)+x)
                    if mapData[index] < 100:
                        mapData[index] = 100

if __name__=='__main__':
    global pub_merged_map
    global image_map
    global initialized

    rospy.init_node('map_merger')

    pub_merged_map = rospy.Publisher("/merged_map", OccupancyGrid)

    rospy.Subscriber("/map", OccupancyGrid, callback_laser_map)

    initialized = false

    image_map = [0]*(Width*Height)

    rospy.loginfo("init")
    rospy.spin()