# (d) Write a program that asks the user for a number n and prints the sum of the numbers 1 to n.

n = int(input("Enter a number: "))
total = sum(range(1, n + 1))
print("Sum from 1 to ", n ," is " , total)