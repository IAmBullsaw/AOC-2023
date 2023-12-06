import sys
sys.path.append('../utils/')
import utils


example1 = utils.example_as_list("""
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""")
answer1 = 35

import re

def dest(ranges, source):
    for r in ranges:
        if source in range(r[1],r[2]+1):
            return 2
    return source






def solve1(puzzle):
    seeds = list(puzzle[0].split(':')[1].split())

    reg = re.compile(r'(\w+)-\w+-(\w+)')
    maps = {}
    curr = ''
    for l in puzzle[1:]:
        if m := reg.match(l):
            curr = m[1][0:2]
            maps[curr]= []
        elif l:
            maps[curr].append([int(x) for x in l.split()])
    print(maps)
    print(dest(maps['se'], 79), 'should be 81')
    print(dest(maps['se'], 50), 'should be 52')
    print(dest(maps['se'], 10), 'should be 10')
    pass


example2 = """""".split('\n')
answer2 = -1

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
