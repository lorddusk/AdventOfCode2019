from functions.utils import getInput
from collections import defaultdict
from anytree import Node, Walker

def main(raw_input):
    map = defaultdict(list)
    mapTree = set()
    tree = {}
    for item in raw_input.strip().split('\n'):
        satellite, child = item.split(')')
        mapTree.add(satellite)
        mapTree.add(child)
        map[satellite].append(child)
    for i in mapTree:
        tree[i] = Node(i)

    for satellite, children in map.items():
        tree[satellite].children = [tree[child] for child in children]

    YOU = tree['YOU']
    SAN = tree['SAN']

    W = Walker()
    up, common, down = W.walk(YOU, SAN)
    return (len(up) + len(down) - 2) # -2 because you don't count the orbital jumps between YOU and SAN

if __name__ == '__main__':
    raw_input = getInput("input")
    totalJumps = main(raw_input)
    print(f"Total Jumps From YOU to SAN: {totalJumps}")