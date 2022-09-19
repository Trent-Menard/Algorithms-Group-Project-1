# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:37:11 2022

@author: Trent Menard, Matt Wagers, Ryan Hasty
"""

import sys
import random

# class PublicUser:
#     public_key = ""
#     private_key = ""
    
# Use Fermat's Little Theorem for parameters of pow() to gen p & q
# Large prime numbers for testing; from https://bigprimes.org/
MIN_PRIME_NUMBER = 1000000
MAX_PRIME_NUMBER = 10000000

# Generate random p & q val between 1 & 10 mil
p_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
q_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER) 
all_candidates = set()
prime_candidates = set()
failed_prime_candidates = set()

def FermatPrimalityTest(n):
    # Arbitrairly test 20 values within range to verify primality
    for a in range(1, 20):
        test = random.randint(MIN_PRIME_NUMBER + 1, MAX_PRIME_NUMBER - 1)
        all_candidates.add(test)
        
        if pow(test, n-1, n) == 1:
            prime_candidates.add(n)
        else:
            failed_prime_candidates.add(n)
            # print(p, " is NOT prime.")
            # return False
        
    # print(p, " is prime!")
    return True
    
# If p_val is not prime, generate another p_val
while not FermatPrimalityTest(p_val):
    p_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
    
# If q_val is not prime, generate another q_val
while not FermatPrimalityTest(q_val):
    q_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
    
    
print("Generated p_val = " + str(p_val) + " & q_val = " + str(q_val) + "\n")
print("Success: " + str(prime_candidates) + "\n")
print("Failed: " + str(failed_prime_candidates) + "\n")
print("All Candidates: " + str(all_candidates) + "\n")
print("Error Ratio: " + str(len(failed_prime_candidates) / len(all_candidates)) + "%")

# print("D: ",d)
# print("E: ",e)
# print("N: ",n)
# print("Phi: ",phi)
# print(e)

def encrypted_message():
    #create a dictionary to store more than one message?
    pass
    
def sign_message(sign):
    #I guess we just create a variable for the signature?
    pass
    
def public_user():
    ans = int(input("\nAs a public user, what would you like to do?\n" +
                    "1. Send an encrypted message.\n" +
                    "2. Authenticate a digital signature.\n" + 
                    "3. Exit.\n" +
                    "\n Enter your choice: "))
    
    if ans == 1:
        message = input("\nEnter a message: ")
        #call funtion to encrypt a message (message)
        # encrypt(message,e,n)
    elif ans == 2:
        #call funtion to authenticate a digital signature
        pass
    elif ans == 3:
        sys.exit("Goodbye.")
    else:
        print("Invalid choice.")
        public_user()
    
def owner():
    ans = int(input("\nAs the owner of the keys, what would you like to do?\n" +
                    "1. Decrypt a received message.\n" +
                    "2. Digitally sign a message.\n" +
                    "3. Exit.\n" +
                    "\nEnter your choice: "))
    if ans == 1:
        #call function to list encrypted messages
        print("\nThe following messages are available:\n\t")
    elif ans == 2:
        #call function to signs a message
        sig = input("\nEnter a message: ")
        sign_message(sig)
    elif ans == 3:
        sys.exit("Goodbye.")
    else:
        print("Invalid choice.")
        owner()
        
def prompt():
    ans = int(input("Please select your user type\n" +
          "1. A public user.\n" +
          "2. The owner of the keys.\n" +
          "3. Exit program\n" +
          "\nEnter your choice: "))
    
    if ans == 1:
        public_user()
    elif ans == 2:
        owner()
    elif ans == 3:
        sys.exit("Goodbye.")
    else:
        print("Invalid choice.")
        prompt()
        
def encrypt(message,e,n):
    upper_msg = message.upper()
    encrypted = [ord(x) for x in upper_msg] # generate numerical alphabet
    print("\nASCII VALUES OF MESSAGE: ",encrypted, "\n") # remove this line when ready
    encryptedM = [pow(m,e,n) for m in encrypted] # encrypt each letter
    print("C = (M^e)modn --> ", encryptedM, "\n") # remove this line when ready
    return encryptedM
    
def decrypt(e_msg,d,n):
    finish = ''
    decrypted = [pow(c,d,n) for c in e_msg]
    print("M = (C^d)modn -->",decrypted, "\n") # remove this line when ready
    d_msg = [chr(x) for x in decrypted]
    for x in d_msg:
        finish += x
    return finish
    
def e_gcd(a =1, b = 1):
    if b == 0:
        return (1, 0, a)
    (x, y, d) = e_gcd(b, a%b)
    return y, x - a//b*y, d

# encryptM = encrypt("Ths message is top secret af",e,n)
# print(decrypt(encryptM,d,n))
