# LIST is a mutable data tyoe
markas=[80,90,85,95,75,]

print(markas,type(markas))
#length
print(len(markas))
# index
print(markas[-1])
print(markas[3])
# slicing a list - list(star:end)
print(markas[0:3]) 
markas.append(50)# appaend is add value last and insert is add valuein  staeting
print(markas)
#  insert is add valuein  starting but index dena hoga jis jis place par add karni he
markas.insert(1,100)
print(markas)
markas.clear()
print(markas,len(markas))

#TUPLE-IMMUTABLE DATA TYPE
markas=(80,90,85,95,95,95,75,85, 85 ,75)
print(markas,type(markas))
print(markas[3])
print(markas.index(95))
print(markas.count(75))

# set=> unique items collection
markas={98,96,94,65,98,98,98}
print(len(markas))

for score in markas:
    print(score)

# Dictionary is a collection of keybord(key=>value)unique .
marks={"math":90, "chemistry":88, "physics": 95}
print(marks,type(marks))
print(marks["physics"])# return the esect value in physics keybord
marks["physics"]=100        # change the value in physics
print(marks["physics"])     
marks["english"] =70        # add the english subject and value
print(marks["english"])

# use the for loop
marks={"math":90, "chemistry":88, "physics": 95}
for key in marks:
    print(key,marks[key])
