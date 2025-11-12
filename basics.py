name = "habbie maria eugene m"


print(name.upper())

name=name.upper()
print(name)

name=name.lower()
print(name)

print(name.find('e'))
print(name.find('eugene'))

string = "python for all"

print(string)

print(string.replace('for','4'))
print(string)

print("python" in string)

print(1+1)
print(1-1)
print(3/2)
print(3//2)
print(3*2)
print(3**2)


x = 10

#x = x + 3

x += 3
print(x)

x = 10 + 3 * 2
print(x)

x = (10 + 3) * 2
print(x)





x = 3>2
print(x)

x = 3<2
print(x)

x = 3>=2
print(x)

x = 3<=2
print(x)

x = 3==2
print(x)

x = 3!=2
print(x)



price = 25
print(price>10 and price <30)


price = 5
print(price>10 or price <30)

price = 5
print(not price > 10)




temperature = 35

if temperature>30:
    print("It`s a hot day")
    print("Drink plenty of water")
else:
    print("Normal weather")


temperature = 25

if temperature>30:
    print("hot weather")
print("Done")


temperature = 25

if temperature>30:
    print("hot weather")
elif temperature >20:         #[20,30]
    print("It's a nice day")
elif temperature >10:         #[10,20]
    print("It's very cold")
print("Done")




weight = int(input("weight: "))

unit = input("(K)g or (L)bs: ")


if unit=="L" or unit=="l":
    print("Weight in Kg: ",int(weight*0.45359237))

elif unit=="K" or unit=="k":
    print("Weight in Lbs: ",weight//0.45359237)