import re

# search()
# Returns first match

text = "My phone number is 9876543210 and my email is test123@gmail.com"

match = re.search(r"\d{10}", text)

if match:
    print("Phone Number:", match.group()) #-- 9876543210


# match()
# Checks only at beginning of string

result = re.match(r"My", text)
print(result.group() if result else "No Match")

result = re.match(r"phone", text)
print(result)


# fullmatch()
# Entire string must match

print(re.fullmatch(r"\d+", "12345"))
print(re.fullmatch(r"\d+", "123abc"))


# findall()
# Returns all matches

sentence = "Apple costs 100, Banana costs 50"

numbers = re.findall(r"\d+", sentence)
print(numbers)

words = re.findall(r"[A-Za-z]+", sentence)
print(words)


# finditer()
# Returns iterator of match objects

for match in re.finditer(r"\d+", sentence):
    print(match.group(), "Position:", match.start())


# sub()
# Replace pattern

text = "Python is easy"

new_text = re.sub("easy", "powerful", text)

print(new_text)


# split()
# Split using regex

text = "Apple,Banana;Orange Mango"

print(re.split(r"[,; ]+", text))


# compile()
# Compile regex once

pattern = re.compile(r"\d+")

print(pattern.findall("123 abc 456"))


# Character Classes

sample = "Python123 @#$"

print(re.findall(r"\d", sample))     # Digits

print(re.findall(r"\D", sample))     # Non-digits

print(re.findall(r"\w", sample))     # Letters, digits, underscore

print(re.findall(r"\W", sample))     # Special characters

print(re.findall(r"\s", "A B\tC\n")) # Spaces

print(re.findall(r"\S", "A B\tC\n")) # Non-spaces


# Quantifiers

text = "aaa aa a aaaa"

print(re.findall(r"a+", text))

print(re.findall(r"a*", text))

print(re.findall(r"a?", text))

print(re.findall(r"a{2}", text))

print(re.findall(r"a{2,4}", text))


# Anchors

print(re.search(r"^Hello", "Hello World"))

print(re.search(r"World$", "Hello World"))


# OR Operator

text = "cat dog tiger"

print(re.findall(r"cat|dog", text))


# Groups

text = "John 25"

match = re.search(r"([A-Za-z]+)\s(\d+)", text)

print("Name:", match.group(1))
print("Age:", match.group(2))


# Email Validation

email = "test123@gmail.com"

pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

print(bool(re.fullmatch(pattern, email)))


# Phone Number

phone = "9876543210"

print(bool(re.fullmatch(r"\d{10}", phone)))


# Password Validation

password = "Python@123"

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'

print(bool(re.fullmatch(pattern, password)))


# Date Extraction

text = "DOB: 15/08/2026"

print(re.findall(r"\d{2}/\d{2}/\d{4}", text))


# URL Extraction

text = "Visit https://www.google.com"

print(re.findall(r"https?://\S+", text))


# Remove Extra Spaces

text = "Python     is     awesome"

print(re.sub(r"\s+", " ", text))


# Only Alphabets

text = "Python123@#!"

print(re.findall(r"[A-Za-z]+", text))


# Only Numbers

text = "abc123xyz456"

print(re.findall(r"\d+", text))


# Hexadecimal Color Code

text = "Color code: #FFAA11"

print(re.findall(r"#[A-Fa-f0-9]{6}", text))


# Example 1:
import re

def clean_text(text):
    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)
    # Remove extra spaces
    text = " ".join(text.split())
    # Convert to lowercase
    return text.lower()

input_text = "   Hello, World.!!! Welcome to Python, Programming....    "
cleaned_text = clean_text(input_text)
print("Cleaned Text: ", cleaned_text)
