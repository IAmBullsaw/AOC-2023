import fileinput

example1 = """""".split('\n')

def solve1(puzzle):
    pass


example2 = """""".split('\n')

def solve2(puzzle):
    pass

def main():

    puzzle = list(fileinput.input())
    if not puzzle[-1].strip():
        puzzle = puzzle[:-1]

    # for line in fileinput.input():
    #     line

    solve1(example1)
    # solve1(puzzle)

    # solve2(example2)
    # solve2(puzzle)

if __name__ == '__main__':
    main()
