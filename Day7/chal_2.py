# https://adventofcode.com/2021/day/7

import functools

input = "Day7/input.txt"


@functools.lru_cache()
def sumFromZeroTo(value: int):
    total = 0
    for i in range(value + 1):
        total += i
    return total


def mostFrequent(arr):
    # Insert all elements in Hash.
    Hash = dict()
    for i in range(len(arr)):
        if arr[i] in Hash.keys():
            Hash[arr[i]] += 1
        else:
            Hash[arr[i]] = 1

    # find the max frequency
    max_count = 0
    res = -1
    for i in Hash:
        if max_count < Hash[i]:
            res = i
            max_count = Hash[i]

    return res


def costOfShift(arr: list, final_pos: int):
    cost = 0
    for pos in arr:
        cost += sumFromZeroTo(abs(final_pos - pos))
    return cost


def main():
    with open(input) as f:
        positions = [int(i) for i in f.readline().strip().split(",")]

    # print(mostFrequent(positions), costOfShift(positions, mostFrequent(positions)))
    first_guess = mostFrequent(positions)
    cost = new_cost = costOfShift(positions, first_guess)

    shift = 0
    while cost >= new_cost:
        cost = new_cost
        shift += 1
        high = costOfShift(positions, first_guess + shift)
        low = costOfShift(positions, first_guess - shift)
        new_cost = high if high < low else low
    #    print(first_guess, shift, new_cost)

    print(cost)


if __name__ == "__main__":
    main()
