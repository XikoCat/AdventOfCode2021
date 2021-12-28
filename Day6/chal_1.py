# https://adventofcode.com/2021/day/6

input = "Day6/input.txt"


def simulateDay(pool: list):
    child_count = 0
    for index, fish in enumerate(pool):
        if fish == 0:
            child_count += 1
            pool[index] = 6
        else:
            pool[index] -= 1

    while child_count > 0:
        pool.append(8)
        child_count -= 1

    return pool


def main():
    with open(input) as f:
        lanternfish = [int(i) for i in f.readline().strip().split(",")]

    # print(lanternfish)

    for day in range(80):
        lanternfish = simulateDay(lanternfish)
        # print(day, len(lanternfish))

    print(len(lanternfish))


if __name__ == "__main__":
    main()
