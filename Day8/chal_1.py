# https://adventofcode.com/2021/day/8

input = "Day8/input.txt"


def countLengths(arr: list, lenght: int):
    count = 0
    for s in arr:
        count += 1 if len(s) == lenght else 0
    return count


def main():
    sequences = []
    with open(input) as f:
        for line in f.readlines():
            line = line.strip().split(" ")
            sample, code = [], []
            for i in range(10):
                sample.append(line[i])
            for i in range(4):
                code.append(line[i + 11])
            sample.sort(key=len)
            sequences.append([sample, code])

    print(sequences)

    count = 0

    for seq in sequences:
        count += countLengths(seq[1], 2)  # count 1's
        count += countLengths(seq[1], 4)  # count 4's
        count += countLengths(seq[1], 3)  # count 7's
        count += countLengths(seq[1], 7)  # count 8's

    print(count)


if __name__ == "__main__":
    main()
