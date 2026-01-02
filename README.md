# Contact Book Manager (Console Application)

## 📌 Overview
A console-based contact management system built using Python.  
The application supports adding, searching, updating, and deleting contacts with **persistent storage** and **real-world validation rules**.

This project is designed using **production-style data modeling**, avoiding name-based identifiers and enforcing uniqueness for phone numbers and email addresses.

---

## 🧠 Key Concepts Used
- Dictionary & Nested Dictionary
- Functions & Modular Design
- while loop (menu-driven program)
- if / elif / else conditions
- try / except for error handling
- String cleaning (strip, lower, replace)
- File handling using JSON
- Data validation & uniqueness enforcement

---

## 🗂 Data Design
Contacts are stored using **system-generated IDs** as primary keys.

Example:
```python
{
  "C001": {
    "name": "Arun",
    "phone": "9876543210",
    "email": "arun@gmail.com"
  }
}
