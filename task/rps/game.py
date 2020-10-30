import random

options = ('rock', 'paper', 'scissors')
user_choice = ""
computer_choice = ""
is_game_stopped = False


def find_and_print_result():
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


def game_turn(choice):
    global user_choice
    global computer_choice
    user_choice = choice
    computer_choice = random.choice(options)
    find_and_print_result()


while not is_game_stopped:
    command = input()
    while command not in options and not command == "!exit":
        print("Invalid input")
        command = input()
    if command == "!exit":
        print("Bye!")
        is_game_stopped = True
    else:
        game_turn(command)
