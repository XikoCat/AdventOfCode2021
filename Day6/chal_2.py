# https://adventofcode.com/2021/day/6

input = "Day6/input.txt"


def simulateDay(pool: list):
    childs = pool[0]
    for i in range(len(pool) - 1):
        pool[i] = pool[i + 1]
    pool[6] += childs
    pool[8] = childs
    return pool


def sum_number_list(list):
    count = 0
    for value in list:
        count += value
    return count


def main():
    with open(input) as f:
        lanternfish = [int(i) for i in f.readline().strip().split(",")]

    age_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in lanternfish:
        age_count[fish] += 1

    # print(0, sum_number_list(age_count), age_count)

    for day in range(256):
        age_count = simulateDay(age_count)
        # print(day + 1, sum_number_list(age_count), age_count)

    print(sum_number_list(age_count))


if __name__ == "__main__":
    main()
