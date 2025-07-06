username = input("enter your username")
if (len(username) == 10):
    print("your username contains 10 characters")
elif (len(username) <10):
    print("your username contains less than 10 characters")
else:
    print("your username contains more than 10 characters")
