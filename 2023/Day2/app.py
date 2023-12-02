with open("input.txt", "r") as f:
    input = f.read().split("\n")

# 12 red cubes, 13 green cubes, and 14 blue cubes

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

result = 0


def checkIfGameValid(games):
    for game in games:
        for cube in game:
            green, red, blue = True, True, True
            # ' 1 green'
            if "green" in cube:
                noOfCubes = int(cube.replace("green", "").strip())
                if noOfCubes > MAX_GREEN:
                    green = False
            if "red" in cube:
                noOfCubes = int(cube.replace("red", "").strip())
                if noOfCubes > MAX_RED:
                    red = False
            if "blue" in cube:
                noOfCubes = int(cube.replace("blue", "").strip())
                if noOfCubes > MAX_BLUE:
                    blue = False

            if green and red and blue:
                continue
            else:
                return False

    return True


for lines in input:
    rawGameNumber, gameInfo = lines.split(":")
    gameNumber = int(rawGameNumber.replace("Game", "").strip())
    games = [q.split(",") for q in gameInfo.split(";")]
    if checkIfGameValid(games):
        result += gameNumber

print(result)
