# Write a program to calculate ticket price for Universal Studio at Clear Lake.
# There are two options of tickets to be sold: one-park-a-day and park-to-park.
# Your program first display the options to the users like:
# A. One park a day, $114 for each adult and $94 for each child.
# B. Park to park (going two parks on the same day),
# $144 for each adult and $124 for each child.

# Then, ask user to select which option he/she will select,
# A or B. Also, ask user to enter how many adults and how many children.
# Only "A" and "B" can be used for selecting from the options.
# If use enters any other input (even including "a" or "b"),
# your program will display an error message and end. Only positive integers or
# 0 are allowed to be used for the number of adults or children.
# If the input is invalid, your program will display an error message and end.
# After the input is validated, your program will ask the user whether or
# not he or she wants to add a fast pass to each visitor, "y" for yes and
# anything else for no. If yes, $50 will be added to each visitor's ticket price.
# Calculate the total price based on the ticket option selected and
# the number of visitors. Display the total price in money format.

adults = int(input('how many adults: '))
children = int(input('how many children: '))

one_park_a_day_adults = 114
one_park_a_day_children = 94
park_to_park_adults = 144
park_to_park_children = 124

One_park_a_day_adults_and_children = (one_park_a_day_adults * adults) + ( one_park_a_day_children * children)

print("A. One park a day, for adult and  child. $ % for adult and  child." %One_park_a_day_adults_and_children)

park_to_park_adults_and_children = (park_to_park_adults * adults) + (park_to_park_children * children)

print("B. park-to-park, for adult and  child. $ % for adult and  child." %park_to_park_adults_and_children)


A = One_park_a_day_adults_and_children
B = park_to_park_adults_and_children
#print('A. One park a day, $114 for each adult and $94 for each child.')
#print('B. Park to park (going two parks on the same day), $144 for each adult and $124 for each child. ')

option = input('Please select A or B:')

if option == "A":
    print("For Selecting Option A your bill will be " +str(A))
if option == "B":
    print("For Selecting Option B your bill will be " + str(B))
else:
    print("Input Something Within A or B")

