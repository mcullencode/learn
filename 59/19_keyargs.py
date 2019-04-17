def remainder(number, divisor):
    return number % divisor

assert remainder(20, 7) == 6

remainder(20, 7)
remainder(20, divisor = 7)
remainder(number = 20, divisor = 7)
remainder(divisor = 7, number = 20)

#all these calls are equivalent. positional arguments must be specified before keyword arguments.
remainder(number = 20, 7)
# returns an error.

remainder(20, number = 7)
#returns an error

#the flexibility of keyword args make the function call clearer to new readers of the code. With the
# call remaunder(20, 7) its not evident which argument is the number.

#the secon impact of the keywrod args is that they can have defualt values specified in the function
# definition. this allows a function to provide dditional capabilities when you need them but lets uou accept default behaviour most of the time

def flow_rate(weight_diff, time_diff, period = 1):
    return (weight_diff / time_diff) * period

flow_per_sec = flow_rate(weight_diff, time_diff)
flow_per_hour = flow_rate(weight_diff, time_diff, period = 3600)

#default value for period is 1, i.e. weight flow per second. we can alter this by specifiying a period in the function argument.