file_path = "input.txt"

def parse_input(lines):
    instructions = []
    path = {}
    starts = []
    ends = []

    for instruction in lines[0].strip():
        instructions.append(instruction)

    for index in range(1, len(lines)):
        line = lines[index].strip()

        if line == "":
            continue

        position = line.split(" = ")[0]
        L, R = line.split(" = ")[1].replace("(", "").replace(")", "").split(", ")
        path[position] = {"L": L, "R": R}

        if position.endswith("A"):
            starts.append(position)
        if position.endswith("Z"):
            ends.append(position)

    return instructions, path, starts, ends


def find_position_index(path, position):
    for i, path_part in enumerate(path):
        if path_part == position:
            return i

    return -1

def calculate(lines):
    def gcd(num1, num2):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1

    def get_frequency(start, path, instructions):
        step_count, step_ptr = 0, 0
        while True:
            step_count += 1
            next_pair = path[start]
            start = next_pair["L"] if instructions[step_ptr] == 'L' else next_pair["R"]
            if start in ends:
                return step_count
            step_ptr = (step_ptr + 1) % len(instructions)

    instructions, path, starts, ends = parse_input(lines)
    frequencies = [get_frequency(curnode, path, instructions) for curnode in starts]

    answer = 1
    for freq in frequencies:
        answer = (answer * freq) // gcd(answer, freq)

    return answer


def main(lines):
    output = calculate(lines)
    print("Answer:", output)


if __name__ == "__main__":
    with open(file_path, "r") as file:
        lines = file.readlines()

    # lines = [
    #     "LR",
    #     "",
    #     "11A = (11B, XXX)",
    #     "11B = (XXX, 11Z)",
    #     "11Z = (11B, XXX)",
    #     "22A = (22B, XXX)",
    #     "22B = (22C, 22C)",
    #     "22C = (22Z, 22Z)",
    #     "22Z = (22B, 22B)",
    #     "XXX = (XXX, XXX)",
    # ]

    main(lines)
