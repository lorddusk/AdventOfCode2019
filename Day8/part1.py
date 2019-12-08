from functions.utils import getInput


def main(input, width, height):
    i = 0
    layerList = []
    for layer in chunks(input, (width * height)):
        zero = 0
        one = 0
        two = 0
        for chunk in chunks(layer, width):
            for digit in chunk:
                if digit == '0':
                    zero += 1
                if digit == '1':
                    one += 1
                if digit == '2':
                    two += 1
        layer = {
            "layer": i,
            "0": zero,
            "1": one,
            "2": two
        }
        layerList.append(layer)
        i += 1
    layerList = sorted(layerList, key=lambda zero: zero['0'])
    print(layerList[0]['1'] * layerList[0]['2'])

def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    for start in range(0, len(s), n):
        yield s[start:start + n]


if __name__ == '__main__':
    input = getInput("day8")
    width = 25
    height = 6
    main(input, width, height)
