import itertools

from functions.intcode import execIntCodeOne, execIntCodeTwo, execIntCodeThree, execIntCodeFour, execIntCodeFive, \
    execIntCodeSix, execIntCodeSeven, execIntCodeEight
from functions.utils import debug


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
            debug(f"Input: {thruster}, {prevOutput}")
            pos = execIntCodeThree(_input, pos, thruster, prevOutput)
        elif intCode == 4:
            if _input[pos + 2] == 99:
                prevOutput = execIntCodeFour(_input, mode, pos)
                debug(f"Finalizing on 4: {prevOutput}")
                return prevOutput
            else:
                pos, prevOutput = execIntCodeFour(_input, mode, pos)
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
    debug(f"Finalizing !on 4: {prevOutput}")
    return prevOutput


if __name__ == '__main__':
    output = []
    output.append(
        [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0,
         5])  # 139629729 for 98765
    # output.append([3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
    #                -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
    #                53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10])  # 18216 for 97856
    for x in output:
        thrusterSequences = itertools.permutations([0, 1, 2, 3, 4])
        thrusterOutputs = []
        feedbackLoop = [9, 8, 7, 6, 5]
        code = 0
        for thruster in thrusterSequences:
            for i in range(len(thruster)):
                debug(f"Step {i}T - Current Code {code}")
                code = main(x, thruster[i], code)
            for j in range(len(feedbackLoop)):
                print(f"Step {j}F - Current Code {code}")
                code = main(x, feedbackLoop[j], code)
        thrusterOutputs.append(code)
        thrusterOutputs.sort(reverse=True)
        print(f"Highest Thruster Output: {thrusterOutputs[0]}")
