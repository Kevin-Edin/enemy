import time
player = "Peter"
player_health = 20
map_size = 30
player_money = 0

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x}, {self.y}"
    
    
    def add(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    
class Inventory:
    def __init__(self, inv_owner: str, inv_size: int):
        self.size = inv_size
        self.owner = inv_owner
        self.contents = []

    def add_item(self, item):
        if len(self.contents) < self.size:
            self.contents.append(item.name)

    def remove_item(self, item):
        del self.contents[self.contents.index(item)]

    def get_contents(self):
        return self.contents
    
player_inventory = Inventory(player, 5)

class Item:
    def __init__(self, name: str, description: str, value: int, rarity: str):
        self.name = name
        self.description = description
        self.value = value
        self.rarity = rarity

    def inspect(self):
        print(self.description)
    
    def sell(self):
        player_inventory.remove_item(self.name)
        return self.value
    
    def use(self):
        player_inventory.remove_item(self.name)

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

    def move_to(self, x, y):
        if self.is_alive():
            new_position = Vector2(x, y)
            self.position = self.position.add(new_position)
            print(f"{self.name} flyttade till ({self.position})!")

chicken = Enemy(3, 1, "Kyckling")
chicken.print_status()

jesus = Enemy(999, 999, "Jesus")
jesus.print_status()

barbapappan = Enemy(1000000, 1000000, "Barbapappa")
barbapappan.print_status()

chicken.attack(jesus)

jesus.attack(chicken)

jesus.move_to(5, -20)

jesus.current_position()

barbapappan.attack(jesus)

print("ingen kan rymma från barbappapan...")

cat = Item("Cat", "Meows alot", 5, "Insane")

print(player_inventory.get_contents())
player_inventory.add_item(cat)
print(player_inventory.get_contents())
player_money = cat.sell()
print(player_inventory.get_contents())
print(player_money)