"""a positive integer where the sum of its proper divisors
(divisors excluding the number itself) is greater than the
    number itself"""

n = int(input("Enter a number : "))
ans = 0

for i in range(1, (n // 2) + 1):
    if n % i == 0:
        ans += i
        print(i)

if ans > n:
    print("yes", ans)
else:
    print("No", ans)
