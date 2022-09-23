# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:47:17 2022

@authors: Trent Menard, Ryan Hasty, Matt Wagers
"""

class RSA_Menu:
    def __init__(self):
        self.prompt_value = """
Select User Type\n
  1. Public User.\n
  2. Key Owner.\n
  3. Exit Program.\n
Enter your choice: \r"""
    
    def get_Input(self):
        ans = int(input(self.prompt_value))
        return ans

    MAIN_MENU = """
Select User Type\n
  1. Public User.\n
  2. Key Owner.\n
  3. Exit Program.\n
  Enter your choice: \r"""

    PUBLIC_USER_MENU = """
  \nAs a public user, what would you like to do?\n
1. Send an encrypted message.\n
2. Authenticate a digital signature.\n
3. Exit.\n
  Enter your choice: \r"""
  
    PRIVATE_USER_MENU = """
\nAs a key owner, what would you like to do?\n
  1. Decrypt a received message.\n
  2. Digitally sign a message.\n
  3. Exit.\n
  Enter your choice: \r"""
