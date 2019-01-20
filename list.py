# practive list in python 
# list ,
list = ["duc" , "chun" , "OK"]
list.append("OK appped run")
list.insert(2 , "index 2 add success")
for item in list:
    print item + "   index is"+str(list.index(item))
# tuple
# tuple not change value 
tuple =  ("duc" , "chun", "tuple")
#set
# Note: Sets are unordered, so the items will appear in a random order.
set = {"duc" , "chun" , "set"}

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
myIter = iter(list)

print(next(myIter))
print(next(myIter))
print(next(myIter))

