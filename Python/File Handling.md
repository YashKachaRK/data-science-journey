## 📂 File Handling in Python (Beginner → Practical)

File handling means **reading, writing, and managing files** like `.txt`, `.csv`, `.json`, etc.
Very important for **Data Science & Python projects**.

---

## 1️⃣ Opening a File

```python
file = open("data.txt", "r")  # r = read
```

### File Modes

| Mode | Meaning           |
| ---- | ----------------- |
| `r`  | Read              |
| `w`  | Write (overwrite) |
| `a`  | Append            |
| `x`  | Create file       |
| `rb` | Read binary       |
| `wb` | Write binary      |

---

## 2️⃣ Reading a File

### 🔹 Read Entire File

```python
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
```

### 🔹 Read Line by Line

```python
file = open("data.txt", "r")
for line in file:
    print(line)
file.close()
```

### 🔹 Read All Lines into List

```python
file = open("data.txt", "r")
lines = file.readlines()
print(lines)
file.close()
```

---

## 3️⃣ Writing to a File

### 🔹 Write (Overwrites)

```python
file = open("data.txt", "w")
file.write("Hello Data Science\n")
file.close()
```

### 🔹 Append (Adds content)

```python
file = open("data.txt", "a")
file.write("Python File Handling\n")
file.close()
```

---

## 4️⃣ Best Practice: `with` Statement ⭐

Automatically closes file

```python
with open("data.txt", "r") as file:
    print(file.read())
```

---

## 5️⃣ Working with CSV Files (Very Important)

### 🔹 Read CSV

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

### 🔹 Write CSV

```python
import csv

data = [
    ["Name", "Age"],
    ["Yash", 21],
    ["Amit", 22]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

---

## 6️⃣ File Handling Using Pandas (Data Science Way 🔥)

```python
import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())

df.to_csv("new_data.csv", index=False)
```

---

## 7️⃣ JSON File Handling

```python
import json

data = {
    "name": "Yash",
    "role": "Data Scientist"
}

# Write JSON
with open("data.json", "w") as file:
    json.dump(data, file)

# Read JSON
with open("data.json", "r") as file:
    result = json.load(file)
    print(result)
```

---

## 8️⃣ Check File Exists

```python
import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File not found")
```

---

## 9️⃣ Delete a File

```python
import os
os.remove("data.txt")
```

---

## 🔟 Mini Practice Tasks 🧠

1️⃣ Create a file `student.txt` and store name & marks
2️⃣ Read marks and calculate average
3️⃣ Save results in `result.csv`
4️⃣ Load `result.csv` using Pandas

---

## 📌 Interview Questions

* Difference between `read()` and `readlines()`?
* What is `with open()`?
* Difference between `w` and `a` mode?
* Why is CSV important in Data Science?

---

If you want:
✅ **Notes in PDF**
✅ **Practice problems with solutions**
✅ **Real Data Science file-handling project**

Just tell me 👍
