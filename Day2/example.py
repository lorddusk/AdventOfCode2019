examples = [[1,9,10,3,2,3,11,0,99,30,40,50],[1,0,0,0,99],[2,3,0,3,99],[2,4,4,5,99,0],[1,1,1,4,99,5,6,0,99]]

def main():
    for example in examples:
        pos = 0
        intCode = 0
        while (intCode != 99):
            intCode = example[pos]
            if intCode == 1:
                input1 = example[example[(pos + 1)]]
                input2 = example[example[(pos + 2)]]
                output = (input1 + input2)
                outputPos = example[(pos + 3)]
                example[outputPos] = output
                pos += 4
            if intCode == 2:
                input1 = example[example[(pos + 1)]]
                input2 = example[example[(pos + 2)]]
                output = (input1 * input2)
                outputPos = example[(pos + 3)]
                example[outputPos] = output
                pos += 4
        print(example)



if __name__ == '__main__':
    main()