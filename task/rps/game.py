import random


options = ('rock', 'paper', 'scissors')
user_choice = input()
computer_choice = random.choice(options)
if user_choice == computer_choice:
    print(f"There is a draw ({user_choice})")
else:
    user_choice_number = options.index(user_choice)
    computer_choice_number = options.index(computer_choice)
    user_wins = user_choice_number == (computer_choice_number + 1) % 3
    if user_wins:
        print(f"Well done. The computer chose {computer_choice} and failed")
    else:
        print(f"Sorry, but the computer chose {computer_choice}")
