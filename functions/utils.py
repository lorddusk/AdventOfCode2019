def getInput(fileName = "input"):
    with open(f'../inputs/{fileName}.txt', 'r') as f:
        raw_input = f.read()
    return raw_input.strip()

def debug(msg):
    print(f"DEBUG: {msg}")