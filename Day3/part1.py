from functions.utils import getInput


def run(route):
    route_info = {}
    xPos, yPos, count = 0, 0, 0
    movement = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
    for part in route:
        for _ in range(int(part[1:])):
            offset = movement[part[0]]
            xPos += offset[0]
            yPos += offset[1]
            count += 1
            route_info[(xPos, yPos)] = count
    return route_info


def solution(input):
    taxiRoutes = [x.split(',') for x in input.strip().split('\n')]

    route1 = run(taxiRoutes[0])
    route2 = run(taxiRoutes[1])

    crossings = route1.keys() & route2.keys()

    closest = min([x for x in crossings], key=lambda coords: abs(coords[0]) + abs(coords[1]))
    distance = abs(closest[0]) + abs(closest[1])

    return f'Closest: {distance}'


def main():
    raw_input = getInput()
    print(solution(raw_input))


if __name__ == '__main__':
    main()