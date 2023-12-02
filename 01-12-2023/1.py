file_path = "input.txt"


def extract_calibration_values(lines):
    total_calibration = 0
    
    for line in lines:
        first_digit = next(char for char in line if char.isdigit())
        last_digit = next(char for char in reversed(line) if char.isdigit())
        calibration_value = int(first_digit + last_digit)
        total_calibration += calibration_value
    
    return total_calibration

if __name__ == "__main__":
    with open(file_path, "r") as file:
        lines = file.readlines()

    # lines = [
    #     "two1nine",
    #     "eightwothree",
    #     "abcone2threexyz",
    #     "xtwone3four",
    #     "4nineeightseven2",
    #     "zoneight234",
    #     "7pqrstsixteen"
    # ]

    total_calibration = extract_calibration_values(lines)
    print("Total Calibration Value:", total_calibration)