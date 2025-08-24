import random
possible_choices = ["rock", "paper", "scissors"]
enemy = random.randint(0, 2)

icon_choices = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''','''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

user_choice = input("What do you choose? Rock, Paper or Scissors?").lower()

if user_choice == "rock":
    print("Player 1\n")
    print(icon_choices[0])
    print("Player 2\n")
    print(icon_choices[enemy])
    if user_choice == "rock" and possible_choices[enemy] == "rock":
        print("It's a draw")
    elif user_choice == "rock" and possible_choices[enemy] == "paper":
        print("You lost")
    elif user_choice == "rock" and possible_choices[enemy] == "scissors":
        print("You won")

if user_choice == "paper":
    print("Player 1\n")
    print(icon_choices[1])
    print("Player 2\n")
    print(icon_choices[enemy])
    if user_choice == "paper" and possible_choices[enemy] == "paper":
        print("It's a draw")
    elif user_choice == "paper" and possible_choices[enemy] == "scissors":
        print("You lost")
    elif user_choice == "paper" and possible_choices[enemy] == "rock":
        print("You won")

if user_choice == "scissors":
    print("Player 1\n")
    print(icon_choices[2])
    print("Player 2\n")
    print(icon_choices[enemy])
    if user_choice == "scissors" and possible_choices[enemy] == "scissors":
        print("It's a draw")
    elif user_choice == "scissors" and possible_choices[enemy] == "rock":
        print("You lost")
    elif user_choice == "scissors" and possible_choices[enemy] == "paper":
        print("You won")