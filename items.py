class eqItem():
    def __init__(self, name, type, attribute, description):
        self.name = name
        self.type = type
        self.desc = description
        # Types: [Weapon, Armor, atkTrinket, defTrinket, hpTrinket, regenTrinket]
        self.attribute = attribute
    def readDesc(self):
        print(name)
        print(description)


class itemDict():
    def __init__(self):
        self.items = {
            0:eqItem('nothing!', 'void', 0, \
                """
                There is nothing equiped here...
                """),
            1:eqItem('Rusty Sword', 'weapon', 10, \
                """
                A simple, rusted sword
                +10 damage
                """),
            2:eqItem('Reforged Sword', 'weapon', 15, \
                """
                A simple sword
                +15 damage
                """),
            3:eqItem('Guilded Sword', 'weapon', 30, \
                """
                A sword dipped in gold
                +30 damage
                """),
            4:eqItem('Jeweled Sword', 'weapon', 50, \
                """
                A jewel encrusted, gold dipped sword
                +50 damage
                """),
            5:eqItem('Frick... uhh... TOE', 'weapon', 999, \
                """
                *Slurp Sound*
                The Zambies Item
                How did you figure this out?
                """),
            6:eqItem('Master Sword', 'weapon', 999, \
                """
                This powerful sword has been used by many knights through generations! 
                The googledocs Item
                How did you figure this out?
                """),
            7:eqItem('A Shlong Gun', 'weapon', 999, \
                """
                A gun that isn't long, it's SHLONG
                The Goulash_Lord Item
                How did you figure this out?
                """),
            8:eqItem('Dusty Shirt', 'armor', 1, \
                """
                A dusty shirt that adds a layer of defense against simple attacks
                +1 Defense
                """),
            9:eqItem('Leather Jacket', 'armor', 3, \
                """
                A Jacket made of a harder leather
                +3 Defense
                """),
            10:eqItem('Chainmail Shirt', 'armor', 7, \
                """
                A Shirt made of Chains to block sword attacks
                +7 Defense
                """),
            11:eqItem('Old Iron Chestplate', 'armor', 10, \
                """
                A dusty plate of iron to defend against attacks
                +10 Defense
                """),
            12:eqItem('Refined Iron Chestplate', 'armor', 13, \
                """
                A renewed iron chest covering
                +13 Defense
                """),
            13:eqItem('Glimering Iron Chestplate', 'armor', 15, \
                """
                An iron chestpiece glimmering with magic
                +15 Defense
                """),
            14:eqItem('Red Drop Talisman', 'atkTrinket', 3, \
                """
                A ruby droplet
                +3 Atk
                """),
            15:eqItem('Red Drop Necklace', 'atkTrinket', 5, \
                """
                A necklace with a ruby droplet
                +5 Atk
                """),
            16:eqItem('Shining Red Drop Necklace', 'atkTrinket', 10, \
                """
                A necklace with a shimmering ruby droplet
                +10 Atk
                """),
            17:eqItem('Rock Necklace', 'defTrinket', 2, \
                """
                A neclace with a little silver rock
                +2 Def
                """),
            18:eqItem('Crossed Shield Necklace', 'defTrinket', 3, \
                """
                A necklace with a cracked shield
                +3 Def
                """),
            19:eqItem("Knight's Talisman", 'defTrinket', 5, \
                """
                A talisman carried by the strongest of knights
                +5 Def
                """),
            20:eqItem('Half Heart Necklace', 'hpTrinket', 15, \
                """
                A necklace with half of an amethyst heart
                +15 Max HP
                """),
            21:eqItem('Full Heart Necklace', 'hpTrinket', 25, \
                """
                Reconnected heart: A necklace with a full amethyst heart
                +25 Max HP
                """),
            22:eqItem("Doctor's Band", 'hpTrinket', 100, \
                """
                A white band with a red cross
                +100 Max HP
                """),
            23:eqItem("Nurse's Band", 'regenTrinket', 5, \
                """
                A white ribbon with a red cross
                breaks after 10 uses and cannot be taken off
                +5 HP per turn
                """),
            24:eqItem("Ring of full Health", 'regenTrinket', 8, \
                """
                A silver ring shining pink
                breaks after 10 uses and cannot be taken off
                +8 HP per turn
                """)
            }
        self.setUp()
    def setUp(self):
        self.revDict = {}
        self.itemList = []
        values = self.items.values()
        i = 0
        for value in values:
            self.revDict[value.name.lower()] = i
            self.itemList.append(value.name.lower())
            i += 1
    def __getitem__(self, key):
        return self.items[key]
    def inspect(self, item):
        if item in self.itemList:
            id = self.revDict[item]
            print(self.items[id].name)
            print(f'Type: {self.items[id].type}')
            print(self.items[id].desc)
        else:
            print(f"You don't have an item called {rawItem}!")

