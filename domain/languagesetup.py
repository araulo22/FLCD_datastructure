reservedWords = []
separators = []
operators = []


def read_file():
    with open('domain/tokens.in', 'r') as f:
        for i in range(16):
            reservedWords.append(f.readline().strip())
        for i in range(8):
            separator = f.readline().strip()
            if separator == "space":
                separator = " "
            separators.append(separator)
        for i in range(11):
            operators.append(f.readline().strip())

# read_file()
# print(reservedWords)
# print(separators)
# print(operators)
