#Challenge 3: Vowel or Consonant Checker
#Author: Riley
#Date: 03/06/2026

letter = input("Please enter a letter to check if it is a vowel or consonant: ")

if letter in "aeiou" or letter in "AEIOU":
    print(f"The letter {letter} is a vowel.")
elif letter == "y":
    print(f"The letter {letter} can be a vowel or a consonant depending on the word.")
else:
    print(f"The letter {letter} is a consonant.")