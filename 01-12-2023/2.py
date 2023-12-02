file_path = "input.txt"

text_digits = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6, 
    "seven": 7,
    "eight": 8,
    "nine": 9

}

def parse_first_digit(input_string):
    ret_val = 0

    if input_string[0].isdigit():
        ret_val = int(input_string[0])
    else:
        for word in text_digits.keys():
            word_index = input_string.find(word)
            if word_index == 0:
                ret_val = text_digits[word]
                break
        if ret_val == 0 and word != "zero":
            ret_val = parse_first_digit(input_string[1:])

    return ret_val

def parse_last_digit(input_string):
    ret_val = 0

    if input_string[-1].isdigit():
        ret_val = int(input_string[-1])
    else:
        for word in text_digits.keys():
            word_index = input_string[::-1].find(word[::-1])
            if word_index == 0:
                ret_val = text_digits[word]
                break
        if ret_val == 0 and word != "zero":
            ret_val = parse_last_digit(input_string[:-1])

    return ret_val

def extract_calibration_values(lines):
    total_calibration = 0
    
    for line in lines:
        calibration_value = int(str(parse_first_digit(line)) + str(parse_last_digit(line)))
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