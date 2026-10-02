# Logic of range
number=range(20)
print(number)
# agar 1 to 19 chahiye
range(1, 20)
# agar step me chahiye
range(start=0,stop=3,step=1)#koi bhi value de sakte he but by deffoult start=0 and step=1


# WHILE LOOP 
i=1
while i <=10:
    print (i*"radhekrishna")# can not difine i+=1 when code is exsist of the infinite and output traingel me aayega
    i +=1

#FOR LOOP
num=range(6)#0 to 5 num
for i in num:
    print(i)
for i in range (1,100006):
    print(i)

# print the even number
for i in range(1,101):
    if i%2==0:
        print(i)
 #DIRECT KAR SAKTE HE       
for i in range(2,201,2):
    print(i)

#Break and continue
for i in range(1,51):# maltiples of 3 (1 to 50)
    if(i==18):
      
        break
    if(i%3==0):  #break  keybord ka use karke loop  se bahar nikal jate he                         
       print(i)
print("out of loop")

for i in range(1,51):# maltiples of 3 (1 to 50)=>18 skip
    if(i==18):
      
       continue
    if(i%3==0):  # use the continue  keybord print all number but skip only 18 number                        
       print(i)
print("out of loop")


