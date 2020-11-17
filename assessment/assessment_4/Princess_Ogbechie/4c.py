# Using a for loop to create a list ['a','bb','ccc',.......,] ending with 26 copies of the letter z

import string   # imports the string module that allows the lowercase values to be used continuously.

lett = []

for i in string.ascii_lowercase:    #the string.ascii_lowercase command gives a string of all the lowercase letters of the alphabet
    lett += [i * ((string.ascii_lowercase.index(i)+1))]     #the .index function works like with any other list to give the position of a particular letter

print(lett) # Output statement