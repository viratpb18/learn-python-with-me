a = int(input("enter your age:"))
# if statement1
if (a%2==0):
    print("the number is even")
# if statement 2
if a>=18:

    print("you are eligibile to vote")         #indentation space is given after if and else so that it is clear that next line is if
elif a<0:
    print('daru peeke mat dekho mera program')

else:
    print("you are not eligible to vote")
    print("years after which u will be able to vote is:",18-a)