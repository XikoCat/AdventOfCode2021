# https://adventofcode.com/2021/day/1

input = "input.txt"


def countIncrease(list):
    count = 0
    last = list[0]
    for i in range(1, len(list)):
        if last < list[i]:
            count += 1
        last = list[i]
    return count


def main():
    with open(input) as f:
        content = [int(i) for i in f.readlines()]

    print(countIncrease(content))


if __name__ == "__main__":
    main()
