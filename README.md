# DSA_101 — Data Structures & Algorithms Learning Journey

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Progress](https://img.shields.io/badge/Progress-Step%201%20%26%20Interview%20Problems-brightgreen.svg)]()
[![Course](https://img.shields.io/badge/Course-Striver's%20A2Z%20DSA-orange.svg)](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Structured DSA learning repository** following [Striver's A2Z DSA Course](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/) — from fundamentals to interview-ready problem solving.

---

## 🎯 Repository Purpose

This repository documents my **complete DSA learning journey** with:
- **Step-by-step fundamentals** (Python basics → Math → Data Structures → Algorithms)
- **Interview problem solutions** (Blind 75 / Striver's SDE Sheet)
- **Multiple approaches** per problem (brute force → optimal)
- **Clean, commented code** with explanations and complexity analysis

---

## 📚 Learning Roadmap (Striver's A2Z)

| Step | Topic | Status | Problems |
|------|-------|--------|----------|
| **1.1** | Language Basics (Python) | ✅ Complete | 7 |
| **1.2** | Basic Mathematics | ✅ Complete | 3 |
| **1.3** | Recursion & Backtracking | 🔄 Planned | — |
| **2.1** | Arrays | 🔄 Planned | — |
| **2.2** | Strings | 🔄 Planned | — |
| **2.3** | Linked Lists | 🔄 Planned | — |
| **2.4** | Stacks & Queues | 🔄 Planned | — |
| **2.5** | Trees & BSTs | 🔄 Planned | — |
| **2.6** | Graphs | 🔄 Planned | — |
| **2.7** | Dynamic Programming | 🔄 Planned | — |
| **3** | **Blind 75 / Interview Problems** | 🟡 Started | 1+ |

> **Current Focus**: Step 1 complete • Beginning interview problems

---

## 📁 Repository Structure

```
DSA_101/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── images/                      # Diagrams & screenshots
│   └── Python-data-structure.jpg
│
├── Step 1 : Learn the basics/
│   ├── Step 1.1: Things to Know in any language/
│   │   ├── 1.1.1 User_Input-Output.py      # I/O, character classification
│   │   ├── 1.1.2 Data type.py              # Python data types demo
│   │   ├── 1.1.3 if-else (Decision Making).py
│   │   ├── 1.1.4 Switch.py                 # Python match-case / if-else alternative
│   │   ├── 1.1.5 for loops.py              # Fibonacci: iterative, memoized, Binet's formula
│   │   ├── 1.1.6 while loops.py
│   │   └── 1.1.7 patterns.py               # Pattern printing problems
│   │
│   └── Step 2 : basic maths/
│       ├── P1 count_digit.py               # Count digits (string slicing + list comp)
│       ├── P2 reverse_bit.py               # Bit reversal (format, zfill)
│       └── P3 HCF.py                       # GCD (math.gcd + Euclidean recursion)
│
└── Some interview problems/
    └── P1 Next_permutation.py              # Optimal O(N) next permutation algorithm
```

---

## 💡 Featured Solutions

### Step 1.1: Language Fundamentals

| File | Concept | Key Techniques |
|------|---------|----------------|
| `1.1.1 User_Input-Output.py` | I/O handling | `input().split()`, string methods (`isalpha`, `islower`) |
| `1.1.2 Data type.py` | Data types | Type checking, casting, mutable vs immutable |
| `1.1.5 for loops.py` | **Fibonacci** | Iterative O(N), **Memoization** (`functools.lru_cache`), **Binet's Formula** O(1) |
| `1.1.7 patterns.py` | Pattern printing | Nested loops, string multiplication |

### Step 1.2: Basic Mathematics

| File | Problem | Approach |
|------|---------|----------|
| `P1 count_digit.py` | Count digits in integer | String slicing `[::-1]`, list comprehension |
| `P2 reverse_bit.py` | Reverse bits of integer | `format(n, 'b')`, `str.zfill()`, bit manipulation |
| `P3 HCF.py` | Highest Common Factor | `math.gcd()`, **Euclidean algorithm** (recursive) |

### Interview Problems (Blind 75 / Striver's SDE Sheet)

| # | Problem | File | Complexity | Technique |
|---|---------|------|------------|-----------|
| 1 | **Next Permutation** | `P1 Next_permutation.py` | **O(N)** time, O(1) space | In-place reversal, pivot finding |

> **Next Permutation Algorithm** (LeetCode 31 / Coding Ninjas):
> 1. Find pivot: rightmost index `i` where `nums[i] < nums[i+1]`
> 2. If no pivot → reverse entire array (highest permutation)
> 3. Find successor: rightmost element > `nums[pivot]`
> 4. Swap pivot & successor
> 5. Reverse suffix (pivot+1 to end)

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
```

### Run Any Solution
```bash
# Navigate to problem directory
cd "Step 1 : Learn the basics/Step 1.1: Things to Know in any language"

# Run a specific problem
python "1.1.5 for loops.py"
# Enter input when prompted (e.g., 10 for Fibonacci)
```

### For Interview Problems
```bash
cd "Some interview problems"
python "P1 Next_permutation.py"
# Output: [2, 3, 0, 0, 1, 4, 5] for input [2, 1, 5, 4, 3, 0, 0]
```

---

## 📖 Learning Resources

| Resource | Link | Purpose |
|----------|------|---------|
| **Striver's A2Z DSA Course** | [takeuforward.org](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/) | Primary structured curriculum |
| **Blind 75 LeetCode** | [leetcode.com](https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions) | Interview preparation |
| **Striver's SDE Sheet** | [takeuforward.org](https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/) | Company-wise problem lists |
| **Python Docs** | [docs.python.org](https://docs.python.org/3/) | Language reference |
| **Big-O Cheatsheet** | [bigocheatsheet.com](https://www.bigocheatsheet.com/) | Complexity reference |

---

## 🏷️ Code Standards

Each solution follows:
- ✅ **Problem statement** as comment (with source link)
- ✅ **Multiple approaches** (brute → better → optimal)
- ✅ **Time & Space complexity** documented
- ✅ **Inline comments** explaining logic
- ✅ **Clean variable names** (PEP 8 compliant)
- ✅ **Type hints** where applicable

---

## 📈 Progress Tracking

```
Step 1: Learn the Basics        ████████░░  80%
  ├─ 1.1 Language Basics        ██████████  100%
  └─ 1.2 Basic Maths            ██████████  100%

Step 2: Data Structures         ░░░░░░░░░░    0%
Step 3: Algorithms              ░░░░░░░░░░    0%
Step 4: Advanced Topics         ░░░░░░░░░░    0%

Interview Problems              ██░░░░░░░░░   10%
  └─ Blind 75 / SDE Sheet       ██░░░░░░░░░   10%
```

---

## 🤝 Contributing

This is a personal learning repo, but suggestions welcome!

1. Fork the repository
2. Add a solution with **multiple approaches** + **complexity analysis**
3. Follow the existing **file naming convention**
4. Submit a PR with problem description

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 👤 Author

**Prady029** — [GitHub](https://github.com/Prady029) | [LinkedIn](https://linkedin.com/in/prady029)

> *"The expert in anything was once a beginner."* — Helen Hayes

---

*Last updated: October 2024*