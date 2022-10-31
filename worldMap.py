class Map():
    def __init__(self):
        import room
        self.map = [[1, 0, 2],
                    [3, 4, 5],
                    [6, 7, 5],
                    [8, 9, 10]]
        self.row = 0
        self.col = 1
        self.roomDict = room.roomDict()
    def onEntry(self):
        print(self.roomDict.rooms[self.map[self.row][self.col]].desc)
