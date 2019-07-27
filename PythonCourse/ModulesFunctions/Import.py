#unlike any other languages, python has no concept of private of protected variables
#java would only have the functions play and cards available to users, the rest would be hidden

#creatng a function with _function_name, i.e. an underscore in front, makes it a protected function
#which can still be accessed when the corresponding filename is imported, but gives you a warning.
#if object has _ in front of it, its a warning that it shouldnt b meddled with

#prints out all the __functions__
# g = sorted(globals())
#
# for x in globals():
#     print(x)

##recursion

# def fact(n):
#     """calculate n iteratively"""
#     result = 1
#     if n > 1:
#         for f in range(2, n+1):
#             result *= f
#     return result


def factorial(n):
    # n can also be defined as n*(n-1)!

    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def fib(n):
    """f(n) = f(n-1) + f(n-2)"""
    if n < 2:
        return n
    else: return fib(n-1) + fib(n-2)




#runs slowly with high fib numbers. so try iteratively

def fibonacci(n):
    if n ==0 :
        result = 0
    elif n ==1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result

for i in range(35):
    print(i, fibonacci(i))




