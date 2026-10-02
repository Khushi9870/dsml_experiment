#ARETHMETIC OPERATORS
print(6+3)
print(6-3)
print(6*3)
print(6/3)
print(6//3)
print(6%3)
print(6**3)

#assignment operator
x=1
#x=x+6 # answer is 7
x +=6 #(aise hi use kar sakte he %=,-=,/= )
print(x)
#OPERATORS PRECEDENCE
answer=3+5*4
print(answer)#agar answer 32 chahiye to perenthisis ka use karege

#COMPARISON OPERATORS
# >,<,<=,>=,==,!=
print(10<5)
print(10>5)
print(10>=5)
print(10<=5)
print(10==10)
print(10!=10,10!=5)

#LOGICAL OPERATOR
# and OPERATOR
print(19>20 and 19<20)
print(19<20 and 18>16)
print(4==4 and 3==3)
# or OPERATOR
print(19>20 or 19<20)
print(19>20 or 38<20)
print(3==5 or 4<6)

# not OPERATOR
print( not 19>20 )
print( not 19<20 )
print(not True )
print(not False )

# condisational statement
age=16
if age >=118:
    print("you can an adult")
    print(" you can drive car")
    print("you are gave the vote")
elif age < 18 : 
    print("you can not a vote and drive")
marks=30
if marks>=80:
    print('A')
elif marks <80 and marks>=60:
    print('B')
elif marks<60:
    print("fail")