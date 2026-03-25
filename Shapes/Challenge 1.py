# Challenge 1
# Author: Riley
# Date: 03/06/2026


#Shape 1

#Getting the users Input for J and K 

J = int(input("Please enter the length of J: "))
K = int(input("Please enter the length of K: "))


#Math for working out the Area using J and K
total_area = 0.5 * K * J


#outputting the total area to the user
print (f"The total area of the shape is: {total_area}")




#Shape 2:

#Getting the users Input for G, S, W and Q
G = int(input("Please enter the length of G: "))
S = int(input("Please enter the length of S: "))
W = int(input("Please enter the length of W: "))
Q = int(input("Please enter the length of Q: "))


#Math for working out the Area using G, S, W and Q
total_area2 = S * G 
cut_out_area = W * Q

#Final area for the blue shape

final_area = total_area2 - cut_out_area

#outputting the total area to the user
print (f"The total area of the shape is: {final_area}")




#Shape 3:


#Getting the users Input for U, M and N
U = int(input("Please enter the length of U: "))
M = int(input("Please enter the length of M: "))
N = int(input("Please enter the length of N: "))

#Math for working out the separate areas using U, M and N
rectangle_area = U * M
triangle_area = 0.5 * (N ** 2)

#Math of Final area for the blue shape
total_area3 = rectangle_area + triangle_area

#outputting the total area to the user
print (f"The total area of the shape is: {total_area3}")

