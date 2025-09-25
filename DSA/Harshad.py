"""a positive integer that is divisible by the
sum of its digits
"""

num = int(input("Enter a number : "))
curr = num
sum = 0

while num > 0:
    sum += num % 10
    num //= 10

if curr % sum == 0:
    print("Harsh number")
else:
    print("Not a Harshad Number")
