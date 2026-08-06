import os

# Base directory of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create a data folder inside Files
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

sample_file = os.path.join(DATA_DIR, "sample.txt")
languages_file = os.path.join(DATA_DIR, "languages.txt")
new_sample_file = os.path.join(DATA_DIR, "new_sample.txt")
copy_file = os.path.join(DATA_DIR, "copy.txt")
binary_file = os.path.join(DATA_DIR, "binary.bin")
image_file = os.path.join(DATA_DIR, "image.jpg")
fruits_file = os.path.join(DATA_DIR, "fruits.txt")


# Writing to a File
# 'w' mode creates a new file or overwrites an existing file.

with open(sample_file, "w") as file:
    file.write("Hello Python\n")
    file.write("Welcome to File Handling")


# Reading a File
# 'r' mode reads the contents of a file.

with open(sample_file, "r") as file:
    print(file.read())


# Reading One Line
# readline() reads one line at a time.

with open(sample_file, "r") as file:
    print(file.readline())


# Reading All Lines
# readlines() returns all lines as a list.

with open(sample_file, "r") as file:
    print(file.readlines())


# Appending to a File
# 'a' mode adds data without deleting existing content.

with open(sample_file, "a") as file:
    file.write("\nThis line is appended.")


# Writing Multiple Lines
# writelines() writes multiple lines from a list.

lines = [
    "Python\n",
    "Java\n",
    "C++\n"
]

with open(languages_file, "w") as file:
    file.writelines(lines)


# Using with Statement
# Automatically closes the file after use.

with open(sample_file, "r") as file:
    print(file.read())


# File Exists Check
# Check whether a file exists.

if os.path.exists(sample_file):
    print("File Exists")
else:
    print("File Not Found")


# Delete a File
# Removes a file permanently.

if os.path.exists(languages_file):
    os.remove(languages_file)
    print("languages.txt Deleted")


# Rename a File
# Renames an existing file.

if os.path.exists(sample_file):

    if os.path.exists(new_sample_file):
        os.remove(new_sample_file)

    os.rename(sample_file, new_sample_file)
    print("File Renamed Successfully")


# File Modes

# r  -> Read
# w  -> Write
# a  -> Append
# x  -> Create
# rb -> Read Binary
# wb -> Write Binary


# Tell Position
# tell() returns the current cursor position.

with open(new_sample_file, "r") as file:
    print(file.tell())
    print(file.read(5))
    print(file.tell())


# Move Cursor
# seek() moves the cursor.

with open(new_sample_file, "r") as file:
    file.seek(0)
    print(file.read(5))


# Copy File
# Copies contents from one file to another.

with open(new_sample_file, "r") as source:
    data = source.read()

with open(copy_file, "w") as destination:
    destination.write(data)


# Count Lines
# Counts total lines.

with open(new_sample_file, "r") as file:
    count = len(file.readlines())

print("Lines:", count)


# Count Words
# Counts total words.

with open(new_sample_file, "r") as file:
    words = file.read().split()

print("Words:", len(words))


# Count Characters
# Counts total characters.

with open(new_sample_file, "r") as file:
    text = file.read()

print("Characters:", len(text))


# Read Binary File
# Reads binary files such as images.

if os.path.exists(image_file):
    with open(image_file, "rb") as file:
        data = file.read(20)
        print(data)
else:
    print("image.jpg not found.")


# Write Binary File
# Writes binary data.

with open(binary_file, "wb") as file:
    file.write(b"Python")


# Exception Handling
# Handles file-related errors.

try:
    with open(os.path.join(DATA_DIR, "abc.txt"), "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist")


# Example 1
# Write and Read a List of Items.

def write_items_to_file(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n")


def read_items_from_file(filename):
    try:
        with open(filename, "r") as file:
            items = file.readlines()

        print("Items in the file:")

        for item in items:
            print(item.strip())

    except FileNotFoundError:
        print("File not found!")


fruits = ["Apple", "Banana", "Cherry", "Dates"]

write_items_to_file(fruits_file, fruits)

read_items_from_file(fruits_file)