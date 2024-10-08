import random

def roll():
    min_value = 1
    max_value = 6
    result = random.randint(min_value, max_value)
    return result

def print_separator():
    print("\n" + "-"*30 + "\n")
def print_separator_space():
    print("\n")

# Input number of players
while True:
    players = input("Enter the number of Players (2-6): ")
    if players.isdigit():
        players_num = int(players)
        if 1 < players_num <= 6:
            break
        else:
            print_separator()
            print("Number of players must be between 2 and 6. Please try again.")
    else:
        print_separator()
        print("Invalid input. Please enter a number.")

print_separator()

# Input target sum
target_sum = int(input("Enter the target Sum: "))
initial_score = [0 for _ in range(players_num)]
found = False

# Game loop
while not found:
    for i in range(len(initial_score)):
        print_separator()
        print(f"Player {i + 1}'s turn starts now!")
        current_score = 0
        
        while True:
            print_separator_space()
            roll_perm = input("Would you like to roll the dice (y/n): ").strip().lower()
            if roll_perm == 'y':
                value = roll()

                if value == 1:
                    print(f"You rolled a 1! Your turn is over.")
                    initial_score[i]-=current_score
                    current_score = 0
                    break
                else:
                    print(f"You rolled the dice and got {value}.")
                    current_score += value

                # Adding current turn score to player’s total score
                initial_score[i] += value

                # Check if player has won
                final_score = max(initial_score)
                if final_score >= target_sum:
                    found = True
                    winning_idx = initial_score.index(final_score)
                    print_separator()
                    print(f"Player {winning_idx + 1} wins with a total score of {final_score}!")
                    break
                print_separator_space()
                print(f"Your current score for this turn is {current_score}.")
            else:
                break
        if found:
            break
        else:
            print_separator()
            print(f"Player {i + 1}'s total score is {initial_score[i]}.")
