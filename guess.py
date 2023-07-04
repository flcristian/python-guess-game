import random
import json


# Class that defines a player, which has a name and score
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

    def __str__(self):
        return f"{self.name} - {self.score} Right Guesses"


# Reads the data of players from the json file (log.json)
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


# Saves the data of the specified player in the json file (log.json)
def savelog(players) -> None:
    json_data = [{'name': player.name, 'score': player.score} for player in players]
    with open("D:/python/basics/firstproject/log.json", 'w') as file:
        json.dump(json_data, file, indent=4)
    return


# Checks if the guess matches the random number generated
def checkguess(actual, guess) -> bool:
    if actual == guess:
        return True
    return False


# Selects between playing and displaying the leaderboard
def selectoption(choice, players, current) -> bool:
    if choice == "1":
        play(current)

        # Saves logs
        savelog(players)
        return True
    elif choice == "2":
        leaderboard(players, current)
        return True
    return False


# Shows the leaderboard
def leaderboard(players, current) -> None:
    players.sort()
    players.reverse()

    print("\nHere are the best guessers!")
    for player in players:
        if player.name == current.name:
            print(f"--> ({players.index(player) + 1})", f"You - {player.score} Right Guesses <--")
        else:
            print(f"({players.index(player) + 1})", player)
    return


# Play method
def play(player) -> None:
    while True is True:
        print("\nEnter a non-integer value to stop playing!")
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


# Run the program
def run() -> None:
    # Retrieves data from logs
    players = []
    readlog(players)

    name = input("Enter your name: ")
    # Checks if the player already exists and creates one if not
    current = None
    for player in players:
        if player.name == name:
            current = player
            break
    if current is None:
        current = Player(name, 0)
        players.append(current)

    # Calls selection method
    running = True
    while running is True:
        running = selectoption(input(
            "\nChoose an option:\n1 - Play the game\n2 - Show the leaderboard\nAnything else to close the program.\n"),
                               players, current)

    print("\nYou have closed the program. Goodbye!")
    return


run()
