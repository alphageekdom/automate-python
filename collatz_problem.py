def collatz(num):
    if num % 2 == 0:
        return num // 2
    elif num % 2 == 1:
        return 3 * num + 1

try:
    number = int(input('Enter a number: '))
    while number > 0 and number != 1:
        number = collatz(number)
        print(number)

except ValueError:
    print('Enter only an integer')
