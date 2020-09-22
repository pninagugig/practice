def x(z):
    y = ['A', 'B', 'C', 'D']
    d = ''
    for r in z:
        if r not in y and ord(r) < 87:
            d += r
    return d
print(x('BED'))
print(x('CLOSET'))
print(chr(87))
# task: I can also pass array of words
# task: clean code - renaming
# task: the condition should also include: not equal to M or N
# task: if the result has length > 7 raise a custom “TooLong” Error
# task: should also work for lower case letters
# task: ignore special charaters (should not be returned)
# task: sort the output in a descending order
# task: if the input is an array of numbers convert it to a string using the ascii values of the numbersdef x(z):
#     y = [‘A’, ‘B’, ‘C’, ‘D’]
#     d = ‘’
#     for r in z:
#         if r not in y and ord(r) < 87:
#             d += r
#     return d
# print(x(‘BED’))
# print(x(‘CLOSET’))
# # task: I can also pass array of words
# # task: clean code - renaming
# # task: the condition should also include: not equal to M or N
# # task: if the result has length > 7 raise a custom “TooLong” Error
# # task: should also work for lower case letters
# # task: ignore special charaters (should not be returned)
# # task: sort the output in a descending order
# # task: if the input is an array of numbers convert it to a string using the ascii values of the numbers