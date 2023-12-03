file_path = "input.txt"

def extract_digit(char_lines, x, y):
    found_num = ""
    x2 = x

    while x2 >= 0 and char_lines[y][x2].isdigit():
        found_num = char_lines[y][x2] + found_num
        x2 -= 1

    x2 = x + 1
    while x2 < len(char_lines[y]) and char_lines[y][x2].isdigit():
        found_num += char_lines[y][x2]
        char_lines[y][x2] = "?"
        x2 += 1

    return int(found_num)


def find_gear_part_numbers(char_lines, x, y):
    gear_part_numbers = []

    for y1 in range(-1, 2):
        for x1 in range(-1, 2):
            if y1 == 0 and x1 == 0:
                continue

            if 0 <= y + y1 < len(char_lines) and 0 <= x + x1 < len(char_lines[y]):
                if char_lines[y + y1][x + x1].isdigit():
                    digit = extract_digit(char_lines, x + x1, y + y1)
                    gear_part_numbers.append(digit)

    return gear_part_numbers


def calculate_gear_total(char_lines):
    gear_symbols = "*"
    total = 0
    number_buffer = []

    for y in range(len(char_lines)):
        for x in range(len(char_lines[y])):
            if char_lines[y][x] == gear_symbols:
                gear_part_numbers = find_gear_part_numbers(char_lines, x, y)
                number_buffer.append(gear_part_numbers)

    for gear_pn in number_buffer:
        if len(gear_pn) == 2:
            total += gear_pn[0] * gear_pn[1]

    return total


def main(lines):
    char_lines = [[c for c in line] for line in lines]
    output = calculate_gear_total(char_lines)
    print("Answer:", output)


if __name__ == "__main__":
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    # lines = [
    #     "467..114..",
    #     "...*......",
    #     "..35..633.",
    #     "......#...",
    #     "617*......",
    #     ".....+.58.",
    #     "..592.....",
    #     "......755.",
    #     "...$.*....",
    #     ".664.598..",
    # ]
    main(lines)