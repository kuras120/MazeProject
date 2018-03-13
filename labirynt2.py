from turtle import *
from math import *
def readnext():
    n = ["","",""]
    b = a.readline()
    was = 0
    for i in b:
        if i == ' ' or i == '\n':
            was+=1
            continue
        n[was] += i
    return n

def init():
    b = a.read()
    v = 0
    for i in b:
        if i == '\n':
            v+=1
    v+=1
    leng = v
    v = int(sqrt(v))/2
    print(v)
    pu()
    org = [-v*size,v*size] 
    goto(org[0],org[1])
    pd()
    return org,leng

    
a = open("1.txt","r")
org = [0,0]
speed("fastest")
tracer(0, 0)
leng = 0
size = 5
org,leng = init()
a.seek(0)
for i in range(0,leng):
    update()
    m = readnext()
    pu()
    goto(org[0]+int(m[0])*size,org[1]-int(m[1])*size)
    setheading(270)
    pd()
    if(m[2].find('D')>-1):
        fd(size)
        bk(size)
    if(m[2].find('P')>-1):
        setheading(0)
        fd(size)
        bk(size)
turtle.update()
print(leng)


    
