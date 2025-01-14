#import the random module
import random

#Create an empty list
my_list = []

#Lets create a list with 100 random numbers
for i in range(0,99):
    my_list.append ( random.randrange(0,255) )

#print the list of number stored in the list
print(my_list)

    
