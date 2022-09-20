# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:37:11 2022

@author: Trent Menard, Matt Wagers, Ryan Hasty
"""

import sys
import random
import math

def FermatPrimalityTest(n):
    # Arbitrairly test 20 values within range to verify primality
    for test in range(1, 20):
        test = random.randint(MIN_PRIME_NUMBER + 1, MAX_PRIME_NUMBER - 1)
        all_candidates.add(test)
        
        if pow(test, n-1, n) != 1:
            failed_prime_candidates.add(n)
            return False
        else:
            prime_candidates.add(n)
            
    # Pass Fermat test if all 20 tests pass
    return True

def encrypted_message():
    #create a dictionary to store more than one message?
    pass
    
def sign_message(sig_msg,d):
    #I guess we just create a variable for the signature?
    upper_msg = sig_msg.upper()
    char_to_ascii = [ord(x) for x in upper_msg]
    signed = [pow(m,d,n) for m in char_to_ascii]
    print(signed)
    return signed
    
def public_user():
    ans = int(input("\nAs a public user, what would you like to do?\n" +
                    "1. Send an encrypted message.\n" +
                    "2. Authenticate a digital signature.\n" + 
                    "3. Exit.\n" +
                    "\n Enter your choice: "))
    
    if ans == 1:
        message = input("\nEnter a message: ")
        encrypt(message,e,n) # encrypt function
    elif ans == 2:
        #uncomment line below when we get d accessible
        sign_message(sig_msg,d) #sign function
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
        sign_message(sig,d)
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
    # Map char -> ASCII code
    char_to_ascii = [ord(x) for x in upper_msg]
    # Encrypt each ASCII code using Fast Modular Exponentiation with Public Key
    encryptedM = [pow(m,e,n) for m in char_to_ascii]
    return encryptedM
    
def decrypt(e_msg,d,n):
    finish = ''
    # Decrypt using Fast Modular Exponentiation
    char_to_ascii = [pow(c,d,n) for c in e_msg]
    # Map ASCII code-> char
    d_msg = [chr(x) for x in char_to_ascii]
    for x in d_msg:
        finish += x
    return finish
    
# Fast Euclidean Algorithm to calculate d
def e_gcd(a = 1, b = 1):
    if b == 0:
        return (1, 0, a)
    (x, y, d) = e_gcd(b, a%b)
    return y, x - a//b*y, d

# class PublicUser:
#     public_key = ""
#     private_key = ""
    
# Fermat's Little Theorem for parameters of pow() (Fast Modular Exponentantiaion) to gen p & q
MIN_PRIME_NUMBER = 1_000_000
MAX_PRIME_NUMBER = 10_000_000

# Generate random p & q val between 1 & 10 million
p_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
q_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
all_candidates = set()
prime_candidates = set()
failed_prime_candidates = set()

n = p_val * q_val
phi = (p_val - 1) * (q_val - 1)
e = random.randint(1, phi + 1)

# Generate random e (public key) using Euclid's algorithm until its relatively prime to phi
while not math.gcd(e, phi) == 1: 
    e = random.randint(1, phi + 1)

#this is how we get d
d = e_gcd(e,phi)
d = d[0]

# If p_val is not prime, generate another p_val
while not FermatPrimalityTest(p_val):
    p_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
    
# If q_val is not prime, generate another q_val
while not FermatPrimalityTest(q_val):
    q_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)

prompt()

print("Generated p_val = " + str(p_val) + " & q_val = " + str(q_val) + "\n")
print("Success: " + str(prime_candidates) + "\n")
print("Failed: " + str(failed_prime_candidates) + "\n")
print("All Candidates: " + str(all_candidates) + "\n")
print("Prime/All Candidates Ratio: " + str(len(prime_candidates) / len(all_candidates)) + "%")
print("Prime/Failed Candidates Ratio: " + str(len(prime_candidates) / len(failed_prime_candidates)) + "%")
