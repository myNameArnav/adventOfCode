with open("input.txt", "r") as f:
    input = f.read().split("\n")

result = 0


def checkIfGameValid(games):
    green, red, blue = [], [], []
    print(games)
    for game in games:
        for cube in game:
            # ' 1 green'
            if "green" in cube:
                green.append(int(cube.replace("green", "").strip()))
            if "red" in cube:
                red.append(int(cube.replace("red", "").strip()))
            if "blue" in cube:
                blue.append(int(cube.replace("blue", "").strip()))

    return max(green) * max(red) * max(blue)


def main():
    for lines in input:
        rawGameNumber, gameInfo = lines.split(":")
        gameNumber = int(rawGameNumber.replace("Game", "").strip())
        games = [q.split(",") for q in gameInfo.split(";")]
        result += checkIfGameValid(games)

    print(result)


main()
