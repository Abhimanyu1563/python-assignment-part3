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
