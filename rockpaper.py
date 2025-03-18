import random

# Score tracking
user_score = 0
computer_score = 0
rounds = 0

# Possible choices
choices = ["rock", "paper", "scissors"]

def get_winner(user_choice, computer_choice):
    """Determine the winner based on the game rules."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

print("Welcome to Rock, Paper, Scissors!")
print("Type 'exit' to stop playing.\n")

# Game loop
while True:
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice == "exit":
        print("Final Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        continue

    # Computer makes a choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    result = get_winner(user_choice, computer_choice)
    print(f"Result: {result}")

    # Update score
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    rounds += 1
    print(f"Score: You {user_score} | Computer {computer_score}\n")
