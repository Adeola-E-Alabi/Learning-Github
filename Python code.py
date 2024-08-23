def toggle():
    import random
    letter = "X"
    capitalize = False
    array = []
    rand_int = random.choice(range(1,21))
    while rand_int > 0:
        array.append(rand_int)
        rand_int -= 1

    for x in array:
        capitalize = (not capitalize)
        if capitalize == True:
            letter = "The letter X"
        else:
            letter = "The letter x"
    return letter
