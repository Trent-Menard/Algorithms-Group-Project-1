# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:53:37 2022

@author: Trent
"""

from User import Public
from User import Private
from RSA_Menu import RSA_Menu

repeat_Menu = True
encrypted_message = None
decrypted_message = None

while repeat_Menu:
    menu_Result = RSA_Menu().get_Input()
    
    if menu_Result == 1:
        public_User = Public()
        ans = int(input(RSA_Menu.PUBLIC_USER_MENU))
        
        if menu_Result == 1:
            message = input("\nEnter a message: ")
            encrypted_message = public_User.encrypt(message,public_User.public_key,public_User.length)
    
    elif menu_Result == 2:
        private_User = Private()
        ans = int(input(RSA_Menu.PRIVATE_USER_MENU))
        
        if ans == 1:
            decrypted_message = private_User.decrypt(encrypted_message, private_User.d, private_User.length)
    
    elif menu_Result == 3:
        repeat_Menu = False
    else:
        print("Invalid choice.")
