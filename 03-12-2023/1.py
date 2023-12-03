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


def find_engine_part_numbers(char_lines, x, y, width, height):
    engine_part_numbers = []

    for y1 in range(-1, 2):
        for x1 in range(-1, 2):
            if y1 == 0 and x1 == 0:
                continue

            if 0 <= y + y1 < height and 0 <= x + x1 < width:
                if char_lines[y + y1][x + x1].isdigit():
                    digit = extract_digit(char_lines, x + x1, y + y1)
                    engine_part_numbers.append(digit)

    return engine_part_numbers


def calculate_engine_total(char_lines):
    engine_symbols = "@#$%&*+/=-"
    total = 0
    number_buffer = []

    width = len(char_lines[0])
    height = len(char_lines)

    for y in range(height):
        for x in range(width):
            if char_lines[y][x] in engine_symbols:
                engine_part_numbers = find_engine_part_numbers(char_lines, x, y, width, height)
                number_buffer.extend(engine_part_numbers)

    total = sum(number_buffer)
    return total

def main(lines):
    char_lines = [[c for c in line] for line in lines]
    output = calculate_engine_total(char_lines)
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
