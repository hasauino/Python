from emp import Steer

from numpy import array

xnearest=array([0.,0.])
xrand=array([5.,5.])
eta=1.

res=Steer(xnearest,xrand,eta)
print res.get()

