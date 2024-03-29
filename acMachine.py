# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
A four-pole generator has 500 conductors on the armature. If
the generator is running at 1200 rpm, find the average
voltage generated between brushes for (a) a lap winding,
(b) a wave winding. The total flux per pole is 10^6 lines.

"""

speed =int(input("Enter speed in rpm:\n"))
p = int(input("Enter number of poles:\n"))
z = int(input("Enter number of conductors:\n"))
phi = int(input("Enter flux per pole in lines:\n"))*(10**-8)
a_lap = p
a_wav = 2
e_lap = e_wav = 0

# we need to find the average voltage generated by machine
#
#       phi*z*speed*p
#  E =  -------------
#           60*a

def cal_e_lap_wave():
    e_lap = (phi*z*speed*p)/(60*a_lap) # Mathematical modelling of basic voltage output
    e_wav = (phi*z*speed*p)/(60*a_wav) # Same as above :p
    print(e_lap , "V is the voltage between brushes @ lap")
    print(e_wav , "V is the voltage between brushes @ wave")

cal_e_lap_wave()




