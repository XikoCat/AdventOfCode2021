import numpy as np
from numpy.core.numeric import count_nonzero

input = "Day5/input.txt"
array_side = 1000

def count_dangerous(numpy_array):
    count = 0
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array)):
            if numpy_array[i][j] > 1: count += 1
    return count


def map_vents(lines_list):
    vents_map = np.zeros((array_side, array_side))
    for line in lines_list:
        x1, y1, x2, y2 = line
        
        # If line is not horizontal or vertical, Ignore it
        if x1 != x2 and y1 != y2:
            continue
        
        vents_map[x2][y2] += 1
        while x1 != x2 or y1 != y2:
            vents_map[x1][y1] += 1
            dx = x2 - x1
            dy = y2 - y1
            if dx != 0:
                x1 += int(dx / abs(dx))
            if dy != 0:
                y1 += int(dy / abs(dy))
    return vents_map


def main():
    with open(input) as f:
        lines = [i.strip().replace(' -> ',',') for i in f.readlines()]

    lines_list = []
    for line in lines:
        parsed_line = [int(i) for i in line.split(',')]
        lines_list.append(parsed_line)

    
    vents_map = map_vents(lines_list)
    danger_count = count_dangerous(vents_map)

    print(danger_count)

if __name__ == "__main__":
    main()
