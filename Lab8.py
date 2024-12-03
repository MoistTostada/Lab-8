import random

player = {"name": "null",
          "Inventory": {}, 
          "stats": {}
         }

def roll4D6():
    """
    Roll a 6-sided die 4 times, drop the lowest value,
    sum the remaining values, and return the sum.
    """
    arr = [random.randint(1, 6) for _ in range(4)]
    arr.remove(min(arr))
    return sum(arr)

def showStats():
    # Show each stat to the player
    for stat in player["stats"]:
        print(f"{stat}: {player['stats'][stat]}")

def charCreation():
    player["name"] = input("Enter your name: ")
    player["stats"] = {
        "str": roll4D6(),
        "dex": roll4D6(),
        "cons": roll4D6(),
        "int": roll4D6(),
        "char": roll4D6(),
        "weight": 0
    }
    player["stats"]["weight"] = player["stats"]["str"] * 15

def main():
    # Create a new file to store the user's stats
    filename = "game_stats.txt"
    with open(filename, "w") as file:
        charCreation()
        file.write(f"Name: {player['name']}\n")
        file.write("Stats:\n")
        for stat in player["stats"]:
            file.write(f"{stat}: {player['stats'][stat]}\n")
        print(f"Your information was successfully written to {filename}")

if __name__ == "__main__":
    main()
    
