names = ['Cecilia', 'Lisa', 'Marie']
letters = [len(n) for n in names]

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

print(longest_name)

#whole loop is slightly visually noisy. enumerate slightly improves, but still not ideal. Python provices a zip built in fnc
#zip wraps two or more iterators with a lazy generator. the zip generator yields tuples containign the next value from each iterator
#resultin code is much cleaner than indexing into multiple lists.

for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count