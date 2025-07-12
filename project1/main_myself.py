import random

choices = {
    "stone":1,
    "paper":0,
    "scissor":-1
    }
forcomputer = {1,-1,0}
a = input("enter your choice in stone paper and scissors:  ")
yourchoice = choices[a]

compchoice = random.choice(list(forcomputer))

if compchoice==1:
    print("computer choose stone")
elif compchoice ==0:
    print("computer choose paper")
else:
    print("computer choose scissors")




print("you choose", a)
def game():
    if compchoice == yourchoice:
        print("the match is drawn")
       
        
    elif compchoice ==1 and yourchoice==0:
        print("you won")
    elif compchoice ==0 and yourchoice==1:
        print("you lost")
    elif compchoice ==1 and yourchoice==-1:
        print("you lost")
    elif compchoice ==-1 and yourchoice==1:
        print("you won")
    elif compchoice ==-1 and yourchoice==0:
        print("you lost")
    elif compchoice ==0 and yourchoice==-1:
        print("you won")
   
    


print(game())

