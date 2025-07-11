'''
for n = 3
  *
 ***
*****

'''

num = int(input("enter the number"))
for i in range (1,num+1):
    print(" "*(num-i),end=(""))     #end function says the print on the next line to be executed on the same line
    print("*"*(2*i-1), end =(""))
    print("")

