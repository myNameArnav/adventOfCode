with open("/Users/arnavjain/Documents/Projects/adventOfCode/2023/Day2/input.txt", "r") as f:
    input = f.read().split("\n")
    
# 12 red cubes, 13 green cubes, and 14 blue cubes

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

result = 0

def checkIfGameValid(games):
    green, red, blue = [],[],[]
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

for lines in input:
    rawGameNumber, gameInfo = lines.split(":")
    gameNumber = int(rawGameNumber.replace("Game", "").strip())
    games = [q.split(",") for q in gameInfo.split(";")]
    result += checkIfGameValid(games)


print(result)