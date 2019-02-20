#write helper functions instead of complex expression

from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
#print(repr(my_values))

# gives values for red blue and green. 5, 0 and ''. Using the get method
# on the result dictionary will return different values in each circumstance

#print('Red:    ', my_values.get('red'))
#print('Green:     ', my_values.get('green'))
#print('Opactiy:   ', my_values.get('opacity'))

#returns ['5'], [''], None

# would be nice if a default value of 0 was assigned when a parameter isnt supplied or is blank. Can solve with below


#line below :. ,get(key, default), i.e. assigned key value, if not, go to default value. .get()[0] takes 1st element of
# array. or 0 just assigns to 0 if false.

red = my_values.get('red', [''])[0] or 0.
print('red', red)

# easier version

red = int(red[0]) if red[0] else 0

# can write a helper function

def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

green = get_first_int(my_values, 'green')

