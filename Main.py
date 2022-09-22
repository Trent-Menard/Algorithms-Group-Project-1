# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:53:37 2022

@author: Trent
"""

from User import User
from User import Public
from RSA_Menu import RSA_Menu

user = User()
RSA_menu = RSA_Menu().get_Input()
public_user = Public()

public_user.prompt()
