# JS Runtime

A lightweight JavaScript runtime built in Python using the Google V8 JavaScript Engine through PyMiniRacer.

This project executes JavaScript code from `.js` files, captures console output, and prints the results to the terminal. It demonstrates how a non-JavaScript language can be used to run JavaScript programs while providing a simple and extensible runtime architecture.

---

## Features

### JavaScript Execution

* Execute JavaScript files directly from the command line
* Support for modern JavaScript syntax through Google's V8 Engine
* Console output capturing and display
* Error handling for runtime exceptions

### Supported JavaScript Concepts

* Variable declarations (`let`, `const`)
* Primitive data types (`number`, `string`, `boolean`)
* Arrays and Objects
* Functions and Arrow Functions
* Conditional Statements (`if`, `else if`, `else`)
* Loops (`for`, `while`, `do...while`)
* Array Methods (`map`, `filter`, `reduce`, `find`, etc.)
* String Methods
* Math Operations (`Math.floor`, `Math.random`, etc.)
* Spread and Rest Operators
* Modern ES6+ JavaScript Features

---

## Project Structure

```text
js-runtime/
│
├── runtime/
│   ├── interpreter.py
│   └── version.py
│
├── tests/
│   ├── tc1.js
│   ├── tc2.js
│   ├── tc3.js
│   ├── tc4.js
│   └── tc5.js
│
├── examples/
│   └── hello.js
│
├── assets/
│   ├── tc1.png
│   ├── tc3.png
│   └── tc5.png
│
├── run.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Architecture

```text
JavaScript File
        │
        ▼
      run.py
        │
        ▼
     JS Runtime
        │
        ▼
Google V8 Engine
 (PyMiniRacer)
        │
        ▼
 Console Output
  Collection Layer
        │
        ▼
      Terminal
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/js-runtime.git
cd js-runtime
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

```text
Python 3.13+
py-mini-racer==0.6.0
```

---

## Usage

Run a JavaScript file using:

```bash
python run.py <javascript_file>
```

Example:

```bash
python run.py tests/tc1.js
```

---

## Example

### JavaScript Input

```javascript
console.log("Hello World");
```

### Output

```text
Hello World
```

---

## Sample Test Cases

### TC1 – Odd / Even Checker

Input:

```javascript
let num = 7;

if (num % 2 === 0) {
    console.log(num + " is Even");
} else {
    console.log(num + " is Odd");
}
```

Output:

```text
7 is Odd
```

---

### TC2 – Triangle Pattern

Output:

```text
*
**
***
****
*****
```

---

### TC3 – Armstrong Number

Output:

```text
true
false
```

---

### TC4 – Array Reverse

Output:

```text
Original: 1, 2, 3, 4, 5
Reversed: 5, 4, 3, 2, 1
```

---

### TC5 – Palindrome Check

Output:

```text
racecar is a Palindrome
```

---

## Design Decisions

Instead of implementing a JavaScript parser and interpreter from scratch, this project embeds Google's V8 JavaScript Engine through PyMiniRacer.

### Benefits

* High JavaScript compatibility
* Fast execution speed
* Support for modern JavaScript features
* Lightweight Python integration
* Reliable handling of JavaScript execution

The runtime focuses on:

* Reading JavaScript source files
* Executing code safely through V8
* Capturing console output
* Displaying results in the terminal

---

## How It Works

1. User provides a JavaScript file.
2. `run.py` reads the file contents.
3. The JavaScript code is passed to the runtime.
4. The runtime executes the code using the V8 Engine.
5. Console output is captured and stored.
6. Captured output is printed to the terminal.

---

## Running Included Test Cases

```bash
python run.py tests/tc1.js
python run.py tests/tc2.js
python run.py tests/tc3.js
python run.py tests/tc4.js
python run.py tests/tc5.js
```

---

## Future Improvements

* Interactive REPL Mode
* Multiple File Execution
* Module Support
* Custom JavaScript APIs
* Enhanced Error Reporting
* Execution Statistics

---

## License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

## Author

**Dipan Pramanik**

Built as a hackathon project to demonstrate JavaScript runtime execution using Python and Google's V8 Engine.
