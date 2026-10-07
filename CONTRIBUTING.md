# Contributing to DSA_101

We welcome contributions to this Data Structures & Algorithms learning repository! Whether you're adding new problem solutions, improving explanations, or fixing bugs, your help makes this resource better for everyone.

## 🚀 Quick Start

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/DSA_101.git
   cd DSA_101
   ```

3. **Set up development environment** (optional - pure Python):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install pytest black isort flake8
   ```

4. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

5. **Make your changes** and test them

6. **Submit a pull request**

## 🔧 Development Setup

### Prerequisites
- Python 3.8+
- Git
- No external dependencies (pure Python standard library)

### Environment Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install pytest black isort flake8
```

### Running Solutions
```bash
# Run any solution directly
python "Step 1 : Learn the basics/Step 1.1: Things to Know in any language/1.1.5 for loops.py"

# Run interview problems
python "Some interview problems/P1 Next_permutation.py"

# Run all Python files (syntax check)
find . -name "*.py" -not -path "./.git/*" | xargs python -m py_compile
```

## 📁 Repository Structure

```
DSA_101/
├── README.md                           # Main documentation
├── LICENSE                             # MIT License
├── requirements.txt                    # Dev dependencies
├── images/                             # Diagrams
├── .github/
│   ├── workflows/                      # CI/CD
│   └── ISSUE_TEMPLATE/                 # Issue templates
├── Step 1 : Learn the basics/
│   ├── Step 1.1: Things to Know in any language/
│   │   ├── 1.1.1 User_Input-Output.py
│   │   ├── 1.1.2 Data type.py
│   │   ├── 1.1.3 if-else (Decision Making).py
│   │   ├── 1.1.4 Switch.py
│   │   ├── 1.1.5 for loops.py
│   │   ├── 1.1.6 while loops.py
│   │   └── 1.1.7 patterns.py
│   └── Step 2 : basic maths/
│       ├── P1 count_digit.py
│       ├── P2 reverse_bit.py
│       └── P3 HCF.py
└── Some interview problems/
    └── P1 Next_permutation.py
```

## 📝 Code Style

- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- Line length: 88 characters (Black default)

```bash
# Format
black .

# Sort imports
isort .

# Check
flake8 . --max-line-length=88 --extend-ignore=E203,W503 --exclude=.git,__pycache__,.venv,venv,env,images
```

## ✨ Contribution Guidelines

### What We Welcome
- **New problem solutions** from Blind 75, Striver's SDE Sheet, LeetCode
- **Multiple approaches** per problem (brute force → optimal)
- **Better explanations** and comments
- **Complexity analysis** (time/space) for each approach
- **Test cases** and edge case handling
- **Documentation improvements** in README

### Solution Template
Each new problem solution should follow this structure:

```python
# Problem: [Problem Name] - [Source Link]
# Difficulty: [Easy/Medium/Hard]
# Topic: [Array/String/Tree/DP/etc.]

# Approach 1: Brute Force
# Time: O(...) | Space: O(...)
def brute_force_solution(input):
    """
    Explanation of brute force approach.
    """
    pass

# Approach 2: Optimized
# Time: O(...) | Space: O(...)
def optimized_solution(input):
    """
    Explanation of optimized approach.
    Key insight: ...
    """
    pass

# Approach 3: Most Optimal (if applicable)
# Time: O(...) | Space: O(...)
def optimal_solution(input):
    """
    Explanation of most optimal approach.
    Key insight: ...
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        # (input, expected_output)
    ]
    for inp, expected in test_cases:
        result = optimal_solution(inp)
        assert result == expected, f"Failed: {inp} -> {result} (expected {expected})"
    print("All tests passed!")
```

### File Naming Convention
- Use descriptive names: `P1_two_sum.py`, `P2_binary_search.py`
- Prefix with problem number from the source (Blind 75, SDE Sheet)
- Use underscores, not spaces

### Directory Placement
- **Fundamentals**: `Step 1 : Learn the basics/` - language basics, math
- **Data Structures**: `Step 2 : Data Structures/` - arrays, strings, linked lists, trees, graphs
- **Algorithms**: `Step 3 : Algorithms/` - sorting, searching, DP, greedy
- **Interview Problems**: `Some interview problems/` - Blind 75, SDE Sheet problems

## 📋 Pull Request Guidelines

### Before Submitting
- [ ] Code follows style guidelines (`black`, `isort`, `flake8` pass)
- [ ] Solution includes multiple approaches (brute → optimal)
- [ ] Time/space complexity documented for each approach
- [ ] Inline comments explain key insights
- [ ] Test cases included in `if __name__ == "__main__":` block
- [ ] README.md updated if adding new problem categories

### Pull Request Description
Include:
- **Problem**: Which problem(s) does this solve?
- **Source**: LeetCode number, Blind 75 index, SDE Sheet reference
- **Approaches**: What approaches are included?
- **Complexity**: Time/space for each approach
- **Testing**: How was this tested?

### Example PR Description
```
## Problem
LeetCode 15. 3Sum (Blind 75 #15, Medium)

## Source
https://leetcode.com/problems/3sum/

## Approaches
1. Brute Force: O(N³) time, O(1) space - three nested loops
2. Two Pointers: O(N²) time, O(1) space - sort + two pointers
3. Hash Set: O(N²) time, O(N) space - hash set for duplicates

## Complexity
- Best: Two Pointers O(N²) time, O(1) space
- All approaches tested with edge cases

## Testing
- Verified with LeetCode test cases
- Added custom edge cases: empty array, all zeros, duplicates
```

## 🧪 Testing Guidelines

### Manual Testing
```bash
# Run your solution
python "Some interview problems/PXX_problem_name.py"

# Verify output matches expected
```

### Adding Test Cases
Include comprehensive test cases:
```python
test_cases = [
    # Basic cases
    ([1,2,3,4,5], 9, [[1,3,5], [2,3,4]]),
    # Edge cases
    ([], 0, []),
    ([0,0,0], 0, [[0,0,0]]),
    # Negative numbers
    ([-1,0,1,2,-1,-4], 0, [[-1,-1,2], [-1,0,1]]),
]
```

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Problem**: Which problem/solution has the bug?
2. **Input**: What input causes the issue?
3. **Expected vs Actual**: What should happen vs what happens
4. **Error Messages**: Full traceback if applicable
5. **Environment**: Python version, OS

## 💡 Feature Requests

For new features:
1. **Check existing issues** to avoid duplicates
2. **Describe the learning value** - how does this help DSA learners?
3. **Propose implementation** if you have ideas
4. **Consider curriculum alignment** - fits Striver's A2Z roadmap?

## 📚 Documentation

- Update README.md for new problems/categories
- Add problem to the appropriate tracking table
- Include complexity in solution comments
- Reference source (LeetCode, Striver, etc.)

## 🤝 Community Guidelines

- **Be respectful** and inclusive
- **Help others** learn DSA concepts
- **Explain the "why"** - not just the "how"
- **Ask questions** if something is unclear
- **Provide constructive feedback**

## 📞 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For DSA questions and general discussion
- **Striver's A2Z Course**: [takeuforward.org](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/)

## 🙏 Learning Together

This repo is a learning journey. Every solution added helps someone else understand DSA better. Whether you're a beginner adding your first two-pointer solution or an expert optimizing a DP approach - thank you for contributing!

> *"The best way to learn is to teach. The best way to teach is to write code that others can learn from."*

Thank you for contributing to DSA_101! 🎉