#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

def main():
    score_table = {}  # this is a dictionary
    score_table['akif'] = 100 # add a new key-value pair
    score_table['ali'] = 90 # add a new key-value pair
    score_table['veli'] = 80 # add a new key-value pair
    for elem in score_table: # iterate the dictionary
        print('%s\t--->\t%d' % (elem, score_table[elem])) # print the key-value pair

    score_table['akif'] = 99 # update the value of the key 'akif'
    score_table['veli'] = 88 # update the value of the key 'veli'
    score_table['mehmet'] = 77 # add a new key-value pair
    for elem in score_table: # iterate the dictionary
        print('%s\t--->\t%d' % (elem, score_table[elem])) # print the key-value pair

    score_table.pop('ali') # remove the key-value pair with the key 'ali'
    for elem in score_table: # iterate the dictionary
        print('%s\t--->\t%d' % (elem, score_table[elem])) # print the key-value pair

    score_table.clear() # remove all the key-value pairs
    print(score_table) # print the dictionary


if __name__ == '__main__': # this is the main function
    main()
