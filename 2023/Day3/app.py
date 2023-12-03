with open("input.txt", "r") as f:
    input = f.read().split()

# [
#     ["4", "6", "7", ".", ".", "1", "1", "4", ".", "."],
#     [".", ".", ".", "*", ".", ".", ".", ".", ".", "."],
#     [".", ".", "3", "5", ".", ".", "6", "3", "3", "."],
#     [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
#     ["6", "1", "7", "*", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", "+", ".", "5", "8", "."],
#     [".", ".", "5", "9", "2", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", "7", "5", "5", "."],
#     [".", ".", ".", "$", ".", "*", ".", ".", ".", "."],
#     [".", "6", "6", "4", ".", "5", "9", "8", ".", "."],
# ]

GRID = []
result = []


def getSymbolList(input: list) -> list:
    x = []

    for line in input:
        a = list(line)
        for s in a:
            if s.isdigit() or s == ".":
                continue
            else:
                x.append(s)
    return list(set(x))


def getNumberLen(row: list, pos: int) -> list:
    temp = []
    for cell in range(pos, len(row)):
        if row[cell].isdigit():
            temp.append(row[cell])
        else:
            break
    return ["".join(temp), len(temp)]


def checkForSymbols(
    row: list, upRow: list, downRow: list, coli: int, numLen: int
) -> bool:
    rowSliceStart = 0 if coli == 0 else coli - 1
    rowSliceEnd = coli + numLen + 1
    masterRow = (
        row[rowSliceStart:rowSliceEnd]
        + upRow[rowSliceStart:rowSliceEnd]
        + downRow[rowSliceStart:rowSliceEnd]
    )

    for symbol in symbolList:
        if symbol in masterRow:
            return True

    return False


def main(GRID):
    for rowi, row in enumerate(GRID):
        rowLen = len(row)
        skipper = 0
        for coli in range(len(row)):
            col = row[coli]
            if coli == skipper:
                if col.isdigit():
                    num, numLen = getNumberLen(row, coli)
                    upRow = [] if rowi == 0 else GRID[rowi - 1]
                    downRow = [] if rowi == len(GRID) - 1 else GRID[rowi + 1]
                    isEnginePart = checkForSymbols(row, upRow, downRow, coli, numLen)
                    if isEnginePart:
                        result.append(int(num))
                skipper += numLen if col.isdigit() else 1
    return sum(result)


symbolList = getSymbolList(input)

for line in input:
    GRID.append(list(line))

print(main(GRID))
