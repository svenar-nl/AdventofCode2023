file_path = "input.txt"

def calculate(lines):
    output = len(lines)

    extra_card_numbers = []
    card_points = {}

    for line in lines:
        card_id = int(line.split(":")[0].split("Card")[1].lstrip().rstrip())
        winning_numbers = [int(num) for num in line.split(" | ")[0].split(": ")[1].lstrip().rstrip().replace("  ", " ").split(" ")]
        your_numbers = [int(num) for num in line.split(" | ")[1].lstrip().rstrip().replace("  ", " ").split(" ")]

        num_matches = 0

        for num in your_numbers:
            if num in winning_numbers:
                num_matches += 1
        
        card_points[card_id] = num_matches

        if num_matches > 0:
            for i in range(num_matches):
                extra_card_numbers.append(card_id + i + 1)

    pointer = 0
    while pointer < len(extra_card_numbers):
        card_id = extra_card_numbers[pointer]
        num_matches = card_points[card_id]

        if num_matches > 0:
            for i in range(num_matches):
                extra_card_numbers.append(card_id + i + 1)

        pointer += 1
    output += len(extra_card_numbers)
    return output

def main(lines):
    output = calculate(lines)
    print("Answer:", output)

if __name__ == "__main__":
    with open(file_path, "r") as file:
        lines = file.readlines()

    # lines = [
    #     "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    #     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    #     "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    #     "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    #     "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    #     "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
    # ]

    main(lines)
