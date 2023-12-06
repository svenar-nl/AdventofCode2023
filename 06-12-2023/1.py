import math

file_path = "input.txt"


def calculate(lines):
    race_durations = [int(value) for value in lines[0].split()[1:]]

    race_records = [int(value) for value in lines[1].split()[1:]]

    sum = 1
    for i in range(0, len(race_durations)):
        duration = race_durations[i]
        record = race_records[i]
        a = -1
        b = duration
        c = -record
        discriminant = math.sqrt(b**2 - 4 * a * c)
        x1 = math.floor((duration + discriminant) / (2 * a))
        x2 = math.ceil((duration - discriminant) / (2 * a)) - 1
        sum *= abs(x2 - x1)

    return sum


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
