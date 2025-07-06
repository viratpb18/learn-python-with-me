eng = int(input("enter total marks out of 100 in english: "))
hind = int(input("enter total marks out of 100 in hindi: "))
math = int(input("enter total marks out of 100 in maths: "))
totalmarks = eng + hind + math
totalpercent = (totalmarks/300)*100
if (totalpercent>=40 and eng>=33 and hind>=33 and math>=33):
    print("congrats you are passed")
    print("your percentage is,",totalpercent)
else:
    print("you are failed")
    print("your total percentage is", totalpercent)
