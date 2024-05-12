class Warrior:
    def __init__(self, health = 50, attack = 5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0

class Knight(Warrior):
    def __init__(self):
        super().__init__(self, health = 50, attack = 7)
        

def fight(first_unit: Warrior,
          second_unit: Knight) -> bool:
    while second_unit.is_alive and first_unit.is_alive:
        second_unit.health -= first_unit.attack
        if second_unit.is_alive:
            first_unit.health -= second_unit.attack

    return first_unit.is_alive



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    print("Coding complete? Let's try tests!")
