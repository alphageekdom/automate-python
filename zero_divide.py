def spam(num):
    try:
        return 42 / num
    except ZeroDivisionError:
        print(f'Error, cannot divide by: {num}')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))