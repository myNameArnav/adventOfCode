with open("input.txt", "r") as f:
    input = f.read()

input = input.split("\n")

# test = [input[0]]

result = 0

for message in input:
    reversed = message[::-1]

    for sym in message:
        try:
            a = int(sym)
            break
        except ValueError:
            continue

    for invsym in reversed:
        try:
            b = int(invsym)
            break
        except ValueError:
            continue

    c = a * 10 + b

    result += c

print(result)
