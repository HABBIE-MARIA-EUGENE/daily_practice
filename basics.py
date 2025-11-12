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



weight = int(input("weight: "))

unit = input("(K)g or (L)bs: ")


if unit.upper() =="L":
    converted = weight * 0.45
    print("Weight in Kg: ",converted)
    print("Weight in Kg: "+str(converted))

else:
    converted = weight/0.45
    print("Weight in Lbs: ",converted)
    print("Weight in Lbs: "+str(converted))




i = 1

while i<=5:
    print(i)
    i = i + 1


i = 1

while i<=1_000:
    print(i)
    i = i + 1




i = 1

while i<=10:
    print(i*"*")
    i = i + 1


#list

names = ["habbie", "maria", "eugene", "hello", "world"]

print(names)

print(names[0])
print(names[-1])
print(names[-2])

names[0] = "Habbie"
print(names)

print(names[0:3])   #upto end index excluding end index




numbers = [1,2,3,4,5]
print(numbers)

numbers.append(6)  #appends at the end of the list
print(numbers)

numbers.insert(0,-1)
print(numbers)

numbers.remove(3)
print(numbers)


print(1 in numbers)
print(7 in numbers)


print(len(numbers))  #to get number of items in the list


numbers.clear()
print(numbers)


numbers = [1,2,3,4,5,6]

print(numbers)

for item in numbers:
    print(item)

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i+1