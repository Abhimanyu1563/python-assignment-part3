# Python File Handling, API Integration & Exception Management

## 📌 Overview

This project demonstrates core Python concepts through practical tasks:

* File handling (read, write, append)
* API integration using requests
* Exception handling and validation
* Logging errors to a file

---

## 📂 Project Structure

```
part3_api_files.py
python_notes.txt
error_log.txt
README.md
```

---

## 🧩 Task 1 — File Handling

* Created a text file `python_notes.txt`
* Wrote multiple lines using write mode
* Appended additional content using append mode
* Read the file and displayed numbered lines
* Implemented keyword search functionality

---

## 🌐 Task 2 — API Integration

Used the DummyJSON API:

* Fetched 20 products using GET request
* Displayed data in table format
* Filtered products with rating ≥ 4.5
* Sorted filtered results by price (descending)
* Retrieved products from "laptops" category
* Sent a POST request with custom product data

---

## ⚠️ Task 3 — Exception Handling

### Part A — Safe Divide

* Created `safe_divide(a, b)`
* Handles:

  * Division by zero
  * Invalid input types

### Part B — Safe File Reader

* Created `read_file_safe(filename)`
* Handles:

  * FileNotFoundError
* Uses `finally` to confirm execution

### Part C — Safe API Calls

* Wrapped API calls in try-except blocks
* Handles:

  * ConnectionError
  * Timeout
  * General exceptions

### Part D — Input Validation Loop

* Accepts product ID (1–100) or 'quit'
* Validates input before API call
* Displays product details or error message

---

## 📝 Task 4 — Logging

* Created `error_log.txt`
* Logs errors with timestamp
* Format:

```
[YYYY-MM-DD HH:MM:SS] ERROR in function_name: message
```

* Logged:

  * Connection error
  * HTTP 404 error
* Displayed log contents at the end

---

## 🛠️ Technologies Used

* Python 3
* requests library
* Google Colab (for execution)

---

## ▶️ How to Run

1. Install dependencies:

```
pip install requests
```

2. Run the script:

```
python part3_api_files.py
```

---

## 📌 API Used

DummyJSON Products API
https://dummyjson.com/products

---

## ✅ Conclusion

This project integrates file operations, API handling, exception management, and logging into a single workflow, demonstrating practical Python programming skills.
