import time
player_health = 20

class Enemy:
    def __init__(self, hp: int, atk: int, nam: str):
        self.health = hp
        self.damage = atk
        self.name = nam

    def print_status(self):
        print(f"Fiende med namnet {self.name} har {self.health} hp")

    def attack(self, target):
        print(f"{self.name} attackerar dig!")
        target = (target - self.damage)
        return target
    
    def take_damage(self, incoming_damage):
        if self.health > 0:
            self.health = self.health - incoming_damage
            print(self.health)


chicken = Enemy(3, 1, "Kyckling")
chicken.print_status()

jesus = Enemy(999, 999, "Jesus")
jesus.print_status()

chicken.take_damage(3)