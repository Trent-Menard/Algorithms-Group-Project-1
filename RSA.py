# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:37:11 2022

@author: Trent
"""

import math
import pandas as pd #Dr. Hu said he wasn't against us using pandas

class PublicUser:
    public_key = ""
    private_key = ""
    
# How to choose parameters for pow() to get p & q? Random Num Gen? What for min & max?
# base, power, %
p_val = pow(30192, 43791, 65301)
q_val = pow(30192, 43791, 65301)
public_key = 0;
phi = 0;
e = 0;

# Random Num Gen?
    if math.gcd(x, phi) == 1:
        x = e;
        break

#test to store messages inside a dataframe
#only 

def encrypted_message():
    #create a dictionary to store more than one message?
    
def sign_message(sign):
    #I guess we just create a variable for the signature?
    

def public_user():
    ans = 0
    ans = int(input("\nAs a public user, what would you like to do?\n\t
                    "1. Send an encrypted message\n\t
                    "2. Authenticate a digital signature\n\t
                    "3. Exit\n
                    "Enter your choice: "))
    if ans == 1:
        message = input("\nEnter a message: ")
        #call funtion to encrypt a message (message)
    elif ans == 2:
        #call funtion to authenticate a digital signature
    else:
        prompt()
    
def owner():
    ans = 0
    ans = int(input("\nAs the owner of the keys, what would you like to do?\n\t
                    "1. Decrypt a received message
                    "2. Digitally sign a message
                    "3. Exit\n
                    "Enter your choice: "))
    if ans == 1:
        #call function to list encrypted messages
        print("\nThe following messages are available:\n\t")
    elif ans == 2:
        #call function to signs a message
        sig = input("\nEnter a message: ")
        sign_message(sig)
        
def prompt():
    ans = 0
    ans = int(input("Please select your user type\n\t"
          "1. A public user\n\t"
          "2. The owner of the keys\n\t"
          "3. Exit program\n"
          "Enter your choice: "))
    if ans == 1:
        public_user()
    elif ans == 2:
        owner()
    else:
        #return
        
    