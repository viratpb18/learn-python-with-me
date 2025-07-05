dict = {
    "harry":100,       #it is a dictionary which is very helpful in storing data.it can contain other lists and tuples
    "virat" :0,
    "rohan" :0,
}
print(dict.items())     #prints the items in tuple form

print(dict.keys())     #prints the keys which is the thing present at left hand side

print(dict.values())    #prints the values that is the thing present at left hand side

dict.update({"harry":99,"renuka":100})   #proofs tht dicts are immutable
print(dict.items())

print(dict.get("harry") )    #gives the marks of a person

print(len(dict))