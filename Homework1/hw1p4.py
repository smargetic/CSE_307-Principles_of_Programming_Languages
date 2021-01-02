import datetime

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


dateProvided = input("Please provide a date (MM/DD/YYYY):")
length = len(dateProvided)


if length != 10:
    # not the right amount of characters
    print("None")
    exit(0)
slashMarks = 0
count = 0

# make sure its the right format
for i in range(length):
    if dateProvided[i] == "/":
        if slashMarks == 0:
            if count != 2:
                # month is wrong
                print("None")
                exit(0)
        elif slashMarks == 1:
            if count != 2:
                # day is wrong
                print("None")
                exit(0)
        slashMarks = slashMarks + 1
        count = 0
    else:
        count = count + 1

if count != 4:
    # year is wrong
    print("None")
    exit(0)

if slashMarks != 2:
    # number of slash's is wrong
    print("None")
    exit(0)

month = int(dateProvided[0:2])
day = dateProvided[3:5]
dayInt = int(day)
year = dateProvided[6:]
yearInt = int(year)

#check if valid date
try:
    tempDate = datetime.datetime(yearInt, month, dayInt)
except ValueError:
    print("None")
    exit(0)

weekday = datetime.date(yearInt, month, dayInt).weekday()

print(weekdays[weekday] + ", " + months[month-1] + " " + day + ", " + year)
