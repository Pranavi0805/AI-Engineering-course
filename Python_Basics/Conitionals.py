
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


for i in range(10):
    if i == 5:
        continue
    print(i)

print("Outside For Loop")

#Count down from 5
count = 5
while count > 0:
    print(count)
    count -= 1

print("Outside While Loop")

#Loop through a list

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
#Loop with range
for i in range(10): #[0,1,2,3,4]
    print(i)

#Example 1: Checking a condition
num = -50
if num > 0:
    print("Positive Number")
elif num == 0:
    print("Zero")
else:
    print("Negative Number")
    
#Example 2: Nested conditions
age = 3
if age > 18:
    if age < 30:
        print("Young Adult")
    else:
        print("Adult")

#Example 3: Prime number
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
            