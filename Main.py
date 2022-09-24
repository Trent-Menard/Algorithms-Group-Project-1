# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:53:37 2022

@authors: Trent Menard, Ryan Hasty, Matt Wagers
"""

from User import Public
from User import Private
from RSA_Menu import RSA_Menu

repeat_Menu = True
encrypted_message = None
decrypted_message = None
sig_msg = None
d_sig_msg = None

public_User = Public()
private_User = Private()

while repeat_Menu:
    menu_Result = RSA_Menu().get_Input()
    
    if menu_Result == 1:
        
        ans = int(input(RSA_Menu.PUBLIC_USER_MENU))
        if menu_Result == 1:
            message = input("\nEnter a message: ")
            encrypted_message = public_User.encrypt(message,public_User.public_key,public_User.length)
        elif menu_Result == 2:
            d_sig_msg = public_User.encrypt(sig_msg, public_User.public_key, public_User.length)
    
    elif menu_Result == 2:
        ans = int(input(RSA_Menu.PRIVATE_USER_MENU))
        
        if ans == 1:
            decrypted_message = private_User.decrypt(encrypted_message, private_User.d, private_User.length)
        elif ans == 2:
            message = input("\nEnter a message: ")
            sig_msg = private_User.sign_message(message, private_User.d, private_User.length)
    
    elif menu_Result == 3:
        repeat_Menu = False
    else:
        print("Invalid choice.")
