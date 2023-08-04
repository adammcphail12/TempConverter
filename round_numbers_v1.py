
def round_ans(val, digit =0):
    p = 10 ** digit
    var_rounded = (val * p * 2 + 1) // 2 / p
    return '{:.0f}'.format(var_rounded)


print(round(5.9))