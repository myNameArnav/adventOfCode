# input or input2
with open("input.txt", "r") as f:
    input = f.read().split("\n")

inp = {}
result = 1
wins = []


inputTime = ((((input[0]).split(":")[1]).replace("  ", " ")).strip()).split(" ")
inputDistance = ((((input[1]).split(":")[1]).replace("  ", " ")).strip()).split(" ")

inputTime = [int(time) for time in inputTime if time != ""]
inputDistance = [int(distance) for distance in inputDistance if distance != ""]


print(inputTime, inputDistance)


for counter, time in enumerate(inputTime):
    prob = 0
    time = int(time)
    for i in range(time+1):
        calc = i * (time - i)
        if calc > inputDistance[counter]:
            prob += 1
    wins.append(prob)
    
print(wins)

for win in wins:
    result *= win

print(result)