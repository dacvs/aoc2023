with open("input.txt") as f:
    ans = 0
    for s in f:
        load = {"red": 0, "green": 0, "blue": 0}
        _, games = s.split(':')
        for game in games.split(';'):
            for cube in game.split(','):
                count, color = cube.split()
                load[color] = max(load[color], int(count))
        ans += load["red"] * load["green"] * load["blue"]
    print("ans", ans)
