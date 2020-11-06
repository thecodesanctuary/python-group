#Program to print out minutes and seconds given a number of seconds


time = int(input("This is a time converter from seconds to minutes and seconds.\nHow many seconds? "))

m = time//60
s = time % 60

print("\nThe time is %d minutes and %d seconds" %(m,s))