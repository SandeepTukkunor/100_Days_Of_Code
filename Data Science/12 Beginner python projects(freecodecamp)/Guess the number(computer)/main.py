import random 

def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:

        guess = int(input(f"please enter a number between 1 and {x}"))
        if guess < random_num:
            print("sorry Guess again, the value is too low")

        elif guess > random_num:
            print("the number is too high, Guess again")
        
    print("yey! you have guessed it correctly , Congrats")


        

guess(10)


