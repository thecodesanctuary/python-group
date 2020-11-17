# this program is given a start set of values in a list and instructions to be worked on

entry = [8,9,10]    # initial set of values

entry[1] = 17   # set index 1 to 17

entry += [4,5,6]    # add 4,5,6 to the end of the list

entry.remove(entry[0])  # remove the first entry from the list

entry.sort()     # sort the list

entry *= 2      # Double the list

entry.insert(3,25)      # insert 25 at index 3

print(entry)

# the final list should equal [4,5,6,25,10,17,4,5,6,10,17]