input = "input.txt"


def getMostCommonOnColumn(lst, pos):
    count_0 = count_1 = 0
    for i in lst:
        if str(i)[pos] == '0':
            count_0 += 1
        if str(i)[pos] == '1':
            count_1 += 1
    return '0' if count_0 > count_1 else '1'


def seiveList(lst, pos, char):
    """Keep only the elements where char is in the pos"""
    new_lst = []
    for element in lst:
        if str(element)[pos] == char:
            new_lst.append(element)
    if len(new_lst) == 0:
        return [lst[-1]]
    return new_lst

def getOxigenRating(lst):
    for i in range(len(lst[0])):
        if len(lst) == 1:
            return lst[0]
        mostCommon = getMostCommonOnColumn(lst, i)
        lst = seiveList(lst, i, mostCommon)
    return lst[0]

def getScrubberRating(lst):
    for i in range(len(lst[0])):
        if len(lst) == 1:
            return lst[0]
        mostCommon = getMostCommonOnColumn(lst, i)
        lst = seiveList(lst, i, '0' if mostCommon == '1' else '1')
    return lst[0]

def main():
    with open(input) as f:
        diagnostic = [i.replace("\n", "") for i in f.readlines()]

    oxigen = int(getOxigenRating(diagnostic), 2)
    scrubber = int(getScrubberRating(diagnostic), 2)
    print(oxigen * scrubber)


if __name__ == "__main__":
    main()
