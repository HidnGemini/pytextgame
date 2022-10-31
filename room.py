class room():
    def __init__(self, enemy, item, itemRegen, description):
        import items
        self.itemDict = items.itemDict()
        if enemy != -1:
            self.hasEnemy = True
            self.enemy = enemy
            enemyDesc = f'A {self.enemy}' #TODO: Make name, NOT ID
        else:
            self.hasEnemy = False
        if item != -1:
            self.hasItem = True
            self.item = item
            self.itemRegen = itemRegen
            itemDesc = f'A {self.itemDict.items[self.item].name} presents itself.'
        else:
            self.hasItem = False
        nothing = ''
        self.desc = f"""
        {enemyDesc if self.hasEnemy else nothing}
        {description}
        {itemDesc if self.hasItem else nothing}
        """


class roomDict():
    def __init__(self):
        self.rooms = {
            -1:room(-1, 14, False, \
            f"""
            The Dev Test Room - A blank room with luminous white walls.
            """),
            0:room(-1, -1, False, \
            f"""
            A meadow surrounded by forest. There may be something hidden 
            in deeper. A faint glow comes from the east.
            """),
            1:room(-1, -1, False, \
            f"""
            A deep forest, you see a meddow toward the east.
            """),
            2:room(-1, 1, False, \
            f"""
            A stone pedestal with a Rusty Sword sticking out presents itself.
            Light beams shine down upon the pedestal.
            """),
            3:room(-1, -1, False, \
            """
            IMPLEMENT LATER [GOLD]

            A forest thicket with a pile of gold in the middle.
            """),
            4:room(-1, -1, False, \
            """
            A forest thicket with a dusty path heading north or south.
            """),
            5:room(-1, -1, True, \
            """
            IMPLEMENT APPLE IDIOT

            An apple tree in the middle of a field
            """),
            6:room(-1, -1, False, \
            """
            IMPLEMENT BLACKSMITH IDIOT

            You find yourself in front of a stand 
            with an old bald blacksmith.
            """),
            7:room(-1, -1, False, \
            """
            A forest thicket with a dusty path heading north or south and branching west.
            """),
            8:room(-1, -1, False, \
            """
            IMPLEMENT STORE IDIOT

            You see a small store with a young
            lady tending the checkout.
            """),
            9:room(-1, -1, False, \
            """
            A forest thicket with a dusty path heading north or west.
            """),
            10:room(-1, -1, False, \
            """
            CAVE POG
            """)
            }
    def __getitem__(self, key):
        return self.rooms[key]




