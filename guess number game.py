from random import randint
num = randint(1,20)
count = 0
answer = input("Pick a number between 1 and 20.")
if answer > num:
    print("Go lower.")
elif answer < num:
    print ("Go higher.")
elif answer == num:
    print ("Correct!")
