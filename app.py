import time
player_health = 20

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x}, {self.y}"
    
    
    def add(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

class Enemy:
    def __init__(self, hp: int, atk: int, nam: str):
        self.health = hp
        self.damage = atk
        self.name = nam
        self.alive = True
        self.position = Vector2(0, 0)

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def current_position(self):
        print(f"{self.name} befinner sig på ({self.position})")
        
    def ded(self):
        if self.health <= 0:
            self.alive = False
            print(f"{self.name} dog.")
        
    def print_status(self):
        print(f"Fiende med namnet {self.name} har {self.health} hp")

    def attack(self, target):
        if self.is_alive():
            print(f"{self.name} attackerar {target.name}!")
            target.health = (target.health - self.damage)
            print(f"{target.name} har nu {target.health} hp")
            target.ded()
    
    def take_damage(self, incoming_damage):
        if self.is_alive():
            self.health = self.health - incoming_damage
            print(self.health)
            self.ded()

    def move(self, x, y):
        if self.is_alive():
            new_position = Vector2(x, y)
            self.position = self.position.add(new_position)
            print(f"{self.name} flyttade till ({self.position})!")

chicken = Enemy(3, 1, "Kyckling")
chicken.print_status()

jesus = Enemy(999, 999, "Jesus")
jesus.print_status()

chicken.attack(jesus)

jesus.attack(chicken)

jesus.move(5, -20)

jesus.current_position()