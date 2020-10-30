users_input = input()
wining_thing = ""
if users_input == "paper":
    wining_thing = "scissors"
elif users_input == "scissors":
    wining_thing = "rock"
elif users_input == "rock":
    wining_thing = "paper"
print("Sorry, but the computer chose " + wining_thing)
