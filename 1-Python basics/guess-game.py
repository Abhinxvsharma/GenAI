import random

def welcome():
  print("\n welcome to guess the number game!")
  print(" i am thinking of a number between 1 and 100")

def get_guess():
  while True:
    try:
      return int(input("Enter your guess: "))
    except ValueError:
      print("please enter valid number")

def check_guess(guess, secret):
  if guess < secret:
    return " too low!"
  elif guess > secret:
    return "too high!"
  else:
    return " correct"
  
def play_game():
  secret = random.randint(1, 100)
  attempts = 0
  max_attempts = 10


  welcome()

  while attempts < max_attempts:
    guess = get_guess()
    attempts += 1

    result = check_guess(guess, secret)
    print(result)


    if result == "correct" :
      print(f"you guessed it in {attempts} attempts!")
      break

  else:
    print(f"out of attempts! the number was {secret}")


def main():
  while True:
    play_game()
    again = input("play again? (y/n): ").lower()
    if again != 'y':
      print("thanks for playing! ")
      break

main()

