
import random 

def range ():
  # program asks user to input a number for min and max so that it can create the range of numbers within those values
  min = int (input ("Please enter the minimum number for the range: "))
  max = int (input ("Please enter the maximum number for the range: "))
  # while loop checks to see if user inputs a value for max that is less than the min or equal to it.
  # then prompts user that that is not a valid max value and asks user to input a new max value
  while (max < min or max == min):
    if (max < min):
      print ("The maximum number can not be smaller than the minimum. Try again...")
      max = int (input ("Please enter the maximum number for the range: "))
    elif (max == min):
      print ("The maximum number should not equal the minimum so a range can be generated. Try again...")
      max = int (input ("Please enter the maximum number for the range: "))
  return min, max

def rng (min , max):
  # rng () func takes in min, max values and uses imported random library to generate a random number within the range and returns the random num
  random_num = random.randint (min , max)
  return random_num
  
def guess (min, max, random_num):
  # program asks user to try and guess the random number 
  user_guess = int (input ("Try to guess the random number: "))  
  # while loop checks to see if user's guess is correct. If not, while loop runs continuously through each if statement
  while (user_guess != random_num):
    # if statement to check if user guesses a number out of range
    if (user_guess < min or user_guess > max):
      print ("Number is out of range! Try again...")
      user_guess = int (input ("Try to guess the random number: "))
    # in case user guesses higher than actual number
    elif (user_guess > random_num):
      print ("Too high! Guess again...")
      user_guess = int (input ("Try to guess the random number: "))
    # in case user guesses lower than actual number
    elif (user_guess < random_num):
      print ("Too low! Guess again...")
      user_guess = int (input ("Try to guess the random number: "))
  # if statement in case user guesses right first try and program prints a congrats message and returns True to show user guessed right
  if (user_guess == random_num):
    print ("Congrats! You guessed the right number! ")
    return True

# main
def main ():
  # beginning text to introduce user to game
  print ("This program will generate a random number in a given number range. ")
  print ("Then the user, you, will be given unlimited tries to guess the right number. ")
  print ()

  # defines min, max and calls the range () func to generate a range with user input values
  min, max = range ()

  # defines random_num and calls rng () func with min, max values to generate a random number
  random_num = rng (min, max)

  # defines user_guess and calls guess () func with min, max, and random_num values 
  user_guess = guess (min, max, random_num)

  # after user guesses correctly, function guess () returns True
  if (user_guess == True):
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
