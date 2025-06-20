import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
players_scores = [0 for _ in range(players)] # say put 0 for all players in list


while max(players_scores) < max_score:
        for player_idx in range(players):
            print("\nPlayer number", player_idx + 1, "turn has just started!")
            print("Your total score is:", players_scores[player_idx], "\n")
            current_score = 0


            while True:
                shou_roll = input("Do you want to roll? (y/n): ").lower()
                if shou_roll != 'y':
                    break
                
                value = roll()
                if value == 1:
                    print("You rolled a 1! You lose all your points.")
                    current_score = 0
                    break
                else:
                    print("You rolled a ", value)
                    current_score += value
                    print("Current score : ", current_score)
            
        players_scores[player_idx] += current_score
        print("Your total score is:", players_scores[player_idx])

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)

    

