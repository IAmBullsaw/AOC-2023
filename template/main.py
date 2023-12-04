import sys
sys.path.append('../utils/')
import utils


example1 = utils.example_as_list("""""")
answer1 =

def solve1(puzzle):
    pass


example2 = """""".split('\n')
answer2 =

def solve2(puzzle):
    pass

def main():

    puzzle = utils.input_as_list(separator=None) # input_as_ints(separator=None)

    if not answer1 == solve1(example1):
        exit(1)
    solve1(puzzle)

    if not answer2 == solve2(example2):
        exit(1)
    solve2(puzzle)

if __name__ == '__main__':
    main()
