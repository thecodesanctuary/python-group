print ("Hey Gabriel, as ususal you like eating and you need me to help calculate your tips.")
bill=int(input("How much is the Bill:? "))
tip=int(input("What percent of that would the tip be?"))
tip_percentile=(tip/100)
total_amount= (tip_percentile*bill) + bill
print("Your bill is:", bill)
print("Total amount paid is:", total_amount)