import re
import math
from heapq import nsmallest

a=input().split(" ")

d=[]
coordinates=[]
coordinatex=[]
coordinatey=[]
coordinatez=[]
value=[]

for i in range(int(a[0])+1): #to get user inputs
    b=input()
    d.append(b)

#print(d)
    
for i in range(int(a[0])+1): #use to get the numbers from the input type (x,y)
    coordinates.append(" ".join(re.findall("[-+]?[.]?[\d]+(?:,\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?",d[i])).split(" "))

#print(coordinates)
    
for i in range(int(a[0])+1): #To make two lists of X coordinates and Y coodinates
    coordinatex.append(float(coordinates[i][0])) #x coordinate list
    coordinatey.append(float(coordinates[i][1])) #y coordinate list
    if(len(coordinates[i])==3):
        coordinatez.append(float(coordinates[i][2]))

#print(coordinatex)
#print(coordinatey)
#print(coordinatez)

for i in range(0,len(coordinatex)-1):
    x=abs(coordinatex[len(coordinatex)-1]-coordinatex[i]) #to get the (x1-x2) value
    y=abs(coordinatey[len(coordinatey)-1]-coordinatey[i]) #to gwt the (y1-y2) Value

    if(len(coordinatez)>0): #for 3d points
        z=abs(coordinatez[len(coordinatez)-1]-coordinatez[i]) #to get the (z1-z2) value
    else:
        z=0

    result=math.sqrt((x**2)+(y**2)+z**2) #the distance between the point
    value.append(result)  #list of distance between the points to the given point

#print(value)
    
p=nsmallest(int(a[1]),value) #to get the smallest int(a[1]) number of values from the value

#print(p)
coordinatex.pop(-1) #to pop the last value of the x coordinate list
coordinatey.pop(-1) #to pop the last value of the y coordinate list
if(len(coordinatez)>0):   #to pop the last value of the z coordinate list if it is a 3d
    coordinatez.pop(-1)
    

for i in range(0,len(p)):#to print and to pop at last
    if(len(coordinatez)>0):
        print("")
        print("Coordinate: ",(i+1))
        print("(",coordinatex[value.index(p[i])],",",coordinatey[value.index(p[i])],",",coordinatez[value.index(p[i])],")")
    else:
        print("")
        print("Coordinate : ",(i+1))
        print("(",coordinatex[value.index(p[i])],",",coordinatey[value.index(p[i])],")")
        


        
    coordinatex.pop(value.index(p[i]))
    coordinatey.pop(value.index(p[i]))
    if(len(coordinatez)>0): #checking whether 2d or 3d
        coordinatez.pop(value.index(p[i]))
    value.pop(value.index(p[i]))
    

c=input("press Enter To Exit")




    
