import random
import shutil


options = ('rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air',
           'paper', 'sponge', 'wolf', 'tree', 'human', 'snake',
           'scissors', 'fire')
chosen_options = ['rock', 'paper', 'scissors']
user_choice = ""
computer_choice = ""
is_game_stopped = False
rating_file = open("rating.txt", mode="r+t")
file_content = ""
user_rating = 0
user_rating_index = 0
file_save_mode = True


def find_and_print_result():
    global user_rating
    if user_choice == computer_choice:
        print(f"There is a draw ({user_choice})")
        user_rating += 50
    else:
        user_choice_number = options.index(user_choice)
        computer_choice_number = options.index(computer_choice)
        user_wins = (user_choice_number - computer_choice_number + len(options)) % len(options) <= int(len(options)/2)
        if user_wins:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_rating += 100
        else:
            print(f"Sorry, but the computer chose {computer_choice}")


def game_turn(choice):
    global user_choice
    global computer_choice
    user_choice = choice
    computer_choice = random.choice(chosen_options)
    find_and_print_result()


def get_information():
    global file_content
    global user_rating
    global user_rating_index
    file_content = rating_file.readlines()
    for i in range(0, len(file_content)):
        line = file_content[i]
        if user_name in line:
            line = line.replace("\n", "")
            _, user_rating = line.split()
            user_rating = int(user_rating)
            user_rating_index = i
            break
    else:
        user_rating_index = len(file_content)
        file_content[len(file_content)-1] += "\n"
        file_content.append("")


def get_options():
    global chosen_options
    user_options = input()
    if not user_options == "":
        chosen_options = user_options.split(",")
    chosen_options = tuple(chosen_options)
    print("Okay, let's start")


user_name = input("Enter your name: ")
print(f"Hello, {user_name}")
get_information()
get_options()
while not is_game_stopped:
    command = input()
    while command not in chosen_options \
            and not command == "!exit" \
            and not command == "!rating":
        print("Invalid input")
        command = input()
    if command == "!exit":
        print("Bye!")
        is_game_stopped = True
        rating_file.close()
        if file_save_mode:
            one_time_file = open("temp.txt", mode="w")
            file_content[user_rating_index] = user_name + " " + str(user_rating) + "\n"
            one_time_file.writelines(file_content)
            one_time_file.close()
            shutil.move("temp.txt", "rating.txt")
    elif command == "!rating":
        print(f"Your rating: {user_rating}")
    else:
        game_turn(command)
