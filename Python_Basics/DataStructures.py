
# 1. LIST
# Ordered, Mutable, Allows Duplicates
numbers = [10, 20, 30, 40]

print("Original:", numbers)

# Add elements
numbers.append(50)
print("append(50):", numbers)

numbers.insert(1, 15)
print("insert(1,15):", numbers)

numbers.extend([60, 70])
print("extend([60,70]):", numbers)

# Remove elements
numbers.remove(30)
print("remove(30):", numbers)

numbers.pop()
print("pop():", numbers)

numbers.pop(0)
print("pop(0):", numbers)

# Access
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# Slicing
print("Slice:", numbers[1:4])

# Update
numbers[0] = 100
print("Updated:", numbers)

# Sort
numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reverse:", numbers)

# 2. TUPLE
# Ordered, Immutable, Allows Duplicates

t = (1, 2, 3, 4, 2)

print("Tuple:", t)

print("First:", t[0])

print("Count of 2:", t.count(2))

print("Index of 3:", t.index(3))

# Cannot modify
# t[0] = 100   # Error

# 3. SET
# Unordered, Mutable, No Duplicates
s = {1, 2, 3, 4}
print("Original:", s)

s.add(5)
print("add(5):", s)

s.remove(2)
print("remove(2):", s)

s.discard(100)      # Doesn't throw error
print("discard(100):", s)

A = {1,2,3}
B = {3,4,5}

print("Union:", A | B)

print("Intersection:", A & B)

print("Difference:", A - B)

print("Symmetric Difference:", A ^ B)

# 4. FROZENSET
# Immutable Set
fs = frozenset([1,2,3,4])

print(fs)

# fs.add(5)  # Error

# 5. DICTIONARY
# Key-Value Pair
# Mutable

student = {
    "name":"Alice",
    "age":22,
    "marks":95
}

print(student)

print("Name:", student["name"])

student["city"] = "Hyderabad"

print("After Adding City:", student)

student["age"] = 23

print("Updated Age:", student)

student.pop("marks")

print("After Pop:", student)

print("Keys:", student.keys())

print("Values:", student.values())

print("Items:", student.items())

# 6. STRING
# Immutable Sequence
text = "Python"

print(text)

print(text.upper())

print(text.lower())

print(text.replace("Python","Java"))

print(text[0])

print(text[-1])

print(text[1:5])

print("Length:", len(text))

# 7. RANGE
# Immutable Sequence

r = range(1,11)

print(list(r))

for i in range(5):
    print(i, end=" ")

print()

# 8. BYTEARRAY
# Mutable Bytes

b = bytearray([65,66,67])

print(b)

b[0] = 97

print(b)

print(b.decode())

# 9. BYTES
# Immutable Bytes
data = bytes([65,66,67])

print(data)

print(data.decode())

# data[0]=97  -- Error


# 10. QUEUE USING LIST

queue = []

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

print("Dequeued:", queue.pop(0))

print(queue)


# 11. STACK USING LIST

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

print("Pop:", stack.pop())

print(stack)

# 12. DEQUE
# Double Ended Queue
from collections import deque

dq = deque([1,2,3])

dq.append(4)

dq.appendleft(0)

print(dq)

dq.pop()

dq.popleft()

print(dq)


# 13. HEAP (Priority Queue)
import heapq

heap = []

heapq.heappush(heap,30)
heapq.heappush(heap,10)
heapq.heappush(heap,20)
heapq.heappush(heap,5)

print(heap)

print("Smallest:", heapq.heappop(heap))

print(heap)

# 14. COUNTER

from collections import Counter

words = ["apple","banana","apple","orange","banana","apple"]

count = Counter(words)

print(count)

print(count["apple"])


# 15. DEFAULTDICT
from collections import defaultdict

d = defaultdict(int)

d["A"] += 1
d["B"] += 5

print(d)

print(d["C"])   # Default 0

# 16. NAMEDTUPLE
from collections import namedtuple

Student = namedtuple("Student",["name","age"])

s = Student("John",21)

print(s.name)

print(s.age)

# 17. ENUMERATE

fruits = ["Apple","Banana","Orange"]

for index,value in enumerate(fruits):
    print(index,value)

# 18. ZIP
names = ["Alice","Bob","Charlie"]
marks = [95,88,91]

for name,mark in zip(names,marks):
    print(name,mark)

# 19. COMPREHENSIONS

squares = [x*x for x in range(6)]

print(squares)

even = {x for x in range(10) if x%2==0}

print(even)

square_dict = {x:x*x for x in range(5)}

print(square_dict)


# 20. NESTED DATA STRUCTURES

students = [
    {"name":"Alice","marks":[90,95]},
    {"name":"Bob","marks":[80,85]}
]
print(students)
print(students[0]["marks"][1])

# Example 1: Word Frequency
sentence = input("Enter a Sentence: ")

# Split the sentence into words
words = sentence.split()

# Initialize Dictionary
word_count = {}

# Count word frequence
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        
print(word_count)
