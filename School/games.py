# Rock paper scissors game
class Rock:
    def run(self):


        import random

        user_action = input("Enter a choice (rock, paper, scissors): ")
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)

        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")

        elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock destroys scissors! You win!")
            else:
                print("Paper envelops rock! You lose.")

        elif user_action == "paper":
            if computer_action == "rock":
                print("Paper eats rock! You win!")
            else:
                print("Scissors slices paper! You lose.")

        elif user_action == "scissors":
            if computer_action == "paper":
                print("Scissors slits paper! You win!")
            else:
                print("Rock ablidirates scissors! You lose.")

# Random number game
class GuessNum:
    def run(self):
        import random
        number = random.randint(1,10)
        guess = int(input("Guess the number between 1 to 10:  "))
        
        if guess == number:
            print("You guessed the number")
        
        else:
            print("You didn´t guess the number")



