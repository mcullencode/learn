age = 24
print('My age is ' + str(age) + 'years')
#replacement field method below
print('My age is {0} years'.format(age))

print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "Jan", "March", "May", "July", "August", "October", "Decemebt"))

print("My age is %d years" % age)

print("My afe is %d %s, %d %s" % (age, "years", 6, "months"))

for i in range(1,12):
    #%2d allocated two spaces for the variable, %4d allocates 4 spaces etc
    print("no, %2d squared is %4d and cubed is %4d" %(i, i**2, i**3))

print("Pi is approximately %12.50f" % (22/7))

for i in range(1,12):
    # in {x:y}, x is the replacement field number and y is the width format
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))

for i in range(1,12):
    # in {x:y}, x is the replacement field number and y is the width format, < still allocating space, just on lhs.
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i**2, i**3))

print("Pi is approximately {0:12.50f}".format(22/7))

