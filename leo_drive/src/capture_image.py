#!/usr/bin/env python
from __future__ import print_function

import roslib
roslib.load_manifest('leo_drive')
import sys
import rospy
import numpy as np
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

  def __init__(self):
    #self.image_pub = rospy.Publisher("image_topic_2",Image)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/image_raw",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "passthrough")
    except CvBridgeError as e:
      print(e)

    (rows,cols,channels) = cv_image.shape
    
    if channels==4 :
    	img= cv_image[:,:,0:3]
    	
    else:
    	img=cv_image
    img= np.flip(img,axis=2)
    	
    '''if cols > 60 and rows > 60 :
      cv2.circle(cv_image, (50,50), 10, 255)
	'''
    cv2.imshow("Image window", img)
    cv2.waitKey(3)
    '''
    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "passthrough"))
    except CvBridgeError as e:
      print(e)'''

def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
