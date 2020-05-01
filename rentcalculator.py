#!/usr/bin/env python3

while True: 
  try: 
    rent = float(input ("\nPlease enter the rent amount for this month: $"))
    bge = float(input("Please enter the utility amount for this month: $"))
    break
  except ValueError: 
    print ("\nMr.Bond, You've entered an invalid number, try again 👾👾👾 ")
    

R = rent/2
B = bge/2

Zach = R+B
Yeshi = rent - Zach
print(f"\n⨊ Zach's Total amount: ‣${Zach}")
print(f"⨊ Yesh's Total amount: ‣${Yeshi}\n")
