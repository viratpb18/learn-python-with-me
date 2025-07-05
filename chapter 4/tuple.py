a =("rohan","sohan", 1 , 2 , 4.7 , False)
print(type(a))     #tuple is an immutable type of list.   () is used in tuple instead of [] to distinguish it from lists
print(a)
# a[0] = 453       #it is an error because tuple is immutable and cant be changed


no =a.count(2)   #cpunts the no of 2
print(no)


i = a.index(2)    #tells the index of 2
print(i)

#tuples are immutable and the values cant be changed but new tuples from existing can be made

print(len(a))   # prints no of data in the tuple