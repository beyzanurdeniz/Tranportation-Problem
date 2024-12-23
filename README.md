# Transportation LP Problem Comparison

This repository compares two different approaches to solving the Transportation Linear Programming (LP) problem:

1. **PuLP Library**: A straightforward LP solver.
2. **Revised Simplex Algorithm with Big M Method**: A custom implementation of the revised simplex method adapted for the transportation problem.

The goal is to evaluate the efficiency of these two methods in terms of the time taken to solve the problem. A detailed analysis of the results is available in [assignment_report.pdf](assignment_report.pdf).

---

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Results](#results)
5. [File Descriptions](#file-descriptions)

---

## Introduction

The Transportation LP problem is a classic optimization problem where the objective is to minimize the cost of transporting goods from suppliers to consumers while meeting supply and demand constraints.

This project explores two approaches:

- **PuLP Library**: A high-level library for linear programming in Python.
- **Revised Simplex Algorithm**: A more customizable approach using the Big M method for handling constraints.

By comparing these methods, we aim to understand their performance trade-offs and applicability to various problem sizes.

---

## Installation

To set up the project, follow these steps:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## Results

The comparison highlights the following findings:

- **PuLP**:

  - Performs exceptionally well on small-scale problems due to its optimized implementation.
  - Offers a simple and reliable solution for standard LP problems.

- **Revised Simplex Algorithm**:
  - Becomes competitive for larger problem instances, showcasing its potential scalability.
  - Provides flexibility for customization, making it suitable for specialized scenarios.

For a more detailed analysis of the results, refer to [assignment_report.pdf](assignment_report.pdf).


## File Descriptions

- **[main.py](main.py)**:

  - Serves as the main script for the project.
  - Generates test cases for the transportation problem.
  - Runs both the PuLP solver and the revised simplex method.
  - Compares their performance in terms of time taken.
  - Prints results to the console and generates a comparison plot.

- **[generating_instance.py](generating_instance.py)**:

  - Contains functions to generate feasible instances of the transportation problem.
  - Ensures that the generated instances meet supply and demand constraints.

- **[transportation_solver.py](transportation_solver.py)**:

  - Implements the transportation problem solver using the PuLP library.
  - Handles the LP formulation and solves it using PuLP's built-in methods.

- **[revised_simplex.py](revised_simplex.py)**:

  - A generic implementation of the revised simplex algorithm.
  - Assumes a standard form input and is not specialized for the transportation problem.
  - Can be adapted for solving other LP problems.

- **[revised_simplex_for_transportation.py](revised_simplex_for_transportation.py)**:
  - Adapts the revised simplex algorithm specifically for the transportation problem.
  - Converts the transportation problem into a standard LP form.
  - Implements the Big M method to handle constraints.
  - Uses the generic revised simplex algorithm to solve the problem.
