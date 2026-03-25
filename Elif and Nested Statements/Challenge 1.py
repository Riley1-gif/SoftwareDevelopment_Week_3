# Challenge 1: Earthquake magnitude ranges
# Author: Riley
# Date: 03/06/2026


print("Welcome to the earthquake magnitude range checker. Please enter the magnitude of the earthquake to see which range it falls into.")
magnitude = float(input("Please enter the magnitude of the earthquake: "))

if magnitude < 2.0:
    print(f"A Magnitude of {magnitude} is considered to be a Very Minior earthquake.")
elif magnitude >= 2.0 and magnitude < 3.0:
    print(f"A Magnitude of {magnitude} is considered to be a Minor earthquake.")
elif magnitude >= 4.0 and magnitude <5.0:
    print(f"A Magnitude of {magnitude} is considered to be a Light eaerthquake.")
elif magnitude >=5.0 and magnitude <6.0:
    print(f"A Magnitude of {magnitude} is considered to be a moderate earthquake.")
elif magnitude >= 6.0 and magnitude <7.0:
    print(f"A Magnitude of {magnitude} is considered to be a strong earthquake.")
elif magnitude >= 7.0 and magnitude <8.0:
    print(f"A Magnitude of {magnitude} is considered to be a Major earthquake.")
elif magnitude >= 8.0 and magnitude <10.0:
    print(f"A Magnitude of {magnitude} is considered to be a Great earthquake.")
else: 
    print(f"A Magnitude of {magnitude} is considered to be a Meteoric earthquake.")
