## 🐼 Pandas Learning Guide (Beginner → Data Science Ready)

Pandas is **core skill for Data Science**, used for **data cleaning, analysis & preprocessing**.

---

## 1️⃣ What is Pandas?

* Python library for **data manipulation**
* Works with **tabular data** (rows & columns)
* Fast, powerful, easy to use

📦 Install:

```bash
pip install pandas
```

---

## 2️⃣ Import Pandas

```python
import pandas as pd
```

---

## 3️⃣ Pandas Data Structures

### 🔹 Series (1D)

```python
s = pd.Series([10, 20, 30])
print(s)
```

### 🔹 DataFrame (2D – MOST USED)

```python
data = {
    "Name": ["Yash", "Amit", "Neha"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)
print(df)
```

---

## 4️⃣ Reading Files (Very Important)

```python
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")
df = pd.read_json("data.json")
```

---

## 5️⃣ Basic Data Inspection

```python
df.head()      # first 5 rows
df.tail()      # last 5 rows
df.info()      # structure
df.shape       # rows, columns
df.columns     # column names
df.describe()  # statistics
```

---

## 6️⃣ Selecting Data

### 🔹 Select Column

```python
df["Age"]
```

### 🔹 Multiple Columns

```python
df[["Name", "Marks"]]
```

### 🔹 Select Row

```python
df.loc[0]      # by index
df.iloc[0]     # by position
```

---

## 7️⃣ Filtering Data

```python
df[df["Marks"] > 85]
df[(df["Age"] > 20) & (df["Marks"] > 85)]
```

---

## 8️⃣ Add / Modify Columns

```python
df["Passed"] = df["Marks"] > 40
df["Bonus"] = df["Marks"] + 5
```

---

## 9️⃣ Delete Columns / Rows

```python
df.drop("Bonus", axis=1, inplace=True)
df.drop(0, axis=0, inplace=True)
```

---

## 🔟 Handling Missing Values

```python
df.isnull()
df.isnull().sum()

df.fillna(0, inplace=True)
df.dropna(inplace=True)
```

---

## 1️⃣1️⃣ Sorting & Grouping

### 🔹 Sort

```python
df.sort_values("Marks", ascending=False)
```

### 🔹 Group By

```python
df.groupby("Age")["Marks"].mean()
```

---

## 1️⃣2️⃣ Apply Functions

```python
df["Grade"] = df["Marks"].apply(
    lambda x: "A" if x >= 85 else "B"
)
```

---

## 1️⃣3️⃣ Merge & Join (Advanced)

```python
pd.merge(df1, df2, on="ID")
```

---

## 1️⃣4️⃣ Save Data

```python
df.to_csv("output.csv", index=False)
```

---

## 1️⃣5️⃣ Mini Project 🔥

**Student Result Analysis**

* Load CSV
* Find toppers
* Average marks per subject
* Passed / Failed students

---

## 📌 Interview Questions

* Difference between Series and DataFrame?
* `loc` vs `iloc`?
* `apply()` vs `map()`?
* `dropna()` vs `fillna()`?

---

## 🎯 Next Steps

👉 Learn **Matplotlib & Seaborn**
👉 Practice **EDA projects**
👉 Start **Machine Learning preprocessing**

If you want:
✅ **Daily Pandas practice tasks**
✅ **Real dataset with solutions**
✅ **Cheat sheet PDF**

