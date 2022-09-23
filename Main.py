# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:53:37 2022

@author: Trent
"""

from User import Public
from User import Private
from RSA_Menu import RSA_Menu
import math

repeat_Menu = True
encrypted_message = None
decrypted_message = None

while repeat_Menu:
    menu_Result = RSA_Menu().get_Input()
    
    if menu_Result == 1:
        public_User = Public()
        prompt_value = """
\nAs a public user, what would you like to do?\n
  1. Send an encrypted message.\n
  2. Authenticate a digital signature.\n
  3. Exit.\n
Enter your choice: \r"""
        ans = int(input(prompt_value))
        
        if ans == 1:
            message = input("\nEnter a message: ")
            encrypted_message = public_User.encrypt(message,public_User.public_key,public_User.length)
    
    elif menu_Result == 2:
        private_User = Private()
        prompt_value = """
  \nAs a key owner, what would you like to do?\n
1. Decrypt a received message.\n
2. Digitally sign a message.\n
3. Exit.\n
Enter your choice: \r"""
        ans = int(input(prompt_value))
        # Prob want to make params only encrypted msg & call other params from inside class
        if ans == 1:
            decrypted_message = private_User.decrypt(encrypted_message,math.gcd(private_User.public_key, private_User.phi),private_User.length)
    elif menu_Result == 3:
        repeat_Menu = False
    else:
        print("Invalid choice.")

print("Pub Key: " + str(public_User.public_key))
print("N (PQ): " + str(public_User.length))
print("Phi: " + str(public_User.phi))

print(str(decrypted_message))
