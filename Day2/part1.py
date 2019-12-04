def main(input):
    input[1] = 12
    input[2] = 2
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
            print(pos)
        elif intCode == 2:
            input1 = input[input[(pos + 1)]]
            input2 = input[input[(pos + 2)]]
            output = (input1 * input2)
            outputPos = input[(pos + 3)]
            input[outputPos] = output
            pos += 4
            print(pos)
        else:
            pos += 1
            print(pos)
    print(input)


if __name__ == '__main__':
    f = open('in/input.txt', 'r')
    input = f.readline().strip()
    output = []
    input = input.split(',')
    for x in input:
        output.append(int(x))
    main(output)