#python provies compact syntax for deriving one list from another
#these expressions are called list comprehensions.

a = [1,2,3,4,5,6,7,8,9,10]
squares = [x**2 for x in a]
print(squares)

#unless youre applying a single argument function, list comprehensions are clearer than the map built in function
# for simple cases. map requires creating a lambda function for the computation. map below

squares = map(lambda x: x**2, a)

#list comprehensions let you easily filter out list items, unlike map


even_squares = [ x**2 for x in a if x % 2 == 0]
print(even_squares)

alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)

#dictionaries and sets have their own equivalent of list comprehensions. these make it easy to create derivative data structures when
#writing algorithms.

chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}

print(rank_dict)
print(chile_len_set)

matrix = [[1,2,3], [4,5,6], [7,8,9]]

flat = [x for row in matrix for x in row]

print(flat)




squared = [[x**2 for x in row] for row in matrix]

print(squared)

flat = [x for sublist1 in my_lists for sublist2 in sublist1 for x in sublist 2]

flat = []

for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)

#.extend similar to append.



