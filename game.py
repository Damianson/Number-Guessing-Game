import random
import string

def game():
    choices = input("Choose your difficulty level:\n 1. Input 1 for 'Easy'\n 2. Input 2 for 'Medium'\n 3. Input 3 for 'Hard'\n")
    number = random.randint(1,10)
    numberOne = random.randint(1,20)
    numberTwo = random.randint(1,50)


    def diff(c,b,number):
        print("Guess a number from 1-" + str(b) + "\nYou have " +  str(c) + " tries\n")
        
        while True:
            guess = input("Guess the number: ")

            if guess.isdigit():
                if int(guess) != number:
                    c = c - 1
                    print("That was wrong\nYou have " + str(c) + " tries left\n")
                    if c == 0:
                        print("Game Over!")
                        exit(0)
                else :
                    print("You got it right!")
                    exit(0)
            else:
                print("Please input only a number")
                diff(c,b,number)

    if choices == '1':
        diff(6,10,number)
    elif choices == '2':
        diff(4,20,numberOne)
    elif choices == '3':
        diff(3,50,numberTwo)
    else:
        print("Please Choose a valid response\n")
        game()

game()
