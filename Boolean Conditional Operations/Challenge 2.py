#Challenge 2: Shopping Cart
#Author: Riley 
#Date: 03/06/2026

is_registered = input("Are you registered with our store? (yes/no): ")
cart_count = 0 
is_guest = False
is_buying_gift_card = True

standard_purchase = is_registered == "yes" and cart_count > 0

other_purchase = is_guest or is_buying_gift_card


if standard_purchase or other_purchase:
    print("You can proceed to checkout.")
else:    
    print("You cannot proceed to checkout.")