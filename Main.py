# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:53:37 2022

@authors: Trent Menard, Ryan Hasty, Matt Wagers
"""

from User import Public
from User import Private
from User import User
from RSA_Menu import RSA_Menu
import sys

global repeat_Menu

base_User = User()
public_User = Public()
private_User = Private()

# This program may represent either a Public or Private User w/ unique keys & attributes
# For simplicity's sake, only actions among 1 Public and 1 Private User are demonstrated.
# IF YOU GET THE E IS UNDEFINED ERROR PLEASE CLOSE THE CONSOLE (KERNEL) AND RUN AGAIN.

def user_menu():
    repeat_Menu = True
    try:
    
        while repeat_Menu:
            menu_Result = RSA_Menu().get_Input()
            
            if menu_Result == 1:
                ans = int(input(RSA_Menu.PUBLIC_USER_MENU))
                
                if ans == 1:
                    message = input("\nEnter a message: ")
                    public_User.encrypt(message, public_User.public_key, public_User.length)
                    print("Message encrypted and sent!")
                    print("Encrypted Message: " + str(public_User.encrypted_msg))
                    
                elif ans == 2:
                    if (len(private_User.digital_signatures) == 0):
                        print("There are no digital signatures to authenticate.")
                        continue
                    
                    for idx, val in enumerate(private_User.digital_signatures):
                        print(idx + 1, " ", val)
                    
                    ans = int(input("\nPlease select a signature to validate: "))
                    print("Signed: ", public_User.authenticate(private_User.digital_signatures[ans-1], public_User.public_key, public_User.length))
                    
            elif menu_Result == 2:
                ans = int(input(RSA_Menu.PRIVATE_USER_MENU))
                
                if ans == 1:
                    
                    if len(public_User.encrypted_messages) == 0:
                        print("There are no messages available to decrypt.")
                        continue
                    
                    print("Encypted messages available:\n")
                    
                    for idx, val in enumerate(public_User.encrypted_messages):
                        print(idx + 1, ": (length =", str(len(val)) + str(")"))
                    
                    ans = int(input("Please select the message index to decrypt: "))
                    
                    private_User.decrypt(public_User.encrypted_messages[ans-1], private_User.d, public_User.length)
                    print("\nDecrypted Message: " + str(private_User.decrypted_messages[ans-1]))
                    
                elif ans == 2:
                    message = input("\nEnter desired signature: ")
                    private_User.sign_message(message, private_User.d, private_User.length)
                    print("Signature sent!")
                    print(private_User.digital_signatures)
                    
            elif menu_Result == 3:
                repeat_Menu = False
            
    except KeyboardInterrupt:
        print("\n\nDetected Ctrl + C; Quitting.")
        sys.exit()
    except ValueError:
        print("\nInvalid choice. Try again or press CTRL + C to quit.")
        user_menu()
        
user_menu()

