# this is a looping function used for printing the history of data in the most recently added order

def iterate_recent(data):
    reversed_data = reversed(data)
    reversed_data = (list(reversed_data))
    print(reversed_data)








# ----- Main Routine ---------
 # First we need a function that asks users to add fruits to a basket. This is we can then design the loop to spit those fruits back out, in the order of most recently added, to the first item added.

run_question_loop = True
fruit_basket = []

while True:
    fruit = input('Please enter your fruit, then press enter. (If you would like to exit the loop, please enter XXX)')

    if fruit == 'XXX' and len(fruit_basket) > 0:
        break
    else:
        fruit_basket.append(fruit)

# Now we need to print this in the most recent order. This means we need it to desend in order of the list counting down

print(fruit_basket)

iterate_recent(fruit_basket)

    
