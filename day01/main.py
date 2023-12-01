import fileinput
import re

example1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".split('\n')

def solve1(puzzle):
    s = 0
    reg = re.compile(r'\d')
    for line in puzzle:
        if not line:
            continue
        matches = reg.findall(line)
        if matches:
            s += int( matches[0] + matches[-1] )
    print(s)




example2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
eighthree
""".split('\n')

def solve2(puzzle):
    s = 0
    reg = re.compile(r'\d|one|two|three|four|five|six|seven|eight|nine')
    t = {'one': '1', 'two':'2', 'three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    for line in puzzle:
        if not line:
            continue
        matches = reg.findall(line)
        if matches:
            a = matches[0] if matches[0].isnumeric() else t[matches[0]]
            b = matches[-1] if matches[-1].isnumeric() else t[matches[-1]]
            print(a,b)
            s += int(a+b)
    print(s)

def main():

    puzzle = list(fileinput.input())
    # for line in fileinput.input():
    #     line

    solve1(example1)
    solve1(puzzle)

    solve2(example2)
    # solve2(puzzle)

if __name__ == '__main__':
    main()
