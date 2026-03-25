#Challenge 2: Sound Levels
#Author: Riley
#Date: 03/06/2026


noise_level = int(input("Please enter the noise level in decibels: "))

if noise_level == 130:
    print(f"The noise level of {noise_level} is the same as a Jackhammer. ")
elif noise_level > 107 and noise_level < 130:
    print(f"The noise level of {noise_level} is between the sound of a Jackhammer and a petrol lawnmower. ")
elif noise_level == 106:
    print(f"The noise level of {noise_level} is the same as a petrol lawnmower.")
elif noise_level > 71 and noise_level <106:
    print(f"The Noise level of {noise_level} is between a petrol lawnmower and a alarm clock. ")
elif noise_level == 70:
    print(f"The Noise level of {noise_level} is the same as a alarm clock.")
elif noise_level > 40 and noise_level < 70:
    print(f"The noise level of {noise_level} is between a alarm clock and a quiet room.")
elif noise_level == 40:
    print(f"the noise level of {noise_level} is the same as a quiet room.")
elif noise_level <40:
    print("The noise level is less than a quiet room.")
elif noise_level > 130:
    print("The noise level is louder than a Jackhammer.")
else:
    print("Please enter a valid noise level.")