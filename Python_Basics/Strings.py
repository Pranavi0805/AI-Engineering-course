# Creating Strings
# Strings are immutable sequences of characters.

text = "Python"
print(text)


# Access Characters
# Access characters using indexing.

text = "Python"

print(text[0])
print(text[-1])


# String Slicing
# Extract part of a string.

text = "Programming"

print(text[0:6])
print(text[3:])
print(text[:5])
print(text[::-1])


# String Length
# Returns the number of characters.

text = "Python"

print(len(text))


# String Concatenation
# Combine two or more strings.

first = "Hello"
second = "World"

print(first + " " + second)


# String Repetition
# Repeat a string multiple times.

print("Hi " * 3)


# Uppercase
# Converts all characters to uppercase.

text = "python"

print(text.upper())


# Lowercase
# Converts all characters to lowercase.

text = "PYTHON"

print(text.lower())


# Capitalize
# Converts first character to uppercase.

text = "python programming"

print(text.capitalize())


# Title
# Converts first letter of every word to uppercase.

text = "python programming"

print(text.title())


# Swapcase
# Converts uppercase to lowercase and vice versa.

text = "PyThOn"

print(text.swapcase())


# Strip
# Removes spaces from both ends.

text = "   Python   "

print(text.strip())


# Lstrip
# Removes spaces from the left.

print(text.lstrip())


# Rstrip
# Removes spaces from the right.

print(text.rstrip())


# Replace
# Replaces one substring with another.

text = "I like Java"

print(text.replace("Java", "Python"))


# Find
# Returns the first occurrence index.

text = "Python Programming"

print(text.find("Pro"))


# Index
# Similar to find(), but raises an error if not found.

print(text.index("Programming"))


# Count
# Counts occurrences of a substring.

text = "banana"

print(text.count("a"))


# Startswith
# Checks whether string starts with a substring.

text = "Python"

print(text.startswith("Py"))


# Endswith
# Checks whether string ends with a substring.

print(text.endswith("on"))


# Split
# Splits string into a list.

text = "Python Java C++"

print(text.split())


# Join
# Joins list elements into a string.

languages = ["Python", "Java", "C++"]

print(", ".join(languages))


# Isalpha
# Returns True if all characters are alphabets.

print("Python".isalpha())


# Isdigit
# Returns True if all characters are digits.

print("12345".isdigit())


# Isalnum
# Returns True if string contains only letters and numbers.

print("Python123".isalnum())


# Isspace
# Returns True if string contains only spaces.

print("   ".isspace())


# Islower
# Checks whether all letters are lowercase.

print("python".islower())


# Isupper
# Checks whether all letters are uppercase.

print("PYTHON".isupper())


# Center
# Centers the string within a specified width.

print("Python".center(20, "-"))


# Ljust
# Left-aligns the string.

print("Python".ljust(15, "."))


# Rjust
# Right-aligns the string.

print("Python".rjust(15, "."))


# Zfill
# Pads the string with leading zeros.

print("25".zfill(5))


# String Formatting using format()
# Inserts values into placeholders.

name = "Pranavi"
age = 22

print("Name: {}, Age: {}".format(name, age))


# f-String
# Modern and recommended way of formatting strings.

name = "Pranavi"
marks = 95

print(f"{name} scored {marks} marks.")


# Membership Operators
# Checks whether a substring exists.

text = "Python Programming"

print("Python" in text)

print("Java" not in text)


# Lexicographical Comparison
# Compares strings alphabetically.

print("apple" < "banana")


# ASCII Value
# ord() returns ASCII value, chr() returns character.

print(ord('A'))

print(chr(65))


# Reverse String
# Reverse using slicing.

text = "Python"

print(text[::-1])


# Palindrome Check
# Checks if a string reads the same forwards and backwards.

text = "madam"

print(text == text[::-1])


# Count Vowels
# Counts vowels in a string.

text = "Programming"

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print(count)


# Remove Spaces
# Removes all spaces from a string.

text = "Python Programming Language"

print(text.replace(" ", ""))


# Example 1:
def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

input_text = input("Enter a string: ")
if is_palindrome(input_text):
    print(f'"{input_text}" is a palindrome.')
else:
    print(f'"{input_text}" is not a palindrome.')
