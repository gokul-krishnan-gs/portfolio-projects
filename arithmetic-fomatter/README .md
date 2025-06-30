# Arithmetic Formatter 🧮

## 📘 Project Description

The **Arithmetic Formatter** takes a list of simple arithmetic problems (addition and subtraction only), formats them vertically and side-by-side, and optionally displays their answers.

This mimics how problems are arranged for school students to solve step-by-step.

---

## 📌 Features

- Validates input problems (maximum 5)
- Only supports addition (`+`) and subtraction (`-`)
- Ensures operands contain only digits and are ≤ 4 digits
- Aligns numbers neatly in columns
- Optionally displays answers

---

## 🧠 Example

### Input:
```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

### Output:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

### With Answers:
```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

### Output:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

---

## 🛠 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/arithmetic-formatter.git
   cd arithmetic-formatter
   ```

2. Run the Python file:
   ```bash
   python arithmetic_formatter.py
   ```

---

## ✅ Requirements

- Python 3.x
- No third-party libraries needed

---

## 🎓 Built With

- Python 🐍

## 🙋‍♂️ Author

**Gokul Krishnan**  
LinkedIn: [linkedin.com/in/gokulkrishnangs](https://linkedin.com/in/gokul-krishnan-gs/)
