class Warrior():
    __health = 100
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.status = True

    def info(self):
        return f"{self.name} ({self.health})"

    def damage(self):
        self.health = self.health - 20
        if(self.health == 0): 
            self.status = False

    def attack(self):
        print(f"{self.name} наносит удар")