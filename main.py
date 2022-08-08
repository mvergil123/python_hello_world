# python guessing game
import random
isCorrectGuess = False
attempts = 1


# get input from user on a number
number = int(input("Please select a number between 1 and 10 "))
while number < 1 or number > 10:
    print("Please enter a number within the range")
    number = int(input("Please enter the number again: "))
    
# have computer guess a number
while not isCorrectGuess: 
    num = random.randint(0,10)
    print(num)

   
    # tell the computer if its right or not
    if num != number:
        print("Sorry, the computer did not guess right.")
        attempts = attempts+1
        isCorrectGuess = False
    else:
        isCorrectGuess = True

    # if right, print "we won"
    if isCorrectGuess == True:
        print("The computer won!")
        print("This is how many tries it took " + str(attempts))
        exit()

