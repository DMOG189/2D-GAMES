#color game



# START

import random
import time

# Define player and enemy stats
player = {
    "health": 100,
    "attack": 20,
    "lives": 3
}

scenarios = [
    {
        "description": "You enter a dark forest and hear a growl nearby.",
        "enemy": {
            "name": "Wolf",
            "health": 30,
            "attack": 10
        }
    },
    {
        "description": "You walk into a deserted town and see a bandit approaching.",
        "enemy": {
            "name": "Bandit",
            "health": 50,
            "attack": 15
        }
    },
    {
        "description": "You find yourself in an abandoned warehouse and a zombie attacks.",
        "enemy": {
            "name": "Zombie",
            "health": 40,
            "attack": 12
        }
    }
]


def attack(enemy):
    damage = random.randint(0, player["attack"])
    enemy["health"] -= damage
    print(f"You attack the {enemy['name']} and deal {damage} damage. Enemy health: {enemy['health']}")


def enemy_attack(enemy):
    damage = random.randint(0, enemy["attack"])
    player["health"] -= damage
    print(f"The {enemy['name']} attacks you and deals {damage} damage. Your health: {player['health']}")


def combat(enemy):
    while enemy["health"] > 0 and player["health"] > 0:
        print("\nChoose your action: 1. Attack 2. Retreat")
        action = input("> ").strip()

        if action == "1":
            attack(enemy)
            if enemy["health"] > 0:
                enemy_attack(enemy)
        elif action == "2":
            print("You retreat from the battle.")
            return False
        else:
            print("Invalid action. Choose 1 or 2.")

    return player["health"] > 0


def play_scenario(scenario):
    print(scenario["description"])
    time.sleep(1)
    enemy = scenario["enemy"]
    print(f"A wild {enemy['name']} appears! Prepare for battle.")
    time.sleep(1)
    if combat(enemy):
        print(f"You have defeated the {enemy['name']}!\n")
    else:
        player["lives"] -= 1
        print(f"You were defeated by the {enemy['name']}. Lives remaining: {player['lives']}\n")


def game_loop():
    while player["lives"] > 0:
        scenario = random.choice(scenarios)
        play_scenario(scenario)
        if player["lives"] <= 0:
            print("You have lost all your lives. Game over!")
            break
        print("Do you want to continue to the next scenario? (yes/no)")
        if input("> ").strip().lower() != "yes":
            break

    print("Thank you for playing the shooter game!")


if __name__ == '__main__':
    game_loop()


# END
