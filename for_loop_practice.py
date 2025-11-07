for i in "apple":
    print(i,end=",")
    
print()

for i in range(5):
    print(i,end=",")
    
for i in range(1,10):
    print(f"{i}X2={i*2}")



a=int(input("A = "))
b=int(input("B = "))

for i in range (a+1,b):
    print(i,end=",")


a=1
b=11

for i in range (a+1,b):
    if (i%2==0):
        print(i,end=",")



a=1
b=11

count=0

for i in range(a+1,b):
    if (i%2==0):
        print(i,end=",")
        count+=1
print()        
print(count)



a=1
b=10
e_count=0
o_count=0

odd=[]
even=[]

for i in range(a,b+1):
    if (i%2==0):
        even.append(i)
        o_count+=1
    else:
        print(i,end=",")
        odd.append(i)
        e_count+=1
print()    
print(even)
print(odd)
print(o_count)
print(e_count)




a=1
b=100
d_count=0

for i in range(a,b+1):
    if i%3==0 and i%5==0:
        print(i)
        d_count+=1
print(d_count)        


sum=0

for i in range(1,5+1):
    print(i,end=",")
    sum+=i
print(sum)

count=2
sum=0


for i in range(count):
    a=int(input())
    sum+=a

print(sum)