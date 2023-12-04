file_path = "input.txt"

def calculate(lines):
    output = 0

    for line in lines:
        card_id = line.split(":")[0].split(" ")[1]
        winning_numbers = [int(num) for num in line.split(" | ")[0].split(": ")[1].lstrip().rstrip().replace("  ", " ").split(" ")]
        your_numbers = [int(num) for num in line.split(" | ")[1].lstrip().rstrip().replace("  ", " ").split(" ")]

        points = 0

        for num in your_numbers:
            if num in winning_numbers:
                points += 1 if points == 0 else points * 2 - points
        
        output += points

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
