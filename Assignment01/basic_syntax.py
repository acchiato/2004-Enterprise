
import random
#getting user inputs
user_name = input("Enter your name: ")
random_number = input("Enter a number: ")

#making lucky number
for i in random_number:
    if(int(random_number)%2==0):
        print(int(random_number)+random.randint(1,677))
        i+=i
    else:
        print(str(user_name)+" Sorry! Try again! ")

