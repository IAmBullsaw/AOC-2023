import fileinput
 
example1 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split('\n')


class Puzzle:

    def __init__(self, puzzle):
        # for i, l in enumerate(puzzle):
        #     print('  %d' % (i) , l)
        # s = "    "
        # for i in range(0,len(puzzle)):
        #     s += str(i)
        # print(s)
        self.p = []
        for l in puzzle:
            self.p.append(l.strip())

    def get(self, x, y):
        """
        x ->
        y
        |  x grows to the right, y grows south
        """
        if 0 <= x < len(self.p[0]) and 0 <= y < len(self.p):
            return self.p[y][x]
        return None

    def yield_adjacent(self, x_start, x_end, y_start):
        # above
        y_start -= 1
        for x in range(x_start-1,x_end+2):
           yield self.get(x, y_start)

        # same row
        y_start += 1
        yield self.get(x_start - 1, y_start)
        yield self.get(x_end + 1, y_start)

        # below
        y_start += 1
        for x in range(x_start-1, x_end+2):
           yield self.get(x, y_start)

    def yield_adjacent_pos(self, x_start, x_end, y_start):
        # above
        y_start -= 1
        for x in range(x_start-1,x_end+2):
           yield self.get(x, y_start), (x, y_start)

        # same row
        y_start += 1
        yield self.get(x_start - 1, y_start), (x_start -1 , y_start)
        yield self.get(x_end + 1, y_start), (x_end +1 , y_start)

        # below
        y_start += 1
        for x in range(x_start-1, x_end+2):
           yield self.get(x, y_start), (x, y_start)

import re
def solve1(puzzle):
    # find number
    p = Puzzle(puzzle)
    # print([x for x in p.yield_adjacent(0,2,0)])

    r = re.compile('\d+')
    s = 0
    for idx,l in enumerate(puzzle):
        for match in r.finditer(l):
            for adj in p.yield_adjacent(match.start(),match.end()-1, idx):
                if adj and adj != '.':
                    s += int(match[0])
                    break
            # print([x for x in p.yield_adjacent(match.start(),match.end()-1, idx)])
    print(s)


    # check what's adjacent

    # if adjacent to thing, +1


example2 = example1

def solve2(puzzle):
    # find number
    p = Puzzle(puzzle)
    # print([x for x in p.yield_adjacent(0,2,0)])

    r = re.compile('\d+')
    s = 0
    m = {}
    for idx,l in enumerate(puzzle):
        for match in r.finditer(l):
            for adj, pos in p.yield_adjacent_pos(match.start(),match.end()-1, idx):
                if adj and adj == '*':
                    if not pos in m:
                        m[pos] = [int(match[0])]
                    else:
                        m[pos].append(int(match[0]))
                    break
            # print([x for x in p.yield_adjacent(match.start(),match.end()-1, idx)])
    for k,v in m.items():
        if len(v) == 2:
            s += v[0] * v[1]
    print(s)

def main():

    puzzle = list(fileinput.input())
    if not puzzle[-1].strip():
        puzzle = puzzle[0:-1]

    # for line in fileinput.input():
    #     line

    # solve1(example1)
    # solve1(puzzle)

    solve2(example2)
    solve2(puzzle)

if __name__ == '__main__':
    main()
