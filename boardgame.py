# created a board game using python

# create a list of tuples with player names and their starting positions
players = [("Player 1", 0), ("Player 2", 0), ("Player 3", 0), ("Player 4", 0)]

# define the board size and number of rounds to play
board_size = 20
num_rounds = 10

# define a function to roll the dice and return a random number between 1 and 6
import random
def roll_dice():
    return random.randint(1, 6)

# define a function to move a player's piece and update their position in the list
def move_player(player, steps):
    name, position = player
    new_position = position + steps
    if new_position > board_size:
        new_position = board_size
    print(name, "moves from", position, "to", new_position)
    return (name, new_position)

# play the game for a fixed number of rounds
for i in range(num_rounds):
    print("Round", i+1)
    # allow each player to take a turn
    for player in players:
        name, position = player
        steps = roll_dice()
        print(name, "rolls a", steps)
        player = move_player(player, steps)
        # update the player's position in the list
        players[players.index((name, position))] = player
    print("")

# print the final positions of all players
print("Final positions:")
for player in players:
    print(player[0], "is at position", player[1])
