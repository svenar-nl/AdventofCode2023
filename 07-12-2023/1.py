from collections import Counter

file_path = "input.txt"

NUM_CARDS = 5

strength = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13,
}

card_combinations = {
    "FIVE_OF_A_KIND": 1,
    "FOUR_OF_A_KIND": 2,
    "FULL_HOUSE": 3,
    "THREE_OF_A_KIND": 4,
    "TWO_PAIR": 5,
    "ONE_PAIR": 6,
    "HIGH_CARD": 7,
}


def detect_type(list_card):
    counter = Counter(list_card)

    card_fequencies = [count for _, count in counter.most_common()]

    match card_fequencies:
        case [5]:
            return card_combinations["FIVE_OF_A_KIND"]
        case [4, 1]:
            return card_combinations["FOUR_OF_A_KIND"]
        case [3, 2]:
            return card_combinations["FULL_HOUSE"]
        case [3, 1, 1]:
            return card_combinations["THREE_OF_A_KIND"]
        case [2, 2, 1]:
            return card_combinations["TWO_PAIR"]
        case [2, 1, 1, 1]:
            return card_combinations["ONE_PAIR"]
        case _:
            return card_combinations["HIGH_CARD"]


class Hand:
    card: str = None
    label: int = None
    bid: int = None

    def __init__(self, card, bid):
        self.card = card
        self.label = detect_type(self.card)
        self.bid = bid

    def __lt__(self, other: "Hand"):
        if self.label != other.label:
            return self.label < other.label

        for i in range(NUM_CARDS):
            if self.card[i] != other.card[i]:
                return strength[self.card[i]] > strength[other.card[i]]


def calculate(lines):
    answer = 0

    inputs = [
        (line.split(" ")[0].strip(), int(line.split(" ")[1].strip())) for line in lines
    ]

    hands = []
    for card, bid in inputs:
        hand = Hand(card, bid)
        hands.append(hand)

    hands.sort(reverse=True)

    for i, hand in enumerate(hands):
        rank = i + 1
        answer += hand.bid * rank

    return answer


def main(lines):
    output = calculate(lines)
    print("Answer:", output)


if __name__ == "__main__":
    with open(file_path, "r") as file:
        lines = file.readlines()

    # lines = ["T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]

    main(lines)
