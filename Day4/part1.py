from utils import getInput


def doubles(num):
    lastUsed = num[0]
    for i in range(1, len(num)):
        if num[i] == lastUsed:
            return True
        else:
            lastUsed = num[i]
    return False


def checkPass(current):
    currentString = str(current)
    if doubles(currentString):
        list = []
        for x in range(len(currentString)):
            if x != len(currentString) - 1:
                firstDigit = currentString[x]
                nextDigit = currentString[x + 1]
                if firstDigit == nextDigit or nextDigit > firstDigit:
                    list.append(True)
        if len(list) == 5:
            return 1
        else:
            return 0
    else:
        return 0


def main():
    raw_input = getInput()
    range = raw_input.split('-')
    minimum = int(range[0])
    maximum = int(range[1])
    current = minimum
    amount = 0
    while current != maximum + 1:
        check = checkPass(current)
        if check == 1:
            amount += 1
        current += 1
    print(amount)


if __name__ == '__main__':
    main()
