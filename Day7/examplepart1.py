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
                pos = execIntCodeFour(_input, mode, pos)
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
    raw_input = getInput("day5")
    splitInput = []
    raw_input = raw_input.split(',')
    for x in raw_input:
        splitInput.append(int(x))
    output = []
    # output.append([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0])  # thrusterSeq = [4,3,2,1,0] , output = 43210
    # output.append([3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0,
    #                0])  # thrusterSeq = [0,1,2,3,4] , output = 54321
    # output.append([3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33,
    #                1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0,
    #                0])  # thrusterSeq = [1,0,4,3,2] , output = 65210
    thrusterSeq = [1, 0, 4, 3, 2]
    code = 0
    for x in output:
        for i in range(5):
            code = main(x, thrusterSeq[i], code)
        print(f"Thruster Output: {code}")
    # main(splitInput)
