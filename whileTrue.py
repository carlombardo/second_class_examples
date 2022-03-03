sum = 0
while True:
    number = int(input("Give me a number (0 to stop): "))
    if number == 0:
        break
    sum = sum + number
print("The sum is: ", sum)

