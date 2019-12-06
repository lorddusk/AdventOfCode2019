from utils import getInput
from collections import defaultdict
from anytree import Node

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

    totalOrbits = 0
    for node in tree:
        totalOrbits += tree[node].depth
    return totalOrbits

if __name__ == '__main__':
    raw_input = getInput("input")
    totalOrbits = main(raw_input)
    print(f"Total Orbits: {totalOrbits}")