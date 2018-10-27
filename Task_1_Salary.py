# Write a program to calculate a gross pay for an employee, given the salary rate is $16 per hour.
# Ask user to enter how many hours he/she works each week.
# If the user works more than 40 hours per week, he will get 1.5x pay for the hours more than 40 hours (for the first 40 hours, it is still $16 per hour).
# You can assume that in this question the user always enters a valid integer.
# There is no input validation for an integer needed. Based on the user's input, calculate the gross pay with a money format.


# salary = 16.0
# hours = float(input('enter how many hours he/she works each week:'))
# if hours < 40:
#     print(hours * salary)
# else:
#     print(40 * 16 + (hours - 40) * (16 * 1.5))
#

salary = 16
hours = int(input('enter how many hours he/she works each week: '))
if hours <40:
    print("your gros pay is" '\t' '$'"%.2f"%(hours * salary))
else:
    print(40 * 16 + (hours - 40) * (16 * 1.5))