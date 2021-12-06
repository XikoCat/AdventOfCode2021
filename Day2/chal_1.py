input = "input.txt"

def locate(instructions):
    x_pos = y_pos = 0
    for order, value in instructions:
        if str(order).find("forward") == 0:
            x_pos += value
            continue
        
        if str(order).find("up") == 0:
            y_pos -= value
            continue
        
        if str(order).find("down") == 0:
            y_pos += value
            continue

    return x_pos, y_pos

def main():
    with open(input) as f:
        instructions = [i.replace("\n","").split(" ") for i in f.readlines()]
        for id, item in enumerate(instructions):
            instructions[id] = [item[0],int(item[1])]

    pos = locate(instructions)
    print(pos, pos[0] * pos[1])

if __name__=="__main__":
    main()