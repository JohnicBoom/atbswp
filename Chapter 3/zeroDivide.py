def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        return 'Error: Are you trying to divide by zero?'
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))