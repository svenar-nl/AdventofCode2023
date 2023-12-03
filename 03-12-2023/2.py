file_path = "input.txt"


def calculate(lines):
    gear_symbols = "*"
    total = 0

    char_lines = [[c for c in line] for line in lines]
    width = len(char_lines[0])
    height = len(char_lines)

    number_buffer = []

    for y in range(height):
        for x in range(width):
            if char_lines[y][x] == gear_symbols:
                gear_part_numbers = []
                for y1 in range(-1, 2):
                    for x1 in range(-1, 2):
                        if y1 == 0 and x1 == 0:
                            continue

                        if 0 <= y + y1 < height and 0 <= x + x1 < width:
                            if char_lines[y + y1][x + x1].isdigit():
                                found_num = ""

                                x2 = x + x1
                                while x2 >= 0 and char_lines[y + y1][x2].isdigit():
                                    x2 -= 1

                                x2 += 1
                                while x2 < width and char_lines[y + y1][x2].isdigit():
                                    found_num += char_lines[y + y1][x2]
                                    char_lines[y + y1][x2] = "?"
                                    x2 += 1
                                
                                gear_part_numbers.append(int(found_num))
                
                number_buffer.append(gear_part_numbers)
    
    for gear_pn in number_buffer:
        if len(gear_pn) == 2:
            total += gear_pn[0] * gear_pn[1]

    return total


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

    output = calculate(lines)
    print("Answer:", output)
