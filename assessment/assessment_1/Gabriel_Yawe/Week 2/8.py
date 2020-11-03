import random
score = 0
i = 0
while i != 10:
    i=i+1
    num_1 = random.randint(1,10)
    num_2 = random.randint(1,10)
    print("What is the product of: ",str(num_1) + "*" +str(num_2))
    product=str(num_1*num_2)
    
    num_symbol= random.randint(1,3)

   # if symbol == 1:
    #    question = input("What is" + str(num1))
     #   answer = num1+num2
      #  if question == answer:
       #     score =score + 1
math()