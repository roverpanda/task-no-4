# task4_optimization_factory.py

import pulp

# Define LP problem
model = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Decision Variables
A = pulp.LpVariable("Product_A", lowBound=0, cat='Integer')
B = pulp.LpVariable("Product_B", lowBound=0, cat='Integer')

# Objective Function
model += 20 * A + 30 * B, "Total_Profit"

# Constraints
model += 3 * A + 4 * B <= 240, "Machine_Hours"
model += 2 * A + 1 * B <= 100, "Labor_Hou_
