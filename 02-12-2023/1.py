file_path = "input.txt"

bag_contents = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def check_possible_games(lines):
    total_sum = 0

    for line in lines:
        game_id = int(line.split(" ")[1].split(":")[0])
        isPossible = True

        game_data = line.split(":")[1].split(";")
        for data in game_data:
            if not isPossible:
                break

            for game_item in data.split(","):
                bag_color = game_item.strip().split(" ")[1].strip(",")
                game_bag_count = int(game_item.strip().split(" ")[0])
                if bag_contents[bag_color] >= game_bag_count:
                    isPossible = True
                else:
                    isPossible = False
                    break

        if isPossible:
            total_sum += game_id

    return total_sum

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

    total_sum = check_possible_games(lines)
    print("Sum of possible games:", total_sum)