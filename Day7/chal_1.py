import math

input = "Day7/input.txt"

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
        if (max_count < Hash[i]):
            res = i
            max_count = Hash[i]
         
    return res

def costOfShift(arr, final_pos):
    cost = 0
    for pos in arr:
        cost += abs(final_pos - pos)
    return cost

def maxValue(arr: list):
    copy_arr = arr
    max = copy_arr.pop()
    for value in copy_arr:
        max = value if value > max else max
    return max

def minValue(arr: list):
    copy_arr = arr
    min = copy_arr.pop()
    for value in copy_arr:
        min = value if value < min else min
    return min

def main():
    with open(input) as f:
        positions = [int(i) for i in f.readline().strip().split(',')]

    #print(mostFrequent(positions), costOfShift(positions, mostFrequent(positions)))
    #first_guess = mostFrequent(positions)
    #cost = new_cost = costOfShift(positions, first_guess)
    #
    #shift = 0
    #while cost >= new_cost:
    #    cost = new_cost
    #    shift += 1
    #    high = costOfShift(positions, first_guess + shift)
    #    low = costOfShift(positions, first_guess - shift)
    #    new_cost = high if high < low else low
    #    print(first_guess, shift, new_cost)
    leftmost_pos = minValue(positions)
    rightmost_pos = maxValue(positions)

    cost = costOfShift(positions, leftmost_pos)
    for i in range(leftmost_pos + 1, rightmost_pos + 1):
        next = costOfShift(positions, i)


    print(cost)

if __name__ == "__main__":
    main()
