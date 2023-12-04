import fileinput

example1 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split('\n')


def double(n):
    if n == 0:
        return 1
    return n*2

def solve1(puzzle):
    stot = 0
    for card in puzzle:
        card, numbers = card.split(':')
        left, right = numbers.split('|')
        left = left.split()
        right = right.split()

        # score
        s = 0
        for x in left:
            if x in right:
                s = double(s)
        stot += s
    print(stot)


example2 = example1

def solve2(puzzle):
    num_cards = len(puzzle)
    m = {n:1 for n in range(1, num_cards+1)}
    for card in puzzle:
        card, numbers = card.split(':')
        card, cardId = card.split()
        cardId = int(cardId)
        left, right = numbers.split('|')
        left = left.split()
        right = right.split()

        num = 0
        for x in left:
            if x in right:
                num += 1

        if num:
            for copy in range(cardId+1, cardId+num+1):
                if copy <= num_cards:
                    m[copy] += 1 * m[cardId]
    stot = 0
    for v in m.values():
        stot += v
    print(stot)


def main():

    puzzle = list(fileinput.input())
    if not puzzle[-1].strip():
        puzzle = puzzle[:-1]

    # for line in fileinput.input():
    #     line

    # solve1(example1)
    # solve1(puzzle)

    # solve2(example2)
    solve2(puzzle)

if __name__ == '__main__':
    main()
