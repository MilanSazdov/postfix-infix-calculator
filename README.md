# 🧮 Infix & Postfix Notation Calculator  

This project implements an **Infix & Postfix Notation Calculator**, supporting both mathematical expression **conversion and evaluation**. It allows users to:  

- Convert an **infix mathematical expression** to **postfix notation**.  
- Evaluate mathematical expressions using **postfix notation**.  
- Handle **basic arithmetic operations** (+, -, *, /, ^).  
- Detect **mathematical errors** (division by zero, invalid syntax, illegal characters, etc.).  
- Support **unary operators** and **parentheses** for expression grouping.  

The implementation is based on **stack data structures**, **regular expressions for token parsing**, and follows the standard **Shunting-yard algorithm** for infix-to-postfix conversion.  

---

## 📑 Table of Contents

- [Technologies & Features](#-technologies--features)
- [Installation & Usage](#-installation--usage)
- [How It Works](#-how-it-works)
- [License](#-license)
- [Contact](#-contact)

---

## 🛠 Technologies & Features

### 🔹 Technologies Used:
- **Python 3.x** – Core programming language.
- **Regular Expressions (re module)** – Used for parsing and validating mathematical expressions.
- **Stack Data Structure** – Implemented for converting infix to postfix notation and evaluating expressions.

### ⚡ Features:
- **Supports Infix to Postfix Conversion** – Converts standard mathematical expressions into Reverse Polish Notation (RPN).
- **Postfix Expression Evaluation** – Evaluates expressions in postfix notation using a stack.
- **Handles Complex Expressions** – Supports parentheses, power operations (`^`), and decimal numbers.
- **Custom Exception Handling** – Detects and raises errors such as division by zero, illegal characters, and consecutive operators.
- **Interactive CLI Menu** – Provides a user-friendly command-line interface for performing operations.

---

## 🔧 Installation & Usage

### 1️⃣ Clone the Repository
First, clone the repository to your local machine and navigate to the project directory:

```sh
git clone https://github.com/MilanSazdov/postfix-infix-calculator.git
cd postfix-infix-calculator
```

### 2️⃣ Install Dependencies

Ensure you have Python **3.10.14** (or newer) installed. No additional libraries are required as the project only uses built-in Python modules.

If you need to verify your Python version, run:

```sh
python --version
```

### 3️⃣ Run the Program

To start the calculator, execute the following command:

```sh
python calculator.py
```

---

## 🛠 How It Works

This project allows users to **convert infix expressions to postfix notation** and **evaluate mathematical expressions** using a stack-based approach.

### 🔹 **1. Converting Infix to Postfix Notation**
The program follows the **Shunting-yard algorithm**, developed by Edsger Dijkstra, to convert infix expressions (e.g., `3 + 5 * 2`) into postfix notation (Reverse Polish Notation - RPN).

#### 📝 **Steps:**
1. **Scan the expression** from left to right.
2. **Push operands (numbers) directly** to the output.
3. **Push operators to a stack**, respecting operator precedence and associativity.
4. **Handle parentheses** correctly by pushing `(` onto the stack and popping until `)` is encountered.
5. **Pop remaining operators** from the stack once the expression is fully read.

---

### 🔹 **2. Evaluating Postfix Expressions**
Once an expression is converted to **postfix notation**, it can be **evaluated efficiently** using a **stack-based algorithm**.

#### 📝 **Steps:**
1. **Read the expression from left to right**.
2. **Push operands (numbers) onto the stack**.
3. **When an operator is encountered**, pop the required number of operands from the stack, perform the operation, and push the result back onto the stack.
4. **At the end**, the stack will contain only one value: the final result.

---

### 🔹 **3. Handling Errors and Special Cases**
The program includes **robust error handling** to detect invalid mathematical expressions, including:
✔ **Division by zero** (`5 / 0` → Error)  
✔ **Consecutive operators** (`3 ++ 4` → Error)  
✔ **Mismatched parentheses** (`(3 + 5 * 2` → Error)  
✔ **Invalid characters** (`3 & 5` → Error)  
✔ **Complex numbers detection** (`(-1) ^ 0.5` → Error)  

With this approach, the calculator ensures **mathematical correctness and stability**.

---

## 📜 License  
This project is licensed under the [MIT License](LICENSE.md).  
See the LICENSE file for more details.  

---

## 🔗 Useful Links  

- 📖 [README](README.md)  
- ❤️ [Code of Conduct](CODE_OF_CONDUCT.md)  
- 📜 [MIT License](LICENSE.md)  

---

## 📬 Contact  
📧 **Email:** [milansazdov@gmail.com](mailto:milansazdov@gmail.com)  
🐙 **GitHub:** [MilanSazdov](https://github.com/MilanSazdov)  

---

