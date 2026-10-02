# Function define

def sum(a,b):
    print(a + b)
sum(1,2) # function call

pricel=100
new_pricel=pricel+(pricel*0.18)
print(new_pricel)

price2=100
new_price2=price2+(price2*0.2)
print(new_price2)

def calc_gst(price):# price is a parameters
    new_price=price+price*0.18
    print(new_price)
#function call
calc_gst(100)# arguments
calc_gst(2050)

from math import sqrt,log2
print(log2(16))
print(type([1,2,3,4,5]))

import random
print(random.random())  #1 to 1
print(random.randint( 1,10)) 
