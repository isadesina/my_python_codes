import random
""" THIS SCRIPT IS A GAME OF NUMBER GUESS"""

rand_no = random.randint(100,1000)  # This line generates the random

user_guess = None  # the initial value of user guess is None
# user_guess = int(input("Enter a number between 100 and 10000"))


while user_guess != rand_no:  # the next lines o code will only run if the condition after the "while" remains true
    user_guess = int(input("Guess a number between 100 and 1000"))
    if user_guess > rand_no:
        print("The number is higher than what you guessed. Guess lower")
 you
    if user_guess < rand_no:
        print("The number is lower than what you guessed. Guess higher")

    elif user_guess == rand_no:
        print("Good job. you guesssed correctly")
        print("\n The number is {}".format(rand_no))
        break





