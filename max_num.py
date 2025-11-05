a = int(input("Enter a number \n"))
b = int(input("Enter a number \n"))
c = int(input("Enter a number \n"))

if (a>b and a>c):
    print(f"{a} is the greatest number out of {a}, {b}, {c}")

elif (b>a) and (b>c):
    print(f"{b} is the greatest number out of {a}, {b}, {c}")

else:
    print(f"{c} is the greatest number out of {a}, {b}, {c}")