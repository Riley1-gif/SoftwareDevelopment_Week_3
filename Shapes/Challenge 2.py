# Challenge 2
# Author: Riley
# Date: 03/06/2026


#Shape 1

#Getting the users Input for X and Y 
X = int(input("Please enter the length of X: "))
Y = int(input("Please enter the length of Y: "))

#Math for working out the Area using X and Y

total_area = X * Y 

#outputting the total area to the user
print (f"The total area of the shape is: {total_area}")



#Shape 2 
#Importing the math module to find the value of pi
import math

#Getting the users Input for C
C = int(input("Please enter the Radius of C: "))

#Math for working out the Area using C
total_area2 = math.pi * (C ** 2)

#outputting the total area to the user
print (f"The total area of the shape is: {total_area2}")


#Shape 3

#Getting the users Input for G, E and F
G = int(input("Please enter the length of G: "))
E = int(input("Please enter the length of E: "))
F = int(input("Please enter the length of F: "))

#import the math module to find the value of pi
import math
#Math for working out the Area using G, E and F
radius = G / 2
semi_circle_area = 0.5 * math.pi * (radius ** 2)
rectangle_area = E * G
triangle_area = 0.5 * F * G

total_area3 = semi_circle_area + rectangle_area + triangle_area

#outputting the total area to the user
print (f"The total area of the shape is: {total_area3}")