from random import random

with open('bird_strikes.csv', 'r') as in_f, open('bird_strikes.test.csv', 'w') as out_f:
    curr = in_f.readline().split(',')
    print(curr)
    curr = in_f.readline().split(',')
    print(curr)
    # out_f.write(curr) # Headers

    # # Column index = 9
    # counter = 0
    # while curr := in_f.readline().split(','):
    #     print(counter, curr[9])
    #     counter += 1

    # = SI(J6 = "No damage", SI(ALEATORIO() >= 0.9, "Caused damage", J6), J6)