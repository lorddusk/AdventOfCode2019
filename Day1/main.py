import math


def mathCalc(input):
    return (math.floor(input / 3) - 2)


def part1(input):
    solution = 0
    for x in input:
        output = mathCalc(x)
        solution += output
    print(f"Part 1: {solution}")


def calculateMass(input, total=0):
    output = mathCalc(input)
    total += output
    if mathCalc(output) <= 0:
        return total
    else:
        total += calculateMass(output)
    return total


def part2(input):
    solution = 0

    for x in input:
        output = calculateMass(int(x))
        solution += output
    print(f"Part 2: {solution}")


if __name__ == '__main__':
    input = []

    f = open('../inputs/day1.txt', 'r')
    for x in f:
        if x is not '':
            input.append(int(x))
    part1(input)
    part2(input)
