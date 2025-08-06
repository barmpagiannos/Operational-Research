
# 🧮 Operations Research Project

This repository contains two optimization models developed for the course **Operations Research** at the School of Electrical & Computer Engineering, Aristotle University of Thessaloniki (AUTH).

Both parts of the project involve real-world inspired problems modeled and solved using **Mixed Integer Linear Programming (MILP)** with the **Gurobi Optimizer** in Python.

---

## 📘 Part 1: Weekly Class Schedule Optimization

**Goal:**  
Design an optimal weekly class schedule for two school classes, satisfying a variety of constraints regarding availability of teachers, subject time requirements, and scheduling rules.

### 🏫 Problem Description:
Each class must attend a fixed number of 2-hour lessons for each subject. The schedule runs from Monday to Friday, with four available time slots per day:
- Z1: 08:00–10:00
- Z2: 10:15–12:15
- Z3: 14:00–16:00
- Z4: 16:15–18:15

### 👩‍🏫 Constraints:
- Each teacher teaches a specific number of lessons per week, per class
- No teacher can teach more than one class per time slot
- No class has more than one subject per slot
- Physical Education can only be scheduled on **Thursday afternoons**
- Monday's first slot is **reserved**
- Certain teachers are **unavailable** on specific days/times
- Each class can have **at most one lesson per subject per day**

### ⚙️ Implementation:
- Model variables represent whether a teacher teaches a subject to a class on a specific day/slot
- All constraints are enforced via `model.addConstr(...)`
- Objective: **Feasibility only** (`model.setObjective(0)`)

### ✅ Output:
Upon successful optimization, the model prints the weekly schedule per class, formatted by day and time slot.

---

## 📘 Part 2: Facility Location Optimization

**Goal:**  
Determine which warehouses to operate (among 12 options) in order to satisfy demand at 12 sales centers at **minimum total cost** (installation + transportation).

### 🏢 Problem Overview:
Each warehouse:
- Has a fixed installation cost and limited capacity
- Can ship to any sales center with a known cost (or ∞ if infeasible)

Each sales center:
- Has a fixed demand
- Can be served by multiple warehouses

### 📦 Constraints:
- All sales center demands must be met exactly
- Warehouses cannot exceed their capacity
- Shipments are only allowed from open warehouses

### 💡 Modeling:
- Binary decision variable `y[i]`: whether warehouse `i` is open
- Continuous variable `x[i, j]`: amount shipped from warehouse `i` to center `j`
- Objective function combines fixed installation cost and transportation cost (per ton)

### ✅ Output:
- List of warehouses to operate
- Shipment plan per warehouse-center pair (in tons)
- Total cost (in thousand euros)

---

## 🛠️ Dependencies

- Python 3.x
- [Gurobi Optimizer](https://www.gurobi.com/)
- `gurobipy` Python API

Install with:
```bash
pip install gurobipy
