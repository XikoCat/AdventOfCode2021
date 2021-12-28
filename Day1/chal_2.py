# https://adventofcode.com/2021/day/1

input = "input.txt"


def sumAdjacent(list, start, sumCount):
    value = 0
    for i in range(start, start + sumCount):
        value += list[i]
    return value


def countIncreaseWithSum(list, sumCount):
    count = 0
    last = sumAdjacent(list, 0, sumCount)
    for i in range(1, len(list) - sumCount + 1):
        current = sumAdjacent(list, i, sumCount)
        if last < current:
            count += 1
        last = current
    return count


def main():
    with open(input) as f:
        content = [int(i) for i in f.readlines()]

    print(countIncreaseWithSum(content, 3))


if __name__ == "__main__":
    main()
