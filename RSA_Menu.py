# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:47:17 2022

@author: Trent
"""

import sys

class RSA_Menu:
    def __init__(self):
        self.prompt_value = """
Select User Type\n
  1. Public User.\n
  2. Key Owner.\n
  3. Exit Program.\n
Enter your choice: \r"""
        self.get_Input()
    
    def get_Input(self):
        ans = int(input(self.prompt_value))
       
        if ans == 1:
            self.prompt_value = """
\nAs a public user, what would you like to do?\n
  1. Send an encrypted message.\n
  2. Authenticate a digital signature.\n
  3. Exit.\n
Enter your choice: \r"""
            
        elif ans == 2:
            self.prompt_value = """
  \nAs a key owner, what would you like to do?\n
1. Decrypt a received message.\n
2. Digitally sign a message.\n
3. Exit.\n
Enter your choice: \r"""
  
        elif ans == 3:
            sys.exit("Goodbye.")
            
        else:
            print("Invalid choice.")

        # return ans
