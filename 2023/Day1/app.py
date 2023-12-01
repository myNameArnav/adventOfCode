with open("2023/Day1/input.txt", "r") as f:
    input = f.read()

input = input.split()

# test = [input[0]]


def words2num(message: str) -> str:
    ogMessage = message
    words = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    for word, num in words.items():
        message = message.replace(word, num)

    return message


def main(input):
    result = 0
    for message in input:
        ogMessage = message
        message = words2num(message)
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

main(input)
