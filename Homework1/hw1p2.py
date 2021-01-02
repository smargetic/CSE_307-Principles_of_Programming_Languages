import re

stringProvided = input("Please provide a number: ")
# int
pureIntMatch = re.match("^-*[0-9]*$", stringProvided)
# either binary, octal, or hexadecimal
intMatch = re.match("^[0-9bBoOxX]*", stringProvided)
# float
floatMatch1 = re.match("^-*\d*e*E*-*\d*\.-*\d*e*E*-*\d*$", stringProvided)
floatMatch2 = re.match("^-*\d+e*E*-*\d+$", stringProvided)


if pureIntMatch:
    negCount = 0
    for i in range(len(stringProvided)):
        # check that right number of neg is present
        if stringProvided[i] == "-":
            negCount = negCount + 1
    if negCount > 1:
        print("None")
        exit(0)
    print("int")
    exit(0)
elif floatMatch1 or floatMatch2:
    numberOfE = 0  # make sure only 1 e

    # print("A match here")
    for i in range(len(stringProvided)):
        if stringProvided[i] == "e" or stringProvided[i] == "E":
            numberOfE = numberOfE + 1
            if i == (len(stringProvided) - 1):
                # there is nothing that follows the e
                print("None")
                exit(0)

    if numberOfE > 1:
        print("None")
        exit(0)
    # should also check if there is something after decimal?
    print("float")
    exit(0)

elif intMatch:
    # print("Go here 2")
    length = len(stringProvided)
    if length <= 2:  # ex. 0b, 0x, 0x
        print("None")
        exit(0)
    binary = -1
    octal = -1
    hexA = -1
    if stringProvided[0] != "0":
        print("None")
        exit(0)
    if (stringProvided[1] == "b") or (stringProvided[1] == "B"):
        binary = 0
        # make sure all that follows is within the range of a binary number
        for i in range(2, len(stringProvided)):
            if (stringProvided[i] != "0") and (stringProvided[i] != "1"):
                print ("None")
                exit(0)
        print("int")
        exit(0)
    elif (stringProvided[1] == "o") or (stringProvided[1] == "O"):
        octal = 0
        for i in range(2, len(stringProvided)):
            # check to make sure that its within hte range of an octal
            isOctalMatch = re.match("^[0-7]*$", stringProvided[i])
            if not isOctalMatch:
                print ("None")
                exit(0)
    elif (stringProvided[1] == "x") or (stringProvided[1] == "X"):
        hexA = 0
        for i in range(2, len(stringProvided)):
            # check to make sure that its within hte range of an hex
            isHexMatch = re.match("^[0-9a-fA-F]*$", stringProvided[i])
            if not isHexMatch:
                print ("None")
                exit(0)
    if (binary == -1) and (octal == -1) and (hexA == -1):
        print("None")
        exit(0)

    print("int")
    exit(0)
else:
    #print("Did not fit any")
    print("None")
    exit(0)
