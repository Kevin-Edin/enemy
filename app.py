import time
player_health = 20

class Enemy:
    def __init__(self, hp: int, atk: int, nam: str):
        self.health = hp
        self.damage = atk
        self.name = nam
        self.alive = True

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def ded(self):
        if self.health <= 0:
            self.alive = False
            print(f"{self.name} dog.")
        
    def print_status(self):
        print(f"Fiende med namnet {self.name} har {self.health} hp")

    def attack(self, target):
        alive = self.is_alive()
        if alive:
            print(f"{self.name} attackerar {target.name}!")
            target.health = (target.health - self.damage)
            print(f"{target.name} har nu {target.health} hp")
            target.ded()
    
    def take_damage(self, incoming_damage):
        alive = self.is_alive()
        if alive:
            self.health = self.health - incoming_damage
            print(self.health)
            self.ded()


chicken = Enemy(3, 1, "Kyckling")
chicken.print_status()

jesus = Enemy(999, 999, "Jesus")
jesus.print_status()

chicken.attack(jesus)

jesus.attack(chicken)