friends = ["rohan", "sohan", 5 ,0, False , "virat"]
print(friends)

friends.append("virat")    #append means adding or inserting a data at the end
print(friends)

# it shows that the strings are immutable whereas lists are very flexible and mutable.
# we can change lists and that will be given to the list and that will be added to the list for the rest of the program

l1 =[2,3,55,33,7,5,47]
l1.sort()    #sorts the numbers in ascending order
print(l1) 


l1.reverse() #opposite of sort
print(l1)

l1.insert(3,33333)      # index number, what you want to insert
print(l1)

value = l1.pop(3)    #prints the no. at  3
print(value)

l1.pop(3)      #removes the value at 3
print(l1)

l1.remove(3)   #remove a data
print(l1)