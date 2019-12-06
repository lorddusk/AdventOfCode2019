def getInput(fileName = "input"):
    with open(f'in/{fileName}.txt', 'r') as f:
        raw_input = f.read()
    return raw_input

def debug(msg):
    print(f"DEBUG: {msg}")