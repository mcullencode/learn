import Player

Tim = Player.Player("Tim")

print(Tim.name)
print(Tim.lives)

Tim.lives -= 1
print(Tim)

Tim.lives = 9
print(Tim)

Tim.level = 2
print(Tim)

Tim.level += 5
print(Tim)


Tim.score = 500
print(Tim)