import math

try:
    year = int(input("What year do you want to check? "))
    first = 1930
    dif = year - first
    mult = float(dif/4)
    x = mult % 1


finally:
    if (dif % 400 == 0) and (dif % 100 == 0) and (dif > 0):
     print("{0} is a world cup year.".format(year))

    elif (dif % 4 == 0) and (dif % 100 != 0) and (dif > 0):
     print("{0} is a world cup year.".format(year))

    elif (x == .5):
     print("{0} is not a world cup year.".format(year))
     print("The next world cup is in 2 years.")

    elif (x == .25):
        print("{0} is not a world cup year.".format(year))
        print("The next world cup is in 3 years.")

    elif (x== .75):
        print("{0} is not a world cup year.".format(year))
        print("The next world cup is in 1 years")