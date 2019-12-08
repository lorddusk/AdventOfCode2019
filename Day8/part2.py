from functions.utils import getInput

width = 25
height = 6
size = width * height

def main(input):
    image = ["2"] * size
    for i in range(len(input) // size):
        layer = input[i * size: (i + 1) * size]
        for j, pixel in enumerate(layer):
            if image[j] == "2":
                image[j] = pixel

    colors = {"0": " ", "1": "#"}
    image = "".join(colors[pixel] for pixel in image)
    for i in range(height):
        print(image[i * width: (i + 1) * width])

if __name__ == '__main__':
    input = getInput("day8")
    main(input)
