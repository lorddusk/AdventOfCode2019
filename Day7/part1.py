import itertools

from functions.intcode import execIntCodeOne, execIntCodeTwo, execIntCodeThree, execIntCodeFour, execIntCodeFive, \
    execIntCodeSix, execIntCodeSeven, execIntCodeEight
from functions.utils import getInput


def parameters(param):
    string = str(param)
    while len(string) != 5:
        string = "0" + string
    mode = string[:3]
    intcode = string[3:]
    return mode, int(intcode)


def main(_input, thruster, prevOutput):
    pos = 0
    intCode = 0
    while intCode != 99:
        intCode = _input[pos]
        mode, intCode = parameters(intCode)
        if intCode == 1:
            pos = execIntCodeOne(_input, mode, pos)
        elif intCode == 2:
            pos = execIntCodeTwo(_input, mode, pos)
        elif intCode == 3:
            pos = execIntCodeThree(_input, pos, thruster, prevOutput)
        elif intCode == 4:
            if _input[pos + 2] == 99:
                return execIntCodeFour(_input, mode, pos)
            else:
                pos, code = execIntCodeFour(_input, mode, pos)
        elif intCode == 5:
            pos = execIntCodeFive(_input, mode, pos)
        elif intCode == 6:
            pos = execIntCodeSix(_input, mode, pos)
        elif intCode == 7:
            pos = execIntCodeSeven(_input, mode, pos)
        elif intCode == 8:
            pos = execIntCodeEight(_input, mode, pos)
        else:
            pos += 1


if __name__ == '__main__':
    raw_input = getInput("day7")
    splitInput = []
    raw_input = raw_input.split(',')
    for x in raw_input:
        splitInput.append(int(x))
    thrusterSequences = itertools.permutations([0, 1, 2, 3, 4])
    thrusterOutputs = []
    for thrusterSeq in thrusterSequences:
        code = 0
        for i in range(len(thrusterSeq)):
            code = main(splitInput, thrusterSeq[i], code)
        thrusterOutputs.append(code)
    thrusterOutputs.sort(reverse=True)
    print(f"Highest Thruster Output: {thrusterOutputs[0]}")
