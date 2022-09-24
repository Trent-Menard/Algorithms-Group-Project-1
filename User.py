# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:34:17 2022

@author: Trent, Ryan, Matt
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

def gen_vals():
    p = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
    q = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
    
    # If p_val is not prime, generate another p_val
    while not FermatPrimalityTest(p):
        p = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
        
    # If q_val is not prime, generate another q_val
    while not FermatPrimalityTest(q):
        q = random.randint(MIN_PRIME_NUMBER, MAX_PRIME_NUMBER)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(1, phi)
    
    # Generate random e (public key) using Euclid's algorithm until its relatively prime to phi
    while not math.gcd(e, phi) == 1:
        e = random.randint(1, phi)
        
    return e,n,phi
            


def encrypt(message, e, n):
    upper_msg = message.upper()
    char_to_ascii = [ord(x) for x in upper_msg]
    # Encrypt each ASCII code using Fast Modular Exponentiation with Public Key
    encryptedM = [pow(m, e, n) for m in char_to_ascii]
    return encryptedM
    
def decrypt(e_msg, d, n):
    finish = ''
    # Decrypt using Fast Modular Exponentiation
    char_to_ascii = [pow(c, d, n) for c in e_msg]
    # Map ASCII code-> char
    d_msg = [chr(x) for x in char_to_ascii]
    for x in d_msg:
        finish += x
    return finish

def sign_message(sig_msg, d, n):
    char_to_ascii = [ord(x) for x in sig_msg]
    signed = [pow(m, d, n) for m in char_to_ascii]
    return signed

def authenticate(signed_msg,e,n):
    finish = ''
    # Decrypt using Fast Modular Exponentiation
    char_to_ascii = [pow(s, e, n) for s in signed_msg]
    # Map ASCII code-> char
    d_msg = [chr(x) for x in char_to_ascii]
    for j in d_msg:
        finish += j
    return finish
