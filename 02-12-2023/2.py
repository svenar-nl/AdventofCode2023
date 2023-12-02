file_path = "input.txt"

bag_contents = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def check_possible_games(lines):
    total_power = 0

    for line in lines:
        game_id = int(line.split(" ")[1].split(":")[0])

        game_data = line.split(":")[1].split(";")
        bag_least_possible_colors = {"red": 0, "green": 0, "blue": 0}
        for data in game_data:
            for game_item in data.split(","):
                bag_color = game_item.strip().split(" ")[1].strip(",")
                game_bag_count = int(game_item.strip().split(" ")[0])

                if game_bag_count > bag_least_possible_colors[bag_color]:
                    bag_least_possible_colors[bag_color] = game_bag_count
            
        total_power += bag_least_possible_colors["red"] * bag_least_possible_colors["green"] * bag_least_possible_colors["blue"]

    return total_power

if __name__ == "__main__":
    with open(file_path, "r") as file:
        lines = file.readlines()

    # lines = [
    #     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    #     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    #     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    #     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    #     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    # ]

    total_power = check_possible_games(lines)
    print("Power of least possible colors:", total_power)