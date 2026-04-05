# -------- Task 1: File Write --------

filename = "python_notes.txt"

notes = [
    "Topic 1: Variables store data. Python is dynamically typed.",
    "Topic 2: Lists are ordered and mutable.",
    "Topic 3: Dictionaries store key-value pairs.",
    "Topic 4: Loops automate repetitive tasks.",
    "Topic 5: Exception handling prevents crashes."
]

# Write mode
with open(filename, "w", encoding="utf-8") as file:
    for line in notes:
        file.write(line + "\n")

print("File written successfully.")

# Append mode
with open(filename, "a", encoding="utf-8") as file:
    file.write("Topic 6: Functions help reuse code.\n")
    file.write("Topic 7: APIs allow communication between systems.\n")

print("Lines appended.")

# -------- Task 1: File Read --------

# Read file and print numbered lines
with open(filename, "r", encoding="utf-8") as file:
    lines = file.readlines()

print("\nNumbered Lines:")
for i, line in enumerate(lines, start=1):
    print(f"{i}. {line.strip()}")

# Count total lines
print(f"\nTotal number of lines: {len(lines)}")

# Keyword search
keyword = input("\nEnter a keyword to search: ").lower()

matches = [line.strip() for line in lines if keyword in line.lower()]

if matches:
    print("\nMatching lines:")
    for line in matches:
        print(line)
else:
    print("No matching lines found.")
