import time, worldMap, playerClass, inputparse, items, enemies
currentMap = worldMap.Map() 
itemDictionary = items.itemDict()
player = playerClass.Player(100, 0, 10, currentMap, itemDictionary)
currentMap.onEntry()
while not(player.gameOver):
    inputparse.Parse(player, currentMap)
    if player.regenTime != 0:
        if player.hp < player.maxHp:
            player.hp += player.regen
            player.regenTime -= 1 if player.regenTime != 0 else 0
    elif player.equipedTrinket in [23, 24]:
        player.shatter()
    time.sleep(0.15) 
print('game over')