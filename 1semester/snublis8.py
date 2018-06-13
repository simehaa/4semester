class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.inventory = []

    def has_sword(self):
        return 'sword' in self.inventory

    def pick_up(self, thing):
        self.inventory.append(thing)

    def is_better(self, other):
        return self.level > other.level



me = Player('Simen', 100)
you = Player('Bob', 1)
print you.level
print me.name
me.pick_up('sword')
print me.has_sword()
print me.is_better(you)
