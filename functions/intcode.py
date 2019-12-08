from functions.utils import debug


def param(mode, pos, _input, n, inc):
    parameter = int(mode[n])
    if n != 0:
        if parameter == 0:
            input1 = _input[_input[(pos + inc)]]
        elif parameter == 1:
            input1 = _input[(pos + inc)]
        else:
            input1 = None
    else:
        if parameter == 0:
            input1 = _input[(pos + inc)]
        elif parameter == 1:
            input1 = (pos + inc)
        else:
            input1 = None
    return int(input1)


def execIntCodeEight(_input, mode, pos):
    input1 = param(mode, pos, _input, 2, 1)
    input2 = param(mode, pos, _input, 1, 2)
    outputPos = param(mode, pos, _input, 0, 3)
    if input1 == input2:
        _input[outputPos] = 1
    else:
        _input[outputPos] = 0
    pos += 4
    return pos


def execIntCodeSeven(_input, mode, pos):
    input1 = param(mode, pos, _input, 2, 1)
    input2 = param(mode, pos, _input, 1, 2)
    outputPos = param(mode, pos, _input, 0, 3)
    if input1 < input2:
        _input[outputPos] = 1
    else:
        _input[outputPos] = 0
    pos += 4
    return pos


def execIntCodeSix(_input, mode, pos):
    input1 = param(mode, pos, _input, 2, 1)
    if input1 == 0:
        input2 = param(mode, pos, _input, 1, 2)
        pos = input2
    else:
        pos += 3
    return pos


def execIntCodeFive(_input, mode, pos):
    input1 = param(mode, pos, _input, 2, 1)
    if input1 != 0:
        input2 = param(mode, pos, _input, 1, 2)
        pos = input2
    else:
        pos += 3
    return pos


def execIntCodeFour(_input, mode, pos):
    output = param(mode, pos, _input, 2, 1)
    pos += 2
    if _input[pos] == 99:
        debug(f"ENDING LOOP")
        return output
    else:
        return pos, output


def execIntCodeThree(_input, pos, thruster, prevOutput):
    if pos == 0:
        instruction = int(thruster)
    else:
        instruction = int(prevOutput)
    outputTo = _input[(pos + 1)]
    _input[outputTo] = instruction
    pos += 2
    return pos


def execIntCodeTwo(_input, mode, pos):
    input1 = param(mode, pos, _input, 2, 1)
    input2 = param(mode, pos, _input, 1, 2)
    output = (input1 * input2)
    outputPos = param(mode, pos, _input, 0, 3)
    _input[outputPos] = output
    pos += 4
    return pos


def execIntCodeOne(_input, mode, pos):
    input1 = param(mode, pos, _input, 2, 1)
    input2 = param(mode, pos, _input, 1, 2)
    output = (input1 + input2)
    outputPos = param(mode, pos, _input, 0, 3)
    _input[outputPos] = output
    pos += 4
    return pos
