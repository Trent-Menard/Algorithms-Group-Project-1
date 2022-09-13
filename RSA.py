# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:37:11 2022

@author: Trent
"""

import math

class PublicUser:
    public_key = ""
    private_key = ""
    
# How to choose/generate parameters for pow() to get p & q?
# base, power, %
p_val = pow(30192, 43791, 65301)
q_val = pow(30192, 43791, 65301)
public_key = 0;
phi = 0;
e = 0;

for x in range(phi):
    if math.gcd(x, phi) == 1:
        x = e;
        break
