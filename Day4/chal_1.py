# https://adventofcode.com/2021/day/4

input = "input.txt"


def cardSum(card):
    result = 0
    for line in card:
        for number in line:
            if str(number).find("x") == -1:
                result += number
    return result


def cardWins(card):
    for i in range(len(card)):
        count_x = count_y = 0
        for j in range(len(card[i])):
            if str(card[i][j]).find("x") == 0:
                count_y += 1
            if str(card[j][i]).find("x") == 0:
                count_x += 1
            if count_x == 5 or count_y == 5:
                return True
    return False


def playCard(card, call):
    for i in range(len(card)):
        for j in range(len(card[i])):
            if card[i][j] == call:
                card[i][j] = "x"
                return cardWins(card)
    return False


def getBingoWinner(calls, cards):
    for call in calls:
        for card in cards:
            if playCard(card, call):
                return card, call


def main():
    with open(input) as f:
        bingo = [i.strip() for i in f.readlines()]
    calls = [int(c) for c in bingo.pop(0).split(",")]
    cards = card = []
    for i in range(len(bingo)):
        if bingo[i] == "":
            if len(card) == 5:
                cards.append(card)
            card = []
        else:
            line = str(bingo[i]).split(" ")
            while len(line) > 5:
                line.remove("")
            card.append([int(j) for j in line])

    winner, call = getBingoWinner(calls, cards)

    print(cardSum(winner) * call)


if __name__ == "__main__":
    main()
