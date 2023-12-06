import math

file_path = "input.txt"


def calculate(lines):
    duration = int(lines[0].replace(" ", "").split(":")[1])

    record = int(lines[1].replace(" ", "").split(":")[1])

    a = -1
    b = duration
    c = -record
    discriminant = math.sqrt(b**2 - 4 * a * c)
    x1 = math.floor((duration + discriminant) / (2 * a))
    x2 = math.ceil((duration - discriminant) / (2 * a)) - 1

    return abs(x2 - x1)


def main(lines):
    output = calculate(lines)
    print("Answer:", output)


if __name__ == "__main__":
    with open(file_path, "r") as file:
        lines = file.readlines()

    # lines = [
    #     "Time:      7  15   30",
    #     "Distance:  9  40  200"
    # ]

    main(lines)
