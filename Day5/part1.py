from utils import getInput


def inputer(message):
    return input(message)


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
    # output = [1002,4,3,4,33]
    # output = [1101,100,-1,4,0]
    # output = [104,2,99]
    main(output)
