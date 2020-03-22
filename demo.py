number = 2

result = 0

for i in range(40):
    result = number + number
    print(number, "+", number, "=", result)
    number = result
