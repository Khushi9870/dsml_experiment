#type conversion and type casting
age=input("enter the age: ")
age=int(age)
new_age=int(age)+1
print(new_age)
print(float(new_age))#implicit(automaticaliy)
print(1+int(3.9999))#explicit(programer karta he ye casting)
#sum program=>a,b=>sum
a=int(input("Enter=a:"))
b=int(input("Enter=b:"))
sum=a+b
print(sum)
#string operation
name="amit yadav"
grade='A'
print(name.upper())
print(name)
#find()function is return of the index (index in are position)
print(name.find("it"))
#replace()function
print(name.replace("amit yadav","rinku yadav"))
print(name.replace("yadav","ji"))
#check of the presence through the in keybord and return the boolean value
print('a'in name)#True
