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

# -------- Task 2: API Integration --------


import requests

# STEP 1 — Fetch Products
print("\n===== FETCHING PRODUCTS =====")

url = "https://dummyjson.com/products?limit=20"
response = requests.get(url)
data = response.json()

products = data["products"]

print("\nID | Title | Category | Price | Rating")
print("-" * 60)

for p in products:
    print(f"{p['id']} | {p['title']} | {p['category']} | ${p['price']} | {p['rating']}")


# STEP 2 — Filter & Sort
print("\n===== FILTERED PRODUCTS (Rating ≥ 4.5) =====")

filtered = [p for p in products if p["rating"] >= 4.5]
sorted_products = sorted(filtered, key=lambda x: x["price"], reverse=True)

for p in sorted_products:
    print(f"{p['title']} - ${p['price']} - Rating: {p['rating']}")


# STEP 3 — Category (Laptops)
print("\n===== LAPTOPS CATEGORY =====")

url = "https://dummyjson.com/products/category/laptops"
response = requests.get(url)
data = response.json()

laptops = data["products"]

for laptop in laptops:
    print(f"{laptop['title']} - ${laptop['price']}")


# STEP 4 — POST Request
print("\n===== POST REQUEST =====")

url = "https://dummyjson.com/products/add"

new_product = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

response = requests.post(url, json=new_product)
result = response.json()

print("Response from server:")
print(result)
