p1 = "win 7 crores"
p2 = "you won a lottery"
p3 = "you have won a free iphone 16"
message =input("enter your message: ")


if(p1 in message or p2 in message or p3 in message):     #in gives true or false if the thing entered is present there in a variable
    print("you are a fraud and trying to loot me")
else:
    print("this is not a spam message")