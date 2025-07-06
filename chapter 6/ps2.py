eng = int(input("enter total marks out of 100 in english: "))
hind = int(input("enter total marks out of 100 in hindi: "))
math = int(input("enter total marks out of 100 in maths: "))
if(eng/100)*100>=33:
    print("you are passed in english")
    print("your percentage in english is",(eng/100)*100)
if(hind/100)*100>=33:
    print("you are passed in hindi")
    print("your percentage in hindi is",(hind/100)*100)
if(math/100)*100>=33:
    print("you are passed in math")
    print("your percentage in math is",(math/100)*100)
    totalmarks = eng + hind + math
    if(totalmarks/300)*100>=40:
        print("congrats you are passed in the exam")
        print("your total percentage is",(totalmarks/300)*100)
    else:
        print("oops you failed in the exam")