class Parse():
    def __init__(self, player, currentMap):
        self.player = player
        self.currentMap = currentMap
        self.rawInput = input('>>> ').lower()
        self.input = self.rawInput.split(' ')
        self.main()
    def itemName(self):
        self.input.pop(0)
        item = ''
        for term in self.input:
            item += f'{term} '
        return item[0:(len(item)-1)]
    def main(self):
        word = self.input[0]
        if word in ['go', 'walk', 'move']:
            direction = self.input[1]
            if ((direction == 'n' or direction == 'north') and (self.currentMap.row != 0)) or \
                ((direction == 'e' or direction == 'east') and (self.currentMap.col != (len(self.currentMap.map[0])-1))) or \
                ((direction == 's' or direction == 'south') and (self.currentMap.row != (len(self.currentMap.map)-1))) or \
                ((direction == 'w' or direction == 'west') and (self.currentMap.col != 0)):
                self.player.move(direction)
            elif direction in ['n', 's', 'e', 'w', 'north', 'south', 'east', 'west']:
                print("An invisible barrier prevents you from entry; perhaps it's the flat earth?")
            else:
                print('You must move in CARDINAL DIRECTIONS (N,S,E,W)')
        elif word in ['kill', 'attack', 'hurt', 'fight', 'hit']:
            target = self.input[1]
            if target == 'self':
                self.player.takeDamage((3 * self.player.atk), 'You')
        elif word == 'check':
            checkWhat = self.input[1]
            if checkWhat == 'health' or checkWhat == 'hp':
                print(f'Your health is at {self.player.hp} out of {self.player.maxHp}')
            if checkWhat == 'atk' or checkWhat == 'attack':
                print(f'Your attack is {self.player.atk}')
            if checkWhat == 'def' or checkWhat == 'defense':
                print(f'Your defense is {self.player.defense}' if self.player.defense < 20 else f'Your defense is {self.player.defense} MAXED!')
        elif word in ['inspect', 'read', 'open']:
            item = self.itemName()
            if item in ['inv', 'inventory', 'pockets', 'bag']:
                self.player.readInv()
            elif item in ['self', 'equipment']:
                self.player.readEquiped()
            else:
                id = self.player.itemDict.revDict[item] if item.lower() in self.player.itemDict.itemList else -1
                if id in self.player.inv:
                    self.player.itemDict.inspect(item)
                else:
                    print(f"You don't have an item called {item}!")
        elif self.rawInput in ['inv', 'inventory', 'pockets', 'bag']:
            self.player.readInv()
        elif word in ['equip', 'use']:
            item = self.itemName()
            id = self.player.itemDict.revDict[item] if item.lower() in self.player.itemDict.itemList else -1
            if id in self.player.inv:
                self.player.equip(item)
            else:
                print(f"You don't have an item called {item}!")
            item = item[0:(len(item)-1)]
        elif word in ['take', 'grab']:
            item = self.itemName()
            self.player.pickUp(item)
        elif word in ['remove', 'unequip']:
            item = self.itemName()
            self.player.takeOff(item)
        elif self.rawInput == 'where am i?':
            print(f'You are in {self.currentMap.row}, {self.currentMap.col} with Room ID {self.player.roomID}')
        elif self.rawInput == 'bee removal is the process of removing bees from a location':
            print(f"""
            Bees have been removed from the location.
            """)
        elif self.rawInput == 'tylko jedno w glowie mam':
            print(f"""
            koksu 5 gram
            odleciec sam
            w kraine zapomnienia
            w glowie mysli mam
            """)
