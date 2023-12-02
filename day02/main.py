import fileinput

example1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split('\n')

def solve1(puzzle):
    s = 0
    def constraints(m):
        return m['red'] <=12 and m['green'] <= 13 and m['blue'] <= 14

    for line in puzzle:
        line = line.strip()
        if not line:
            continue
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        line = line.split(':')
        game_id = int(line[0].split()[1])
        sets = line[1]
        add = True
        for play in sets.split(';'):
            play = play.split(',')
            m = {'red':0,'green':0,'blue':0}
            for draw in play:
                draw = draw.split()
                k = draw[1].strip()
                m[k] += int(draw[0].strip())
            if not constraints(m):
                add = False
                break
        if add:
            s += game_id
    print(s)


example2 = example1

def solve2(puzzle):
    s = 0
    def constraints(m):
        return m['red'] <=12 and m['green'] <= 13 and m['blue'] <= 14

    for line in puzzle:
        line = line.strip()
        if not line:
            continue
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        line = line.split(':')
        game_id = int(line[0].split()[1])
        sets = line[1]
        mini = {}
        for play in sets.split(';'):
            play = play.split(',')
            m = {}
            for draw in play:
                draw = draw.split()
                k = draw[1].strip()
                v = int(draw[0].strip())
                if not k in m:
                    m[k] = v
            for k,v in m.items():
                if not k in mini:
                    mini[k] = v
                    continue
                if mini[k] < v:
                    mini[k] = v
        power = 1
        for v in mini.values():
            power *= v
        s += power
    print(s)

def main():

    puzzle = list(fileinput.input())

    # for line in fileinput.input():
    #     line

    # solve1(example1)
    # solve1(puzzle)

    solve2(example2)
    solve2(puzzle)

if __name__ == '__main__':
    main()
