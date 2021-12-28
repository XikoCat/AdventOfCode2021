# https://adventofcode.com/2021/day/2

input = "input.txt"


def locate(instructions):
    h_pos = aim = depth = 0
    for order, value in instructions:
        if str(order).find("down") == 0:
            aim += value
            continue
        if str(order).find("up") == 0:
            aim -= value
            continue
        if str(order).find("forward") == 0:
            h_pos += value
            depth += aim * value
            continue
    return h_pos, depth


def main():
    with open(input) as f:
        instructions = [i.replace("\n", "").split(" ") for i in f.readlines()]
        for id, item in enumerate(instructions):
            instructions[id] = [item[0], int(item[1])]

    pos = locate(instructions)
    print(pos[0] * pos[1])


if __name__ == "__main__":
    main()
