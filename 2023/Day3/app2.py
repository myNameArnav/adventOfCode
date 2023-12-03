with open("input.txt", "r") as f:
    input = f.read().split()

GRID = []
result = []
gearList = []

for line in input:
    GRID.append(list(line))


def getNumberLen(row: list, pos: int) -> list:
    temp = []
    for cell in range(pos, len(row)):
        if row[cell].isdigit():
            temp.append(row[cell])
        else:
            break
    return ["".join(temp), len(temp)]


def makeSubgrid(row: list, upRow: list, downRow: list, coli: int, numLen: int) -> list:
    rowSliceStart = 0 if coli == 0 else coli - 1
    rowSliceEnd = len(row) - 1 if coli == len(row) - 1 else coli + numLen + 1
    masterRow = (
        upRow[rowSliceStart:rowSliceEnd]
        + row[rowSliceStart:rowSliceEnd]
        + downRow[rowSliceStart:rowSliceEnd]
    )
    return masterRow


def checkGearPos(
    row: list, upRow: list, downRow: list, rowi: int, coli: int, numLen: int
) -> list:
    startSlice = 0 if coli == 0 else coli - 1
    endSlice = numLen + coli + 1
    if "*" in upRow[startSlice:endSlice]:
        r = rowi - 1
        c = upRow[startSlice:endSlice].index("*")
    if "*" in row[startSlice:endSlice]:
        r = rowi
        c = row[startSlice:endSlice].index("*")
    if "*" in downRow[startSlice:endSlice]:
        r = rowi + 1
        c = downRow[startSlice:endSlice].index("*")
    return r, c


def findPairs(gearList) -> int:
    temp = {}
    result = 0
    for gear in gearList:
        num = gear[0]
        gearPos = str(gear[1])
        if gearPos in temp.keys():
            temp[gearPos] = [temp[gearPos][0] * num, temp[gearPos][1] + 1]
        else:
            temp[gearPos] = [num, 1]

    for val in temp.values():
        if val[1] == 2:
            result += val[0]
    return result


def main():
    for rowi, row in enumerate(GRID):
        skip = 0
        for coli, col in enumerate(row):
            if skip == coli:
                if col.isdigit():
                    num, numLen = getNumberLen(row, coli)
                    upRow = [] if rowi == 0 else GRID[rowi - 1]
                    downRow = [] if rowi == len(GRID) - 1 else GRID[rowi + 1]
                    masterRow = makeSubgrid(row, upRow, downRow, coli, numLen)
                    if "*" in masterRow:
                        r, c = checkGearPos(row, upRow, downRow, rowi, coli, numLen)
                        a = 0 if coli == 0 else 1
                        gearList.append([int(num), [r, coli + c - a]])
                skip += numLen if col.isdigit() else 1
    pairs = findPairs(gearList)

    return pairs


print(main())
