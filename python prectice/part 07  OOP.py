# Class is a bluprint for creating objects
# Creating class
'''class Student:
    name="Amit yadav"
# Creating object (instance)    

s1=Student()
print(s1.name)

s2=Student()
print(s2.name)

# and new example
class Car:
    color="red"
    brabd="mercedes"

Car1 = Car()  
print(Car1.brabd)  
print(Car1.color) 


class Student:
    
    def __init__(self,fulname):
        self.name= fulname
        print("adding new student in database ..")
s1=Student("radhe")
print(s1.name)
s2=Student("radhe")
print(s2.name)

#class and instance attributes
# class Attribute
class Student:
    collage="gpk kanpur"
 # instance attributets   
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

# Creating object        
s1=Student("Khushi",101)
s2=Student("Kittu",105)
print(s1.collage,s1.name,s1.roll_no)
print(s2.collage,s2.name,s2.roll_no)


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum += val
        print("h1", self.name,"your avg scor is",sum/3)

s1=Student("tony stark",[99,98,97])
s1.get_avg()'''

# prectice question==Create account class with 2 attributes-balance & account no.create mathods for debit,credit & printing the balance.
class Account:
    def __init__(self,bal,acc):
        self.balance= bal
        self.account_no = acc
    # debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance=",self.get_balance())

    def credited(self,amount):
         self.balance +=amount
         print("Rs.",amount,"was credited")    
    def get_balance(self):
        return self.balance
        print("total balance=",self.get_balance())

acc1=Account(10000,12345)


acc1.debit(40000)
acc1.credited(500)
acc1.credited(500)