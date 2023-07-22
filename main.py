finalArray = []
times = ["3:42", "3:34"]  # Insert times here in Minute:Seconds format
for time in times:
    convertedTime = 0
    timeSplitted = time.split(':')
    convertedTime += int(timeSplitted[0]) * 60
    convertedTime += int(timeSplitted[1])
    finalArray.append(convertedTime)
print("The times have been converted from Minutes:Seconds format to just seconds.")
print("Now, insert this list into a tool like https://www.calculator.net/standard-deviation-calculator.html to find the standard deviation, for instance.")
print(", ".join(str(time) for time in finalArray))
