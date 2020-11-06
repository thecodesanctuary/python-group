#Program that tells a freshman, sophomore, junior and senior based on the number of credits they have taken

cred = int(input("How many credits have you taken? "))

if cred <= 23:
    print("You are a freshman.")
elif cred >= 24 and cred <= 53 :
    print("You are a sophomore")
elif cred >=54 and cred <= 83:
    print("You are a junior")
elif cred >= 84:
    print("You are a senior")