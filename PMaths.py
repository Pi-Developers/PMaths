# -*- coding: utf-8 -*-
#!/usr/bin/python

from math import *


while True:

    print "\n\n   ~~~~~~~~~~~~~~~~~~Welcome to PMaths Tool~~~~~~~~~~~~~~~~~~~"

    print "\n Would you like to do..?\n\t1-check even or odd\n\t2-check prime number or not\n\t3-Check Divisbility\n\t4-Check golden ratio"

    print "\n Choose your Option:"

    Input = raw_input("> ")

                               #######

    if Input == "1":

        print "\n Enter Desired Number Here"

        Input2 = int(raw_input("> "))

        if Input2 %2 != 0: 
            print "Your input is odd"
        else:
            print "Your number is even"

                                #######


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

                               #######
    elif Input == "3":

        print "\n Enter Desired Number Here"

        Input2 = int(raw_input("> "))


        print "\n Enter number to be divided with"

        Input4 = int(raw_input("> "))



        if Input2 %Input4 != 0: 
            print "\n Your input is not divisible by %r" %Input4
        else:
            print "\n Your input is divisible by %r" %Input4


                               #######


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
     
            if Q == 1.6:

                print "\n Golden Ratio exists between these 2 digits"
            else:
                print R
                print T
                print "\n Golden Ratio  doesn't exist between these 2 digits"   




        



