#!/usr/bin/env python


#--------Include modules---------------
from copy import copy
import rospy
from visualization_msgs.msg import Marker
from std_msgs.msg import String
from geometry_msgs.msg import Point
from os import system

from random import random
from numpy import array
from numpy import delete
from numpy import concatenate
from numpy import where
from numpy import logical_and as AND
from numpy import linalg as LA
from functions import Near
from functions import Steer
from functions import ObstacleFree
from numpy import vstack
from numpy import delete
from numpy import all as All
from functions import Find
from functions import Cost
from functions import prepEdges
#-------------------------------------


E=vstack((array([0,0,0,0]),array([0,0,1,1]),array([1,1,2,2]),array([2,2,3,3]),array([1,1,5,5])))


print prepEdges(E)

 
  
 
 
