file_path = "input.txt"


def parse_input(data):
    almanac = {}
    current_section = None

    for line in data:
        if not line.strip():
            continue

        parts = line.split(":")

        if "seeds" in parts[0]:
            almanac[parts[0]] = [parts[1].split()]
        else:
            if len(parts) == 2:
                current_section = parts[0].replace(" map", "").strip()
                almanac[current_section] = []
            elif current_section:
                almanac[current_section].append(parts[0].split())
    return almanac


def check_convert_map(seed, conversion_map):
    seed = int(seed)
    match = next(
        (
            (int(line[0]) + (seed - int(line[1])))
            for line in conversion_map
            if int(line[1]) <= seed < (int(line[1]) + int(line[2]))
        ),
        seed,
    )
    return match if match is not seed else seed


def calculate(lines):
    parsed_data = parse_input(lines)

    lowest = float("inf")

    for seed in parsed_data["seeds"][0]:
        curr_soil = int(seed)

        for current_section in parsed_data.keys():
            if current_section != "seeds":
                curr_soil = check_convert_map(curr_soil, parsed_data[current_section])

        lowest = min(lowest, curr_soil)

    return lowest


def main(lines):
    output = calculate(lines)
    print("Answer:", output)


if __name__ == "__main__":
    with open(file_path, "r") as file:
        lines = file.readlines()

    # lines = [
    #     "seeds: 79 14 55 13",
    #     "",
    #     "seed-to-soil map:",
    #     "50 98 2",
    #     "52 50 48",
    #     "",
    #     "soil-to-fertilizer map:",
    #     "0 15 37",
    #     "37 52 2",
    #     "39 0 15",
    #     "",
    #     "fertilizer-to-water map:",
    #     "49 53 8",
    #     "0 11 42",
    #     "42 0 7",
    #     "57 7 4",
    #     "",
    #     "water-to-light map:",
    #     "88 18 7",
    #     "18 25 70",
    #     "",
    #     "light-to-temperature map:",
    #     "45 77 23",
    #     "81 45 19",
    #     "68 64 13",
    #     "",
    #     "temperature-to-humidity map:",
    #     "0 69 1",
    #     "1 0 69",
    #     "",
    #     "humidity-to-location map:",
    #     "60 56 37",
    #     "56 93 4",
    # ]

    main(lines)
