import random

options = ('rock', 'paper', 'scissors')
user_choice = ""
computer_choice = ""
is_game_stopped = False
score_file = open("rating.txt", mode="r+t")
file_content = ""
user_score = 0


def find_and_print_result():
    global user_score
    if user_choice == computer_choice:
        print(f"There is a draw ({user_choice})")
        user_score += 50
    else:
        user_choice_number = options.index(user_choice)
        computer_choice_number = options.index(computer_choice)
        user_wins = user_choice_number == (computer_choice_number + 1) % 3
        if user_wins:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
        else:
            print(f"Sorry, but the computer chose {computer_choice}")


def game_turn(choice):
    global user_choice
    global computer_choice
    user_choice = choice
    computer_choice = random.choice(options)
    find_and_print_result()


def get_information():
    global file_content
    global user_score
    file_content = score_file.readlines()
    for line in file_content:
        if user_name in line:
            line = line.replace("\n", "")
            _, user_score = line.split()
            user_score = int(user_score)


user_name = input("Enter your name: ")
print(f"Hello, {user_name}")
get_information()
while not is_game_stopped:
    command = input()
    while command not in options\
            and not command == "!exit"\
            and not command == "!rating":
        print("Invalid input")
        command = input()
    if command == "!exit":
        print("Bye!")
        is_game_stopped = True
    elif command == "!rating":
        print(f"Your rating: {user_score}")
    else:
        game_turn(command)
score_file.close()
