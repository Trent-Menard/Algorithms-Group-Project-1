# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:34:17 2022

@authors: Trent Menard, Ryan Hasty, Matt Wagers
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

# Extended Euclidean Algorithm to calculate d
def e_gcd(a = 1, b = 1):
    if b == 0:
        return (1, 0, a)
    (x, y, d) = e_gcd(b, a%b)
    return y, x - a//b*y, d

# These have to be declared outside of the constructor because otherwise each
# time a child would try to acess the parent's class attrbutes it would call
# the parent constructor, ultimately generating different values for the child
tmp_p_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
tmp_q_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)

# If p_val is not prime, generate another p_val
while not FermatPrimalityTest(tmp_p_val):
    tmp_p_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
    
    # If q_val is not prime, generate another q_val
    while not FermatPrimalityTest(tmp_q_val):
        tmp_q_val = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
    
    n = tmp_p_val * tmp_q_val
    tmp_phi = (tmp_p_val - 1) * (tmp_q_val - 1)
    e = random.randint(1, tmp_phi)
    
    # Generate random e (public key) using Euclid's algorithm until its relatively prime to phi
    while not math.gcd(e, tmp_phi) == 1:
        e = random.randint(1, tmp_phi)
        
class User:
    
    def __init__(self):       
        self.public_key = e
        self.length = n
        self.phi = tmp_phi
        self.encrypted_messages = []
        self.digital_signatures = []
            
class Public(User):

    def __init__(self):       
        super().__init__()
        
    def encrypt(self, message, e, n):
        upper_msg = message.upper()
        char_to_ascii = [ord(x) for x in upper_msg]
        # Encrypt each ASCII code using Fast Modular Exponentiation with Public Key
        encryptedM = [pow(m, e, n) for m in char_to_ascii]
        
        self.encrypted_msg = encryptedM
        print("Encrypted Message: " + str(self.encrypted_msg))
        
        self.encrypted_messages.append(encryptedM)
        return encryptedM

class Private(User):
    def __init__(self):       
        super().__init__()
        self.d = e_gcd(self.public_key, self.phi)[0]%self.phi
        
    def decrypt(self, e_msg, d, n):
        finish = ''
        # Decrypt using Fast Modular Exponentiation
        char_to_ascii = [pow(c, d, n) for c in e_msg] 
        # Map ASCII code-> char
        d_msg = [chr(x) for x in char_to_ascii]
        for x in d_msg:
            finish += x
            
        print(finish)
        return finish
    
        #(x, y, d) = e_gcd(e_gcd.b, e_gcd.a%e_gcd.b)
        #return y, x - e_gcd.a//e_gcd.b*y, d
    
    def sign_message(self, sig_msg, d, n):
        upper_msg = sig_msg.upper()
        char_to_ascii = [ord(x) for x in upper_msg]
        signed = [pow(m, d, n) for m in char_to_ascii]
        print(signed)
        return signed
