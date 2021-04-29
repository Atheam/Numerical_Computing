import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import svd
from random import random

#generating a sphere
n = 300
s = np.random.uniform(0,2*np.pi,(1,n))
t = np.random.uniform(0,np.pi,(1,n))
v = lambda s,y : np.array([[np.cos(s) * np.sin(t)],[np.sin(s) * np.sin(t)],[np.cos(t)]])
sphere = v(s,t).reshape(3,n)

#generating A matrixes    
A1 = np.random.uniform(0,2,(3,3)) 
A2 = np.random.uniform(0,15,(3,3)) 
A3 = np.random.uniform(-5,5,(3,3)) 

#creating ellipses
ell1 = A1@sphere
ell2 = A2@sphere
ell3 = A3@sphere

#svd A matrixes
U1, S1, V1 = svd(A1)
U2, S2, V2 = svd(A2)
U3, S3, V3 = svd(A3)

#drawing A1 transformation 
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.set_title("A1 transformation")
axis = U1*S1
ax.quiver(0,0,0,axis[0],axis[1],axis[2],color = 'black')
ax.scatter(sphere[0],sphere[1],sphere[2])
ax.scatter(ell1[0],ell1[1],ell1[2])
plt.show()


#drawing A2 transformation 
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.set_title("A2 transformation")
axis = U2*S2
ax.quiver(0,0,0,axis[0],axis[1],axis[2],color = 'black')
ax.scatter(sphere[0],sphere[1],sphere[2])
ax.scatter(ell2[0],ell2[1],ell2[2])
plt.show()


#drawing A3 transformation 
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.set_title("A3 transformation")
axis = U3*S3
ax.quiver(0,0,0,axis[0],axis[1],axis[2],color = 'black')
ax.scatter(sphere[0],sphere[1],sphere[2])
ax.scatter(ell3[0],ell3[1],ell3[2])
plt.show()

#finding A with max and min singular value ratio > 100 
diff = -1
while diff < 100:
    A4 = np.random.uniform(0,3,(3,3)) 
    diag_values = np.diag(A4)
    U,S,V = svd(A4)
    diff = max(S) /min(S)

#creating ellipse
ell4 = A4@sphere

#drawing A4 transformation
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.set_title("A4 transformation")
axis = U*S
ax.quiver(0,0,0,axis[0],axis[1],axis[2],color = 'black')
ax.scatter(sphere[0],sphere[1],sphere[2])
ax.scatter(ell4[0],ell4[1],ell4[2])
plt.show()


#choosed matrix A1

#drawing ZV where Z is a sphere 

ell = (sphere.transpose() @V1).transpose()
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.set_title("rotation by V vector")
ax.scatter(ell[0],ell[1],ell[2])
plt.show()

#drawing ZSV where Z is the sphere 

ell = (sphere.transpose()*S1 @V1).transpose()
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.set_title("rotation by V and scaling by Sigma")
ax.scatter(ell[0],ell[1],ell[2])
plt.show()

#drawing ZUSV where Z is the sphere 

ell = (sphere.transpose()@U1*S1 @V1).transpose()
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.set_title("Complete transformation rotation - scaling")
ax.scatter(ell[0],ell[1],ell[2])
plt.show()







