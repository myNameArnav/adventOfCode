with open("input.txt", "r") as f:
    input = f.read().split()

def words2num(message: str) -> str:
    # handles cases like `eighthree`
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

        # Second part
        message = words2num(message)

        for symbol in message:
            if symbol.isdigit():
                a = int(symbol)

        reversed = message[::-1]
        for symbol in reversed:
            if symbol.isdigit():
                b = int(symbol)

        c = a * 10 + b
        result += c
    return result

print(main(input))
