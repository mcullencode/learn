def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

result = divide(x,y)
if result is None:
    print('Invalid Input')

