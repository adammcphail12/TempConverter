#simpler way of writing in the degree sign
degree_sign = u'\N{DEGREE SIGN}'


test_cases = [2, 4, 23.2]

# testing

for item in test_cases:
    print('{}{}C'.format(item, degree_sign))
