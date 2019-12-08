from functions.utils import getInput


def inputer(message):
    return int(input(message))


def parameters(intCode):
    string = str(intCode)
    while len(string) != 5:
        string = "0" + string
    mode = string[:3]
    intCode = string[3:]
    return mode, int(intCode)


def main(raw_input):
    pos = 0
    intCode = 0
    while (intCode != 99):
        intCode = raw_input[pos]
        mode, intCode = parameters(intCode)
        if intCode == 1:
            input1 = param(mode, pos, raw_input, 2, 1)
            input2 = param(mode, pos, raw_input, 1, 2)

            output = (input1 + input2)

            outputPos = param(mode, pos, raw_input, 0, 3)
            raw_input[outputPos] = output
            pos += 4
        elif intCode == 2:
            input1 = param(mode, pos, raw_input, 2, 1)
            input2 = param(mode, pos, raw_input, 1, 2)
            output = (input1 * input2)

            outputPos = param(mode, pos, raw_input, 0, 3)
            raw_input[outputPos] = output
            pos += 4
        elif intCode == 3:
            inputN = inputer("Enter Instruction: ")
            outputTo = raw_input[(pos + 1)]
            raw_input[outputTo] = inputN
            pos += 2
        elif intCode == 4:
            output = param(mode, pos, raw_input, 2, 1)
            pos += 2
            if raw_input[pos] == 99:
                print(f"Diagnostic Code: {output}")
            else:
                print(f"Output: {output}")
        elif intCode == 5:
            input1 = param(mode, pos, raw_input, 2, 1)
            if input1 != 0:
                input2 = param(mode, pos, raw_input, 1, 2)
                pos = input2
            else:
                pos += 3
        elif intCode == 6:
            input1 = param(mode, pos, raw_input, 2, 1)
            if input1 == 0:
                input2 = param(mode, pos, raw_input, 1, 2)
                pos = input2
            else:
                pos += 3
        elif intCode == 7:
            input1 = param(mode, pos, raw_input, 2, 1)
            input2 = param(mode, pos, raw_input, 1, 2)
            outputPos = param(mode, pos, raw_input, 0, 3)
            if input1 < input2:
                raw_input[outputPos] = 1
            else:
                raw_input[outputPos] = 0
            pos += 4
        elif intCode == 8:
            input1 = param(mode, pos, raw_input, 2, 1)
            input2 = param(mode, pos, raw_input, 1, 2)
            outputPos = param(mode, pos, raw_input, 0, 3)
            if input1 == input2:
                raw_input[outputPos] = 1
            else:
                raw_input[outputPos] = 0
            pos += 4
        else:
            pos += 1


def param(mode, pos, raw_input, n, inc):
    parameter = int(mode[n])
    if n != 0:
        if parameter == 0:
            input1 = raw_input[raw_input[(pos + inc)]]
        elif parameter == 1:
            input1 = raw_input[(pos + inc)]
        else:
            input1 = None
    else:
        if parameter == 0:
            input1 = raw_input[(pos + inc)]
        elif parameter == 1:
            input1 = (pos + inc)
        else:
            input1 = None
    return int(input1)


if __name__ == '__main__':
    raw_input = getInput()
    output = []
    raw_input = raw_input.split(',')
    for x in raw_input:
        output.append(int(x))
    # output = []
    # output.append([3,9,8,9,10,9,4,9,99,-1,8]) # == 8 = 1
    # output.append([3,9,7,9,10,9,4,9,99,-1,8]) # < 8 = 1
    # output.append([3,3,1108,-1,8,3,4,3,99]) # == 8 = 1
    # output.append([3,3,1107,-1,8,3,4,3,99]) # < 8 = 1
    # output.append([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]) # == 0 = 0
    # output.append([3,3,1105,-1,9,1101,0,0,12,4,12,99,1]) # == 0 = 0
    # output.append([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
    #                1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
    #                999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98,
    #                99])  # < 8 = 999, == 8 = 1000, > 8 = 1001
    # output.append([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
    #                1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
    #                999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98,
    #                99])  # < 8 = 999, == 8 = 1000, > 8 = 1001
    # output.append([3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
    #                1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
    #                999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98,
    #                99])  # < 8 = 999, == 8 = 1000, > 8 = 1001
    # for x in output:
    #     diaCode = main(x)
    #     print(f"Diagnostic Code: {diaCode}")
    main(output)
