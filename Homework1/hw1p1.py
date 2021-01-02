keywords = ["False", "None", "True", "and", "as", "assert", "break", "def", "del", "elif", "else", "except", "finally",
            "for", "if", "import", "in", "is", "lambda", "nonlocal", "not", "raise", "return", "try", "while", "with",
            "yield"]
lowerCaseLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                    "t", "u", "v", "w", "x", "y", "z"]
upperCaseLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                    "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def exit_false():
    print("False")
    exit(0)


stringProvided = input("Please provide a string: ")

# I first check if the word provided is already a keyword
for i in range(len(keywords)):
    if stringProvided == keywords[i]:
        exit_false()

for i in range(len(stringProvided)):
    if i == 0:
        legal = -1
        # I check that they start with either a letter or an underscore
        if stringProvided[0] == "_":
            legal = 0
        if legal == -1:
            for j in range(len(lowerCaseLetters)):
                if lowerCaseLetters[j] == stringProvided[0]:
                    legal = 0
        if legal == -1:
            for j in range(len(upperCaseLetters)):
                if upperCaseLetters[j] == stringProvided[0]:
                    legal = 0
        # after all valid arguments are checked, if nothing is valid, i exit
        if legal == -1:
            exit_false()

    if i != 0:
        # I check that it is either a number, underscore, or letter
        legal = -1
        if stringProvided[i] == "_":
            legal = 0
        if legal == -1:
            for j in range(len(lowerCaseLetters)):
                if lowerCaseLetters[j] == stringProvided[i]:
                    legal = 0
        if legal == -1:
            for j in range(len(upperCaseLetters)):
                if upperCaseLetters[j] == stringProvided[i]:
                    legal = 0
        if legal == -1:
            for j in range(len(numbers)):
                if numbers[j] == stringProvided[i]:
                    legal = 0
        if legal == -1:
            exit_false()

print("True")
exit(0)

# Things to ask TA --> don't understand what is the importance of underscores being valid/ invalid? --> private/
# ultra private
