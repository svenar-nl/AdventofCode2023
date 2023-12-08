file_path = "input.txt"

POSITIONS = {
    "Start": "AAA",
    "End": "ZZZ"
}

def parse_input(lines):
    instructions = []
    path = {}

    for instruction in lines[0].strip():
        instructions.append(instruction)

    for index in range(1, len(lines)):
        line = lines[index].strip()

        if line == "":
            continue

        position = line.split(" = ")[0]
        L, R = line.split(" = ")[1].replace("(", "").replace(")", "").split(", ")
        path[position] = {"L": L, "R": R}

    return instructions, path

def find_position_index(path, position):
    for i, path_part in enumerate(path):
        if path_part == position:
            return i
    
    return -1

def calculate(lines):
    answer = 0

    instructions, path = parse_input(lines)

    current_position_index = find_position_index(path, POSITIONS["Start"])
    
    
    current_instruction_index = 0
    while list(path.keys())[current_position_index] != POSITIONS["End"]:
        current_instruction = instructions[current_instruction_index % len(instructions)]
        current_position = list(path.keys())[current_position_index]

        current_position_index = find_position_index(path, path[current_position][current_instruction])

        # print(f"{current_instruction} | {current_position} -> {path[current_position][current_instruction]}")

        current_instruction_index += 1
        answer += 1

    return answer


def main(lines):
    output = calculate(lines)
    print("Answer:", output)


if __name__ == "__main__":
    with open(file_path, "r") as file:
        lines = file.readlines()

    # lines = ["LLR", "", "AAA = (BBB, BBB)", "BBB = (AAA, ZZZ)", "ZZZ = (ZZZ, ZZZ)"]

    main(lines)
