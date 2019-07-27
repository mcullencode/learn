# IpAddy = input('please enter ip')
# print(IpAddy.count("."))
#

# parrot_list = ["non pinin'", "no more", "a stiff", "bereft of live"]
# parrot_list.append("norwegian blue")
#
# for state in parrot_list:
#     print("This parrot is " + state)

# even = [2,4,6,8]
# odd = [1,3,5,7,9]
# numbers = even + odd
# print(sorted(numbers))
# numbers.sort()
# print(numbers)
#
# list_1 = []
# list_2 = list()
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("lists equal ")
#
# print(list("The lists are equal"))

# even = [2,4,6,8]
# another_even = even
#
# #another_even = sorted(even, reverse=True)
#
# print(another_even is even)
#
# #returns True. but if we assign another)even = list(even), we are returned a new list.
#
# anotheranother_even = list(even)
# print(anotheranother_even is even)
#
# another_even.sort(reverse=True)
# print(even)
#
#
# # prints out [8,6,4,2] for even. even though even wasnt directly updated.
# #both variables refer to the same list, so when one is updated, the other is

menu = []
menu.append(['egg', 'spam', 'bacon'])
menu.append(['egg', 'sausage', 'bacon'])
menu.append(['egg', 'spam'])
menu.append(['egg', 'bacon', 'spam'])
menu.append(['egg','bacon',  'sausage', 'spam'])
menu.append(['spam','bacon',  'sausage', 'spam'])
menu.append(['spam','egg',  'spam', 'spam', 'bacon', 'spam'])
menu.append(['spam', 'egg','sausage', 'spam'])

for meal in menu:
    if not "spam" in meal:
        for ingredient in meal:
            print(ingredient)

