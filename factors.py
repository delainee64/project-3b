# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 10/08/2022
# Description: Write a program that asks the user to enter a positive integer, then prints a list
# of all positive integers that divide that number evenly, including itself and 1, in ascending order.

input_num = int(input('Please enter a positive integer: '))
print("The factors of", input_num, "are:")
for i in range(1, input_num+1):
    if(input_num % i == 0):
        print(i)