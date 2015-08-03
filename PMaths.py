# -*- coding: utf-8 -*-
#!/usr/bin/python

# @author Mohamed rashad

import sys
import math
import binascii

from math import *
from sys import *
from decimal import *

##########################

def calc(n):

    t= Decimal(0)
    pi = Decimal(0)
    deno= Decimal(0)
    k = 0

    for k in range(n):

        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)  
                                 
    pi = pi * Decimal(12)/Decimal(640320**(1.5))
    pi = 1/pi

    return pi


##########################


def generate_pascal_triangle(rows):
    if rows == 1: return [[1]]

    triangle = [[1], [1, 1]] # pre-populate with the first two rows

    row = [1, 1] # Starts with the second row and calculate the next

    for i in range(2, rows):
        row = [1] + [sum(column) for column in zip(row[1:], row)] + [1]
        triangle.append(row)

    return triangle

##########################
while True:



    print "\n\n   ~~~~~~~~~~~~~~~~~~ PMaths Tool (Ultimate Python Maths App) ~~~~~~~~~~~~~~~~~~~"

    print "\n Would you like to do..?\n\t1-check even or odd\n\t2-check prime number or not\n\t3-Check Divisbility\n\t4-Check golden ratio\n\t5-Compute Factorial\n\t6-Compute Fibonacci series\n\t7-Compute Pi (Limit 10 million)\n\t8-Encode Text \n\t9-Decode To text"

    print "\n Choose your Option:"

    Input = raw_input("> ")

##########################

    if Input == "1":

        print "\n Enter Desired Number Here"

        Input2 = int(raw_input("> "))

        if Input2 %2 != 0: 
            print "Your input is odd"
        else:
            print "Your number is even"

##########################


    elif Input == "2":
        
        print "\n Enter Desired number Here"
        Input2 = int(raw_input("> "))

        if Input2 > 1:

            for i in range(2, Input2 + 1):

                if Input2 % i == 0 and i != Input2 and i != 1:

                    print "This is not a Prime Number"

                else:

                    print "This is a Prime Number"

        else:
            print "This is not a Prime Number"

##########################

    elif Input == "3":

        print "\n Enter Desired Number Here"

        Input2 = int(raw_input("> "))


        print "\n Enter number to be divided with"

        Input4 = int(raw_input("> "))



        if Input2 %Input4 != 0: 
            print "\n Your input is not divisible by %r" %Input4
        else:
            print "\n Your input is divisible by %r" %Input4


##########################


    elif Input == "4":


        print "\n insert first number (must be larger than the second)"

        n = float(raw_input("> "))

        print "\n insert second number"

        m = float(raw_input("> "))

        if m > n:

            print "\n insert numbers correctly and try again"
            print "\n\n insert first number (must be larger than the second)"

            n = float(raw_input("> "))

            print "\n insert second number"

            m = float(raw_input("> "))     
        
        else:

            
            T = n/m
            Q = float("{0:.1f}".format(T))
     
            if Q > 1.6 and Q < 1.7:

                print "\n Golden Ratio exists between these 2 digits (approximately)"

            else:

                print R
                print T
                print "\n Golden Ratio  doesn't exist between these 2 digits"   

    

##########################

    elif Input == "5":

        print "\n insert a number (integer only)"
        n = int(raw_input("> "))

        print str(math.factorial(n))

##########################

    elif Input == "6":

        print "\n How many terms to generate?"

        x = int(raw_input("> "))
        a = [0,1]

        for n in range(1,x):

            a.append(a[n]+a[n-1])
            print a[-1]

    elif Input == "7" :
        print "\n How many digits of pi to generate ? (limit 10 million)"
        n = int(raw_input("> "))
        print "\n"
        print "\n"

        print "Pi = " + str(calc(n))

##########################


    elif Input == "8" :
        print "\n Choose conversion type\n\t1-Binary\n\t2-Octal\n\t3-Hex "
 
        n = raw_input("> ")
        if n == "1" :
            print "\n Enter Text"
            mm = raw_input("> ")
            print  str(bin(int(binascii.hexlify(mm), 16))).replace("0b" , "")

        elif n == "3" :
            print "\n Enter Text"
            mm = raw_input("> ")
            print  str(":".join("{:02x}".format(ord(c)) for c in mm))

        elif n == "2" :
            print "\n Enter number"
            mm = int(raw_input("> "))
            print  str(oct(mm))



##########################


    elif Input == "9" :
        print "\n Choose conversion type\n\t1-Binary\n\t2-Hex "
 
        n = raw_input("> ")
        if n == "1" :
            print "\n Enter Binary"
            mm = raw_input("> ")
            x = int( mm , 2)
            print  binascii.unhexlify('%x' % x)


        elif n == "3" :
            print "\n Enter Hex"
            mm = raw_input("> ")
            print  mm.decode('hex')


##########################

    elif Input == "10" :
            print "\n How many rows of pascal's triangle to generate ? (limit 10 million)"
            mm = int(raw_input("> "))

            for row in generate_pascal_triangle(mm):
                print row




