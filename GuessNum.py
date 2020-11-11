
import random 

def range ():
    # takes in min and max nums for the range
    min = int (input ("Please enter the minimum number for the range: "))
    max = int (input ("Please enter the maximum number for the range: "))
    # loop in case user inputs a max num smaller than min and asks to input another max num
    while (max < min or max == min):
        if (max < min):
            print ("The maximum number can not be smaller than the minimum. Try again... ")
            max = int (input ("Please enter the maximum number for the range: "))
        elif (min == max):
            print ("The maximum number should not equal the minimum so a range can be generated. Try again...  ")
            max = int (input ("Please enter the maximum number for the range: "))
    return min, max

def RNG (min , max):
    # random num generator that takes in the user's min and max nums
    randomNum = random.randint (min , max )
    return randomNum
    
def guess (min, max, randomNum):
    # userInput is user's guess
    userInput = int (input ("Try to guess the random number: "))  
    # if user guesses wrong, program loops until the user guesses correctly... 
    while (userInput != randomNum):
        if (userInput < min or userInput > max):
            print ("Number is out of range! Try again... ")
            userInput = int (input ("Try to guess the random number: "))
        else:
            print ("Incorrect! Try again... ")
            userInput = int (input ("Try to guess the random number: "))
    # if user guesses correctly... 
    if (userInput == randomNum):
        print ("Congrats! You guessed the right number! ")
        return True
# main
def main ():
    print ("This program will generate a random number in a given number range. ")
    print ("Then the user, you, will be given unlimited tries to guess the right number. ")
    print ()

    min, max = range ()

    randomNum = RNG (min, max)

    print (randomNum)

    userInput = guess (min, max, randomNum)

    # after user guesses correctly, function guess returns True
    if (userInput == True):
        print ()
        # redo asks whether or not the user would like to play the game again
        redo = input ("Would you like to play again? (y/n): ")
        # while loop in case user inputs anything other than y or n
        while (redo != "y" and redo != "n" ):
            print ("Input either \"y\" for yes or \"n\" for no... ")
            redo = input ("Would you like to play again? (y/n): ")
        if (redo == "y"):
            main ()
        elif (redo == "n"):
            print ("Thanks for playing! ")

if __name__ == "__main__":
    main ()
