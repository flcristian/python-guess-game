import random
import json


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


def readlog(players) -> None:
    with open("D:/python/basics/firstproject/log.json", 'r') as file:
        json_data = json.load(file)

    if len(json_data) > 0:
        for item in json_data:
            name = item["name"]
            score = item["score"]
            player = Player(name, score)
            players.append(player)
    return


def savelog(players) -> None:
    json_data = [{'name': player.name, 'score': player.score} for player in players]
    with open("D:/python/basics/firstproject/log.json", 'w') as file:
        json.dump(json_data, file, indent=4)
    return


def checkguess(actual, guess) -> bool:
    if actual == guess:
        return True
    return False


def selectoption(choice, players, player) -> None:
    if choice == "1":
        play(player)
        pass
    elif choice == "2":
        leaderboard(players, player)
        pass
    else:
        pass
    return


def leaderboard(players, player):
    players 
    for user in players:
        if user is player:
            
    

def play(player) -> None:
    
    while True is True:
        print("Enter a non-integer value to stop playing!")
        actual = random.randint(1, 10)
        guess = input("Enter your guess: ")
        if not guess.isdigit():
            break
        result = f"The actual answer was {actual}. "
        won = checkguess(actual, int(guess))
        if won:
            player.score += 1
            print(result + "You win!")
        else:
            print(result + "You lose..")
    
    print("You finished playing the game!")
    return


def run() -> None:
    players = []
    readlog(players)
    name = input("Enter your name: ")
    current = None
    if len(players) > 0:
        for player in players:
            if player.name == name:
                current = player
                break
    if current is None:
        current = Player(name, 0)
        players.append(current)
    play(current)
    savelog(players)
    return


run()