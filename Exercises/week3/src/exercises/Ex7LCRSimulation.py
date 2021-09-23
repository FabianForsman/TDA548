# package exercises

#
#  Simulation of LCR game. See, https://www.wikihow.com/Play-LCR
#
from typing import List
from random import randrange

# ------- Class to hold player data -----------
class Player:
    def __init__(self, name: str, chips: int):
        self.name = name
        self.chips = chips


def lcr_program():
    # test()    # < --- Uncomment to run tests ---

    # Hard coded data
    players: List[Player] = [Player("Fabbo", 3),
                             Player("Krysset", 3),
                             Player("Sonic", 3)]
    current: Player = players[0]
    pot = 0
    print("Simulation starts")
    display_players(players)

    while not check_win(players):
        for i in range(current.chips):
            roll(current, players)
        current = right_player(current, players)
        
    # ---- Logical methods -----------------
def check_win(players: List[Player]):
    tot = 0
    for player in players:
        tot += player.chips
    for player in players:
        if tot == player.chips:
            return winner(player)


def winner(player: Player):
    print(str(player.name) + " wins with " + str(player.chips) + " chips left!")
    return True


def roll(actual: Player, players: List[Player]):
    rand = randrange(0,6)
    if rand == 4:
        move_chip(actual, "L", players)
    elif rand == 5:
        move_chip(actual, "C", players)
    elif rand == 6:
        move_chip(actual, "R", players)
    else:
        move_chip(actual, "Dot", players)


def move_chip(actual: Player, result: str, players: List[Player]):
    if result == "L":
        left_player(actual, players).chips += 1
    if result == "R":
        right_player(actual, players).chips += 1
    if result == "Dot":
        actual.chips += 1
    actual.chips -= 1
    display_state(actual, result, players)


def left_player(actual: Player, players: List[Player]):
    player_index = players.index(actual)
    if player_index == 0:
        return players[2]
    return players[player_index-1]


def right_player(actual: Player, players: List[Player]):
    player_index = players.index(actual)
    if player_index == 2:
        return players[0]
    return players[player_index+1]


# --- IO methods ------------------
def display_state(actual: Player, result: str, players: List[Player]):
    print(actual.name + " got ", end='')
    print(result)
    display_players(players)


def display_players(players: List[Player]):
    for player in players:
        print(player.name + ": " + str(player.chips))
    

    
# ********************** Testing *************************************''
def test():
    # Local hard coded test data
    players = [Player("1", 1), Player("2", 2), Player("3", 3)]

    # TODO Testing
    exit(0)


if __name__ == "__main__":
    lcr_program()
