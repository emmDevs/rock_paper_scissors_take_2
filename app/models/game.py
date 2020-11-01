from player import Player

class Game():

    def __init__(self, player1, player2):
        self.player1 = Player
        self. player2 = Player 

player1 = Player("Bob", "rock")
player2 = Player("Alice", "scissors")
player3 = Player("Janet", "paper")

def play_game(player1, player2):
    if player1.choice == "scissors" and player2.choice == "paper":
        return  player1.name
    elif player1.choice == "scissors" and player2.choice == "rock":
        return player2.name
    elif player1.choice == "rock" and player2.choice == "scissors":
        return player1.name
    elif player1.choice == "rock" and player2.choice == "paper":
        return player2.name
    elif player1.choice == "paper" and player2.choice == "scissors":
        return player2.name
    elif player1.choice == "paper" and player2.choice == "rock":
        return player1.name
    else:
        return None

# print(player1.name)
# print(player2.name)
# print(player1.choice)
# print(player2.choice)
# print (play_game(player1, player2))
# print(play_game(player3, player1))
