# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:47:17 2022

@author: Trent
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
