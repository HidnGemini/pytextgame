class Player():
    def __init__(self, hp, defense, atk, currentMap, itemDictionary):
        self.baseStats = [hp, defense, atk]
        self.hp = hp
        self.maxHp = hp
        self.defense = defense
        self.atk = atk
        self.regen = 0
        self.inv = []
        self.currentMap = currentMap
        self.roomID = self.currentMap.map[self.currentMap.row][self.currentMap.col]
        self.itemDict = itemDictionary
        self.gameOver = False
        self.equipedWeapon = 0
        self.equipedArmor = 0
        self.equipedTrinket = 0
        self.regenTime = 0
        self.unrecoverables = [0, 23, 24]
    def move(self, direction):
        row = self.currentMap.row
        col = self.currentMap.col
        if direction == 'n' or direction == 'north':
            print(f"""
            You walk north
            """)
            row -= 1
        elif direction == 'e' or direction == 'east':
            print(f"""
            You walk east
            """)
            col += 1
        elif direction == 's' or direction == 'south':
            print(f"""
            You walk south
            """)
            row += 1
        elif direction == 'w' or direction == 'west':
            print(f"""
            You walk west
            """)
            col -= 1
        self.currentMap.row = row
        self.currentMap.col = col
        self.roomID = self.currentMap.map[row][col]
        self.currentMap.onEntry()
    def takeDamage(self, damage, whoAttacked):
        trueDamage = int((damage**2) / (damage + (self.defense / 2)))
        self.hp -= trueDamage
        if whoAttacked == 'You':
            print(f"""
            You hit yourself for {trueDamage} damage. That wasn't the smartest idea...
            """)
        else:
            print(f"""
            {whoAttacked} hit you for {trueDamage} damage
            """)
        if self.hp <= 0:
            self.gameOver = True
    def readInv(self):
        if len(self.inv) == 0:
            print(f"""
            You don't have any items!
            """)
        else:
            print(f'Your Bag:')
            for item in self.inv:
                print(self.itemDict[item].name)
        self.readEquiped()
    def readEquiped(self):
        weapStr = f"You wield a {self.itemDict[self.equipedWeapon].name if self.equipedWeapon != 0 else 'nothing'}."
        armorStr = f"You are wearing {self.itemDict[self.equipedArmor].name if self.equipedArmor != 0 else 'nothing to protect yourself'}."
        trinkStr = f"You have {self.itemDict[self.equipedTrinket].name if self.equipedTrinket != 0 else 'nothing'} equiped."
        print(f"""
        {weapStr}
        {armorStr}
        {trinkStr}
        """)
    def equip(self, item):
        id = self.itemDict.revDict[item]
        type = self.itemDict.items[id].type
        if type == 'weapon':
            if self.equipedWeapon != 0:
                self.inv.append(self.equipedWeapon)
                self.equipedWeapon = id
                self.inv.remove(id)
            else:
                self.equipedWeapon = id
                self.inv.remove(id)
        elif type == 'armor':
            if self.equipedArmor != 0:
                self.inv.append(self.equipedArmor)
                self.equipedArmor = id
                self.inv.remove(id)
            else:
                self.equipedArmor = id
                self.inv.remove(id)
        elif type == 'atkTrinket':
            if self.equipedTrinket not in self.unrecoverables:
                self.inv.append(self.equipedTrinket)
                self.equipedTrinket = id
                self.inv.remove(id)
            else:
                self.equipedTrinket = id
                self.inv.remove(id)
        elif type == 'defTrinket':
            if self.equipedTrinket not in self.unrecoverables:
                self.inv.append(self.equipedTrinket)
                self.equipedTrinket = id
                self.inv.remove(id)
            else:
                self.equipedTrinket = id
                self.inv.remove(id)
        elif type == 'hpTrinket':
            if self.equipedTrinket not in self.unrecoverables:
                self.inv.append(self.equipedTrinket)
                self.equipedTrinket = id
                self.inv.remove(id)
            else:
                self.equipedTrinket = id
                self.inv.remove(id)
        elif type == 'regenTrinket':
            if self.equipedTrinket not in self.unrecoverables:
                self.inv.append(self.equipedTrinket)
                self.equipedTrinket = id
                self.inv.remove(id)
            else:
                self.equipedTrinket = id
                self.inv.remove(id)
        else:
            print(f"""
            You can't equip {item}
            """)
        self.reloadStats()
    def reloadStats(self):
        trinketType = self.itemDict[self.equipedTrinket].type
        self.maxHp = self.baseStats[0]
        self.defense = self.baseStats[1] + self.itemDict[self.equipedArmor].attribute
        self.atk = self.baseStats[2] + self.itemDict[self.equipedWeapon].attribute
        if trinketType == 'atkTrinket':
            self.atk += self.itemDict[self.equipedTrinket].attribute
        elif trinketType == 'defTrinket':
            self.defense += self.itemDict[self.equipedTrinket].attribute
        elif trinketType == 'hpTrinket':
            self.maxHp += self.itemDict[self.equipedTrinket].attribute
        elif trinketType == 'regenTrinket':
            self.regen = self.itemDict[self.equipedTrinket].attribute
            self.regenTime = 10
    def pickUp(self, item):
        if self.currentMap.roomDict[self.roomID].hasItem == True:
            if self.itemDict.items[self.currentMap.roomDict[self.roomID].item].name.lower() == item:
                print(f"""
                You take the {item}
                """)
                self.inv.append(self.itemDict.revDict[item])
                self.currentMap.roomDict[self.roomID].item = -1
                self.currentMap.roomDict[self.roomID].hasItem = False
            else:
                print("""
                This room doesn't have that item!
                """)
        else:
            print("""
            This room doesn't have an item to pickup!
            """)
    def takeOff(self, item):
        equiped = [self.equipedWeapon, self.equipedArmor, self.equipedTrinket]
        if self.itemDict.revDict[item] in equiped:
            if item in self.unrecoverables:
                print(f"""
                You removed your {item} but it ripped
                """)
                if self.itemDict.revDict[item] == self.equipedWeapon:
                    self.equipedWeapon = 0
                elif self.itemDict.revDict[item] == self.equipedArmor:
                    self.equipedArmor = 0
                elif self.itemDict.revDict[item] == self.equipedTrinkets:
                    self.equipedTrinket = 0
            else:
                print(f"""
                You removed your {item}.
                """)
                if self.itemDict.revDict[item] == self.equipedWeapon:
                    self.inv.append(self.itemDict.revDict[item])
                    self.equipedWeapon = 0
                elif self.itemDict.revDict[item] == self.equipedArmor:
                    self.inv.append(self.itemDict.revDict[item])
                    self.equipedArmor = 0
                elif self.itemDict.revDict[item] == self.equipedTrinket:
                    self.inv.append(self.itemDict.revDict[item])
                    self.equipedTrinket = 0
            self.reloadStats()
        else:
            print(f"""
            You don't have {item} equiped.
            """)
    def shatter(self):
        print(f"""
        Your {self.itemDict[self.equipedTrinket].name} ripped from overuse.
        """)
        self.equipedTrinket = 0
