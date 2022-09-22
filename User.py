# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:34:17 2022

@author: Trent
"""

import random
import math

MIN_PRIME_NUMBER = 1_000_000
MAX_PRIME_NUMBER = 10_000_000
prime_candidates = set()

def FermatPrimalityTest(n):
    # Arbitrairly test 20 values within range to verify primality
    for test in range(1, 20):
        test = random.randint(MIN_PRIME_NUMBER + 1, MAX_PRIME_NUMBER - 1)
        
        if pow(test, n-1, n) != 1:
            return False
        else:
            prime_candidates.add(n)
            return True
    # Pass Fermat test if all 20 tests pass

# Fast Euclidean Algorithm to calculate d
def e_gcd(a = 1, b = 1):
    if b == 0:
        return (1, 0, a)

class User:
    
    def __init__(self):
        self.p_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
        self.q_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
        
        n = self.p_val * self.q_val
        phii = (self.p_val - 1) * (self.q_val - 1)
        e = random.randint(1, phii + 1)
        
        # Generate random e (public key) using Euclid's algorithm until its relatively prime to phi
        while not math.gcd(e, phii) == 1: 
            e = random.randint(1, phii + 1)
        
        self.public_key = e
        self.length = n
        self.phi = phii
        
        # If p_val is not prime, generate another p_val
        while not FermatPrimalityTest(self.p_val):
            self.p_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
            
        # If q_val is not prime, generate another q_val
        while not FermatPrimalityTest(self.q_val):
            self.q_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
            
    def encrypt(self, message,e,n):
        upper_msg = message.upper()
        # Map char -> ASCII code
        char_to_ascii = [ord(x) for x in upper_msg]
        # Encrypt each ASCII code using Fast Modular Exponentiation with Public Key
        encryptedM = [pow(m,e,n) for m in char_to_ascii]
        
        for val in encryptedM:
            print(val)
            
        self.e_msg = encryptedM
        return encryptedM
    
    def prompt(self):
        prompt_value = """
\nAs a public user, what would you like to do?\n
  1. Send an encrypted message.\n
  2. Authenticate a digital signature.\n
  3. Exit.\n
Enter your choice: \r"""
        ans = int(input(prompt_value))
        
        if ans == 1:
            message = input("\nEnter a message: ")
            self.encrypt(message,self.public_key,self.length)
            
        elif ans == 2:
            #this is how we get d
            d = e_gcd(self.e,self.phi)
            d = d[0]
            self.decrypt(self.e_msg,d,self.length)
            
class Public(User):
    def __init__(self):
        super().__init__()
        
    def decrypt(e_msg,d,n):
        finish = ''
        # Decrypt using Fast Modular Exponentiation
        char_to_ascii = [pow(c,d,n) for c in e_msg]
        # Map ASCII code-> char
        d_msg = [chr(x) for x in char_to_ascii]
        for x in d_msg:
            finish += x
        return finish
    
        (x, y, d) = e_gcd(e_gcd.b, e_gcd.a%e_gcd.b)
        return y, x - e_gcd.a//e_gcd.b*y, d
