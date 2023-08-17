# this is a looping function used for printing the history of data in the most recently added order
def reverse_order(all_items, return_items):
    MAX_CALC = return_items
    # This is for if you have more then 5 (MAX CALC Variable) fruits - Its only going to print out the 5 most recent
    if len(all_items) > MAX_CALC:
        print('\n**** {} Most Recent Items ****'.format(MAX_CALC))
        # Flips the order of the list and prints the last 5 out.
        for item in range(0, MAX_CALC):
            print(all_items[len(all_items) - item - 1])
    # Then you get this if you have 5 or less then 5
    else:
        print('\n**** Items from Newest to Oldest ****')
        # flips the list and prints them all out
        for item in all_items:
            print(all_items[len(all_items) - all_items.index(item) - 1])




# ----- Main Routine ---------
 # First we need a function that asks users to add fruits to a basket. This is we can then design the loop to spit those fruits back out, in the order of most recently added, to the first item added.

run_question_loop = True
fruit_basket = []


while True:
    fruit = input('Please enter your fruit, then press enter. (If you would like to exit the loop, please enter XXX)')

    if fruit == 'XXX' and len(fruit_basket) > 2:
        break
    elif fruit == 'XXX' and len(fruit_basket) == 0:
        print('You need to have at least one Item!')
    else:
        fruit_basket.append(fruit)

# Now we need to print this in the most recent order. This means we need it to desend in order of the list counting down

reverse_order(fruit_basket, 5)




    
