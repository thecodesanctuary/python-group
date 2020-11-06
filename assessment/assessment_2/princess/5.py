#Program to count the number of leap years between 1600 and a particular year


year = int(input("What year are you looking at? "))

leap = year - 1600
t = leap // 4

print("There are %d leap years between 1600 and %d" %(t,year))