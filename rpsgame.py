def game(b,l):
    if(b>2 or b<0):
        print("enter the number correctly")
    elif(b==2 and l==0):
        print("computer won the game")
    elif(b==2 and l==1):
        print("You won the game")
    elif(b<l):
        print("computer won the game")
    elif(b>l):
        print("you won the game")
    elif(b==l):
        print("the match is draw")
    else:
        print("enter the valid number")


import random
a=int(input("enter the no of time you have to play: "))
l1=[0,1,2]
print("enter the stone as 0")
print("enter the paper as as 1")
print("enter the scissor as as 2")
for x in range(a):
    b=int(input("Enter your weapon"))
    l=random.choice(l1)
    if(l==0):
        print("computer said stone")
    elif(l==1):
        print("computer said paper")
    else:
        print("computer said scissor")
    s=game(b,l)
print("the have over")
    
