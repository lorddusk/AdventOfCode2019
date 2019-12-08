from functions.utils import getInput


def main(input):
    input[1] = 41
    input[2] = 12
    pos = 0
    intCode = 0
    while (intCode != 99):
        intCode = input[pos]
        if intCode == 1:
            input1 = input[input[(pos + 1)]]
            input2 = input[input[(pos + 2)]]
            output = (input1 + input2)
            outputPos = input[(pos + 3)]
            input[outputPos] = output
            pos += 4
        elif intCode == 2:
            input1 = input[input[(pos + 1)]]
            input2 = input[input[(pos + 2)]]
            output = (input1 * input2)
            outputPos = input[(pos + 3)]
            input[outputPos] = output
            pos += 4
        else:
            pos += 1
    print(100*input[1]+input[2])


if __name__ == '__main__':
    input = getInput()
    output = []
    input = input.split(',')
    for x in input:
        output.append(int(x))
    main(output)