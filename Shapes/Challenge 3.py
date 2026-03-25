#Challenge 3
# Author: Riley
# Date: 03/06/2026


#Shape 1

#Gettings the users input for 
E = int(input("Please enter the length of E: "))
D = int(input("Please enter the length of F: "))    

#Import the math module
import math

#Math for calculate the height 
height = math.sqrt((E **2 - D ** 2))

#Calculate the Area

area = 0.5 * D * height

print(f"The total area of the shape is: {area}")



#Shape 2

#Impoting the math module
import math

#getting the users input for F and assigning the angle degree
F = int(input("Please enter the length of F: "))
angle_degree = 40

#converting the angle degree to radians
angle_radian = math.radians(angle_degree)

height = F * math.tan(angle_radian)
area = 0.5 * F * height


print(f"Total Area: {area}")


#Shape 3

#import the math module
import math

#Getting the unsers input for G and E and assigning the angle degree
G = int(input("Please enter the length of G: "))
E = int(input("Please enter the length of E: "))
angle_degree = 38

#Calculating the Semi circle area
radius = G / 2
semi_circle_area = 0.5 * math.pi * (radius ** 2)

#Calculating the rectangle area
rectangle_area = E * G

#Calculating the triangle area
angle_radian = math.radians(angle_degree)
tri_base = G / math.tan(angle_radian)
triangle_area = 0.5 * tri_base * G 

#Calculating the total area
total_area = semi_circle_area + rectangle_area + triangle_area


#Outputting the total area to the user
print(f"The total area of the shape is: {total_area}")

