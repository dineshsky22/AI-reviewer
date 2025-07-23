
n = int(("Enter a number: "))

i = 1
while :
    value = 2 ** i
    if value > n:
        print(f"The smallest power of 2 greater than {n} is {value}")
        break
    i += 1