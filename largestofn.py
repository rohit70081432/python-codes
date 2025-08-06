n = int(input("How many numbers: "))
i = 1
large = int(input("Enter number 1: "))

while i < n:
    num = int(input(f"Enter number {i+1}: "))
    if num > large:
        large = num
    i += 1

print("Largest number is:", large)
