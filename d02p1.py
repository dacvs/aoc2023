import lib
load = {"red": 12, "green": 13, "blue": 14}
ans = 0
for s in lib.block("input/02.txt"):
    possible = True
    _, game_id, games = lib.split(s, [" ", ": "])
    for game in games.split(';'):
        for cube in game.split(','):
            count, color = cube.split()
            if load[color] < int(count):
                possible = False
    if possible:
        ans += int(game_id)
print("ans", ans)
