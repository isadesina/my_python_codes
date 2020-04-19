import random

random_no = random.randint(100,1000)

user_guess = None

while user_guess != random_no:
    user_guess = int(input("please enter a number between 100 ans 1000"))
    if user_guess > random_no:
        print("too high, try again")
    elif user_guess < random_no:
        print("too low, try again")
    elif user_guess == random_no:
        print ("correct...good job!")
