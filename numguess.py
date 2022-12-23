import random
inte=random.randint(1,10)
guess=0
for i in range(7):
    num=int(input("Enter a number between 1 & 10:\n"))
    if num==inte:
        guess+=1
        print(f"You Have Guessed the Number Correctly i.e {inte}")
        break
    elif num>=inte:
        guess+=1
        print("Your Guess is too High, Please Enter a Lower Number")
    elif num<=inte:
        print("Your Guess is too Low, Please Enter a Higher Number")
        guess+=1
print(f'You took {guess} attempts to guess the number')
if guess>=7:
    print("You Have Exceeded the Number of attempts")

