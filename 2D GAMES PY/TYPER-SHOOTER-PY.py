import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.ammo = 10

    def shoot(self, enemy):
        if self.ammo > 0:
            hit = random.choice([True, False])
            if hit:
                damage = random.randint(5, 20)
                enemy.health -= damage
                print(f"{self.name} hit {enemy.name} for {damage} damage!")
            else:
                print(f"{self.name} missed!")
            self.ammo -= 1
        else:
            print("Out of ammo!")

    def reload(self):
        self.ammo = 10
        print(f"{self.name} reloaded!")

    def is_alive(self):
        return self.health > 0

class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = 50

    def attack(self, player):
        hit = random.choice([True, False])
        if hit:
            damage = random.randint(5, 15)
            player.health -= damage
            print(f"{self.name} hit {player.name} for {damage} damage!")
        else:
            print(f"{self.name} missed!")

    def is_alive(self):
        return self.health > 0

def game_loop():
    player = Player("Hero")
    enemy = Enemy("Villain")

    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name} - Health: {player.health}, Ammo: {player.ammo}")
        print(f"{enemy.name} - Health: {enemy.health}")

        action = input("Choose an action (shoot/reload): ").strip().lower()
        if action == "shoot":
            player.shoot(enemy)
        elif action == "reload":
            player.reload()
        else:
            print("Invalid action!")

        if enemy.is_alive():
            enemy.attack(player)

        time.sleep(1)

    if player.is_alive():
        print("You won!")
    else:
        print("You lost!")

if __name__ == "__main__":
    game_loop()