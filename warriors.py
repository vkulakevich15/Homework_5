class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.strike_count = 0  

    @property
    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"Type: {self.__class__.__name__}, Health: {self.health}, Attack: {self.attack}"

    def __add__(self, N):
        self.health += N
        self.attack += N
        return self

    def __mul__(self, N):
        self.health *= N
        self.attack *= N
        return self

    def get_damage(self):
        return self.attack

    def take_damage(self, damage):
        self.health -= damage


class Orc(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 55
        self.attack = 6
        self.fury = 2

    def get_damage(self):     # Каждый 3-й удар наносит дополнительный урон +fury
        self.strike_count += 1
        if self.strike_count % 3 == 0:
            return self.attack + self.fury
        return self.attack


def fight(first_warrior, second_warrior):
    while first_warrior.health > 0 and second_warrior.health > 0:
        second_warrior.take_damage(first_warrior.get_damage())
        if second_warrior.health <= 0:
            return True


        first_warrior.take_damage(second_warrior.get_damage())
        if first_warrior.health <= 0:
            return False

    return first_warrior.health > 0



