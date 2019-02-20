#prefer enumerate over range

#if you have a list of strings you want to iterate over, you can loop directly over the sequence.

flavour_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']

for flavour in flavour_list:
    print('%s is delicious' % flavour)

#you may want to iterate over a list and also know the index of the item in the list.

for i in range(len(flavour_list)):
    flavour = flavour_list[i]
    print('%d: %s' % (i+1, flavour))

#python provides enumerate function for addessing this situation. it wraps any iterator with a lazy generator. This generator yields
# pairs of the loop index

for i, flavour in enumerate(flavour_list):
    print('%d: %s' % (i+1, flavour))