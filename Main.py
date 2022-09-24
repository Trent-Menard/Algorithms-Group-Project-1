# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:53:37 2022

@author: Trent, Ryan, Matt
"""

import User

def public_user():
    ans = ""
    ans = str(input("""
    As a public user, what would you like to do?
    1. Send an encrypted message
    2. Authenticate a digital signature
    3. Exit
    Enter your choice: """))
    if ans == "1":
        message = input("\nEnter a message: ")
        e_msg = User.encrypt(message, e, n) # encrypt message
        print("Message encrypted and sent.")
        return e_msg
    elif ans == "2":
        index = 1
        print("\nThe following messages are available:\n\t")
        for x in signed_msgs: # list authenticated msgs as well as authenticate
            auth = User.authenticate(signed_msgs[index-1], e, n)
            print(auth)
            index+=1
        
        
        # help me lol this code is awful ik
        # Which message do you want to decrypt
        #choice = int(input("\nEnter your choice: "))
        
        # NOT SURE HOW TO DO THIS PART PROPERLY
        print("Signature is valid.")
        
        public_user()
    else:
        print("\nThere are no signatures...")
        prompt()
    
def owner():
    ans = ""
    ans = str(input(""" 
    As the owner of the keys, what would you like to do?
    1. Decrypt a received message
    2. Digitally sign a message
    3. Exit
    Enter your choice: """))
    if ans == "1":
        index = 1
        #call function to list encrypted messages
        print("\nThe following messages are available:\n\t")
        for x in myMsgs:
            print(" ",str(index) + ". (Length =",str(len(x)) + ")")
            index+=1
        
        # Which message do you want to decrypt
        choice = int(input("\nEnter your choice: "))
        print("Decrypted Message: ", User.decrypt(myMsgs[choice-1], d, n))
        owner()
            
    elif ans == "2":
        #call function to signs a message
        sig = input("\nEnter a message: ")
        # sign messages by using pass in d, n and add to list
        mySig = User.sign_message(sig, d, n)
        print("Message signed and sent.")
        return mySig
    else:
        prompt()
        
# initial prompt and basically main
def prompt():
    ans = ""
    ans = str(input("""
    Please select your user type
    1. A public user
    2. The owner of the keys
    3. Exit program
    Enter your choice: """))
    if ans == "1":
        global myMsgs # my encrypted messages (length = n)
        myMsgs += [public_user()] # store result from public_user into list
        public_user()
    elif ans == "2":
        global signed_msgs
        signed_msgs += [owner()]
        owner()
    elif ans == "3":
        return False
    else:
        print("invalid option...")
        prompt()
        
# generate starting values
e,n,phi = User.gen_vals()

# this is how we calculate d
d = User.e_gcd(e,phi)
d = d[0]%phi

signed_msgs = []
myMsgs = []

# start program
while(True):
    prompt()