import re

input1 = input("First string: ")
input2 = input("Second string: ")


def unbalanceBackSlashCheck(inputNumber):
    if inputNumber == 1:
        backSlashPresent = 0
        for i in range(len(input1)):
            if (input1[i] == "\\") and (backSlashPresent == 0):
                backSlashPresent = 1
            elif backSlashPresent == 1:
                match = re.match("^[\\\"*']*$", input1[i])
                if not match:
                    print("False")
                    exit(0)
                backSlashPresent = 0
            else:
                backSlashPresent = 0
    if inputNumber == 2:
        backSlashPresent = 0
        for i in range(len(input2)):
            if (input2[i] == "\\") and (backSlashPresent == 0):
                backSlashPresent = 1
            elif backSlashPresent == 1:
                # print(input2[i])
                match = re.match("^[\\\"*']*$", input2[i])
                if not match:
                    print("False")
                    exit(0)
                backSlashPresent = 0
            else:
                backSlashPresent = 0


def unbalancedQuoteCheck(inputNumber):
    if inputNumber == 1:
        quotePresent = 0
        for j in range(len(input1) - 1, -1, -1):
            if (input1[j] == "'") or (input1[j] == "\""):
                quotePresent += quotePresent
            elif quotePresent == 1:
                # I check if there is a backslash
                if input1[j] == "\\":
                    quotePresent = 0
                else:
                    if j != len(input1) - 1:
                        print("False")
                        exit(0)
    elif inputNumber == 2:
        quotePresent = 0
        for j in range(len(input2) - 1, -1, -1):
            if (input2[j] == "'") or (input2[j] == "\""):
                quotePresent += quotePresent
            elif quotePresent == 1:
                # I check if there is a backslash
                if input2[j] == "\\":
                    quotePresent = 0
                else:
                    if j != len(input2) - 1:
                        print("False")
                        exit(0)


def quoteCompletion(inputNumber):
    if inputNumber == 1:
        if input1[len(input1) - 2] == "\\":
            print("False")
            exit(0)
    elif inputNumber == 2:
        if input2[len(input2) - 2] == "\\":
            print("False")
            exit(0)


if (not input1) and (not input2):
    # nothing is present
    print("False")
    exit(0)
elif not input2:
    unbalanceBackSlashCheck(1)
    unbalancedQuoteCheck(1)
    quoteCompletion(1)

    if input1[0] != input1[len(input1) - 1]:
        print("False")
        exit(0)

    if (input1[0] != "'") and (input1[0] != "\""):
        print("False")
        exit(0)
    print("True")
    exit(0)
elif not input1:
    unbalanceBackSlashCheck(2)
    unbalancedQuoteCheck(2)
    quoteCompletion(2)

    if input2[0] != input2[len(input2) - 1]:  # make sure that they equal
        print("False")
        exit(0)

    if (input2[0] != "'") and (input2[0] != "\""):  # make sure that they are valid quotes
        print("False")
        exit(0)
    print("True")
    exit(0)
else:
    unbalanceBackSlashCheck(1)
    unbalanceBackSlashCheck(2)
    unbalancedQuoteCheck(1)
    unbalancedQuoteCheck(2)
    quoteCompletion(2)

    if input1[len(input1) - 1] != "\\":  # new line character
        print("False")
        exit(0)

    if len(input2) != 1:
        if (input2[0] == "'") or (input2[0] == "\""):  # second string does not close the quotes
            print("False")
            exit(0)

    if input1[0] != input2[len(input2) - 1]:  # make sure that they are equal
        print("False")
        exit(0)

    if (input1[0] != "'") and (input1[0] != "\""):  # make sure that they are valid quotes
        print("False")
        exit(0)

    print("True")
    exit(0)