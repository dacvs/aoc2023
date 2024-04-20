with open("input.txt") as f:
    load = {"red": 12, "green": 13, "blue": 14}
    ans = 0
    for s in f:
        possible = True
        title, games = s.strip().split(':')
        _, game_id = title.split()
        for game in games.split(';'):
            for cube in game.split(',')
                count, color = cube.split()
                if load[color] < int(count):
                    possible = False
        if possible:
            ans += int(game_id)
    print("ans", ans)
