n = int(input("Enter a number\n"))
sum = 0
for i in range(1,n+1):
    print(i, end=",")
    sum+=i
print()
print(f"Sum of numbers 1 to {n} = {sum}")