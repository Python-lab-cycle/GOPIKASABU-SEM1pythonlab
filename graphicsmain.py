from graphics.rectangleAPFunction import*
from graphics.CircleAPFunction import*
from graphics.dgraphics.cuboidAPFunction import*
from graphics.dgraphics.sphereAPFun import*

num1=int(input("enter length of rectangle"))
num2=int(input("enter breadth of rectangle"))
print("area=",RArea(num1,num2))
print("perimeter=",Rperimeter(num1,num2))

radius=int(input("enter the radius of circle"))
print("circle area",CArea(radius))
print("circle area",CPerimetr(radius))

radius=int(input("enter the radius of spere"))
print("area of spere",Asphere(radius))
print("perimeter of spere",Psphere(radius))

edge=int(input("enter the edge of cuboid"))
l=int(input("enter the length of cuboid"))
b=int(input("enter the breadth of cuboid"))
h=int(input("enter the height of cuboid"))
print("area of cuboid",Acuboid(radius))
print("perimeter of cuboid",Pcuboid(l,b,h))


