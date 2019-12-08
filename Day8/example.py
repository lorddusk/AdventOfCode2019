def main(input, width, height):
    i = 1
    for layer in chunks(input, (width * height)):
        print(f"Layer: {i}")
        for chunk in chunks(layer, width):
            print(chunk)
        i += 1


def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    for start in range(0, len(s), n):
        yield s[start:start + n]


if __name__ == '__main__':
    example = "123456789012"
    width = 3
    height = 2
    main(example, width, height)
