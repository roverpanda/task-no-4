# task-no-4
# Task 4: Business Optimization – Factory Profit Maximization

## 📌 Problem
A factory must decide how many units of Product A and B to produce, using limited machine and labor hours, to **maximize profit**.

## 📊 Data
| Resource       | Product A | Product B | Limit |
|----------------|-----------|-----------|-------|
| Machine Hours  | 3         | 4         | 240   |
| Labor Hours    | 2         | 1         | 100   |
| Profit         | ₹20/unit  | ₹30/unit  |       |

## 🧮 Model
- **Variables**: Units of A and B
- **Constraints**: Machine and labor limits
- **Objective**: Maximize ₹20A + ₹30B

## 🛠 Tools
- Python
- PuLP

## ✅ Output
- 20 units of Product A
- 30 units of Product B
- **Profit = ₹1300**

## 🔧 To Run
```bash
pip install pulp
python task4_optimization_factory.py
