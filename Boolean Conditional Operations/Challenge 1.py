#Challenge 1: Enrollment in a school
# Author: Riley
# Date: 03/06/2026

#Requirements:
#Lives less than 4 km from the school
#Is under 18 years old
#Has the right to stay in New Zealand

print("Welcome to the school enrollment system. Please answer the following questions to see if you are eligible for enrollment.")
age = int(input("Please enter your age: "))
distance_from_school = int(input("Please enter the distance from school in Km's: "))
right_to_stay = input("Do you have the right to stay in New Zealand? (yes/no): ")

if right_to_stay == "no":
    international_fees = input("Will you be paying international fees? (yes/no): ")
    if international_fees == "no":
        print("You are not eligible for enrollment.")
    else:
        if distance_from_school <= 4 and age < 18:
            print("You are eligible for enrollment.")
        else:
            print("You are not eligible for enrollment.")
