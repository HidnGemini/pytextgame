class enemy():
    def __init__(self, name, desc, atk, hp, defense):
        self.name = name
        self.desc = desc
        self.atk = atk
        self.maxHp = hp
        self.hp = hp
        self.defense = defense
    def takeDamage(self, damage):
        trueDamage = int((damage**2) / (damage + (self.defense / 2)))
        self.hp -= trueDamage
        print(f"""
        You hit the {self.name} for {trueDamage} damage
        """)




