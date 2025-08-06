n = int(input("Enter the value of n: "))
limit = n ** 2

num = 1
for _ in range(n):  # run n times
    if num > limit:
        break
    print(num, end=' ')
    num *= 2
