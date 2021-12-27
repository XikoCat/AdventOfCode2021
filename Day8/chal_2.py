input = "Day8/input.txt"

def decodeSample(seq:list):
    numbers = [None]*10
    segments = [None]*7

    sample = list(seq[0])[:]
    sample.sort(key=len)
    for key, elem in enumerate(sample):
        sample[key] = ''.join(sorted(elem))

    #1: only element of 2 segments
    numbers[1] = sample.pop(0)

    #7: only element of 3 segments
    numbers[7] = sample.pop(0)

    #a: only segment that is part of #7 but not of #1
    segments[0] = numbers[7].replace(numbers[1][0], '').replace(numbers[1][1], '')

    #4: only element of 4 segments
    numbers[4] = sample.pop(0)

    #8: only element of 7 segments
    numbers[8] = sample.pop(6)

    #6: only element of 6 segments that is missing a segment of #1
    #c: segment of #1 missing in #6
    for ele in sample:
        if len(ele) == 6:
            if str(ele).find(numbers[1][0]) == -1:
                numbers[6] = ele
                sample.remove(ele)
                segments[2] = numbers[1][0]
                break
            if str(ele).find(numbers[1][1]) == -1:
                numbers[6] = ele
                sample.remove(ele)
                segments[2] = numbers[1][1]
                break
    
    #f: segment of #1 that is not #c
    segments[5] = numbers[1].replace(segments[2] ,'')



    #5: only # of 5 segments missing #c
    for ele in sample:
        if len(ele) == 5:
            if str(ele).find(segments[2]) == -1:
                numbers[5] = ele
                sample.remove(ele)
                break

    #e: segment of #6 missing on #5
    segments[4] = numbers[6]
    for char in numbers[5]:
        segments[4] = segments[4].replace(char, '')

    #9: #8 - #e
    numbers[9] = numbers[8].replace(segments[4],'')
    sample.remove(numbers[9])

    #0: only element with 6 segments left
    numbers[0] = sample.pop()

    #2: only element left that contains #e
    numbers[2] = sample.pop() if sample[1].find(segments[4]) != -1 else sample.pop(0)

    #3: only element left
    numbers[3] = sample.pop()

    seq[0] = numbers

def decodeCode(seq:list):
    code = ''
    for key, elem in enumerate(seq[1]):
        seq[1][key] = ''.join(sorted(elem))
        number = list(seq[0]).index(seq[1][key])
        code += str(number)
    return int(code, 10)

def main():
    sequences = []
    with open(input) as f:
        for line in f.readlines():
            line = line.strip().split(' ')
            sample, code = [], []
            for i in range(10):
                sample.append(line[i])
            for i in range(4):
                code.append(line[i + 11])
            sequences.append([sample, code])

    result = 0

    for seq in sequences:
        decodeSample(seq)
        result += decodeCode(seq)
    
    print(result)

if __name__ == "__main__":
    main()
