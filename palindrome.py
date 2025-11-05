num = int(input("enter the number: "))
z = num
rev = 0
while(num>0):
    x = num%10

    rev = rev*10+x
    num = num//10

print(rev)

if(z==rev):
    print(z," is palindrme")
else:
    print(z," is not palindrome")