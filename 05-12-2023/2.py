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


def convert_map_to_range(conversion_map):
    return sorted(
        [
            [int(line[1]), int(line[1]) + int(line[2]) - 1, int(line[0]) - int(line[1])]
            for line in conversion_map
        ],
        key=lambda x: x[0],
    )


def convert_seed_range_list(seed_range, conversion_range):
    seed_range_list = []
    curr_value = seed_range[0]

    for i in range(len(conversion_range)):
        if curr_value < conversion_range[i][0]:
            seed_range_list.append([int(curr_value), (int(conversion_range[i][0] - 1))])
            curr_value = int(conversion_range[i][0])

        if curr_value >= int(conversion_range[i][0]) and curr_value <= int(
            conversion_range[i][1]
        ):
            max_value = (
                int(conversion_range[i][1])
                if not int(seed_range[1]) <= int(conversion_range[i][1])
                else int(seed_range[1])
            )
            seed_range_list.append(
                [
                    (curr_value + conversion_range[i][2]),
                    (max_value + conversion_range[i][2]),
                ]
            )
            curr_value = max_value + 1

        if int(seed_range[1]) == curr_value - 1:
            break

    if curr_value < seed_range[1]:
        seed_range_list.append([curr_value, seed_range[1]])

    return sorted(seed_range_list, key=lambda x: x[0])


def calculate(lines):
    parsed_data = parse_input(lines)

    seeds = parsed_data["seeds"][0]
    seed_pairs = [
        (int(seeds[i]), int(seeds[i]) + int(seeds[i + 1]) - 1)
        for i in range(0, len(seeds), 2)
    ]

    conversion_maps = [cm for cm in parsed_data.keys() if cm != "seeds"]
    conversion_range_dict = {
        cm: convert_map_to_range(parsed_data[cm]) for cm in conversion_maps
    }

    lowest = float("inf")

    for seed_range in seed_pairs:
        curr_seed_range = [seed_range]

        for curr_conv_map in conversion_range_dict.keys():
            curr_output_list = [
                convert_seed_range_list(entry, conversion_range_dict[curr_conv_map])
                for entry in curr_seed_range
            ]
            curr_output_list = sorted(
                [item for sublist in curr_output_list for item in sublist],
                key=lambda x: x[0],
            )
            curr_seed_range = curr_output_list.copy()

        lowest = min(lowest, curr_seed_range[0][0])

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
