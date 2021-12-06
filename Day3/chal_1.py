input = "input.txt"


def getMostCommonOnColumn(lst, pos):
    count_0 = count_1 = 0
    for i in lst:
        if str(i)[pos] == '0':
            count_0 += 1
        if str(i)[pos] == '1':
            count_1 += 1
    return '0' if count_0 > count_1 else '1'


def getGamma(lst):
    gamma = ""
    for i in range(len(lst[0])):
        gamma += getMostCommonOnColumn(lst, i)
    return gamma


def getEpsilon(lst):
    gamma = getGamma(lst)
    epsilon = ""
    for c in gamma:
        if c == '0':
            epsilon += '1'
        if c == '1':
            epsilon += '0'
    return epsilon


def main():
    with open(input) as f:
        diagnostic = [i.replace("\n", "") for i in f.readlines()]

    gamma = int(getGamma(diagnostic), 2)
    epsilon = int(getEpsilon(diagnostic), 2)
    print(gamma * epsilon)


if __name__ == "__main__":
    main()
