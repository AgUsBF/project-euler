# Project Euler Solutions

## 🔍 About

This repository contains my solutions to the problems presented by [Project Euler](https://projecteuler.net/).

## 🗂️ Structure

The repository is organized as follows:

- Each problem is contained in its own directory, named according to the problem number (e.g., `Problem_1`, `Problem_2`, etc.).
- Each directory contains:
  - `Problem.md`: A markdown file presenting the problem along with a brief description of the approach taken.
  - `solution.py`: The Python script used to solve the problem.
  - `test_solution.py`: A test file checking the result for test cases.

## Usage

To run the scripts in a python interactive terminal just import the function and call it with the desired parameter, such as:

```python
>>> from Problem_NUMBER.solution import solution as solution
>>> solution(parameters)
```

To run the tests included run in a bash terminal:

```bash
python3 ./Problem_NUMBER/test_solution.py
```

## 📄 License

This project is shared under the **GNU-GPL V3** license.
