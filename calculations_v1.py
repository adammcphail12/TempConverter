def to_celsius(to_convert):
    # this formula converts F to C
    answer = (to_convert -32) * 5 / 9
    return answer


def to_fahrenheit(to_convert):
    # and this formula converts C to F
    answer = to_convert * 1.8 + 32
    return answer

# these are my test cases 
to_c_test = [0, 100, -459]
to_f_test = [0, 100, 40, - 273]

# testing to fahreninheit fu ction

for item in to_f_test:
    print('{} C is {:.0f} F\n'.format(item, to_fahrenheit(item)))


# and here is the testing of my to celsius function
for item in to_c_test:
    print('{} F is {:.0f} C\n'.format(item, to_celsius(item)))