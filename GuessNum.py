
import random 

# print ("This program will generate a random number in a given number range. ")
# print ("Then the user, you, will be given unlimited tries to guess the right number. ")
# print ()
# min = input ("Please enter the minimum number for the range: ")
# max = input ("Please enter the maximum number for the range: ")

# RNG (min, max)

# function RNG that takes in min/max inputs and chooses a random num
def RNG (min , max):
    randomNum = random.randint (min , max )
    # return randomNum
    print (randomNum)

def main ():
    print ("This program will generate a random number in a given number range. ")
    print ("Then the user, you, will be given unlimited tries to guess the right number. ")
    print ()
    min = int (input ("Please enter the minimum number for the range: "))
    max = int (input ("Please enter the maximum number for the range: "))

    RNG (min, max)

if __name__ == "__main__":
    main ()
