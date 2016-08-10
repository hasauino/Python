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
from numpy import concatenate
from numpy import vstack

from numpy import linalg as LA
from functions import Nearest
from functions import Steer
import parameters as param
from functions import ObstacleFree







#-------------------------------RRT------
x_init=array([0.10,0.10])
V=array([x_init])
i=1.0
E=concatenate((x_init,x_init))


while True:
# Sample free
 x_rand = array([param.dim*random(),param.dim*random()])
 
# Nearest
 x_nearest=V[Nearest(V,x_rand),:]

# Steer
 x_new=Steer(x_nearest,x_rand,param.eta)

# ObstacleFree
 mapsub=1
 if ObstacleFree(x_nearest,x_new,mapsub,param.steps):
 	V=concatenate((V,array([x_new])), axis=0)
        temp=concatenate((x_nearest,x_new))
        E=vstack((E,temp))


 
 
 
 
 
 
