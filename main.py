import numpy as np
import time
import matplotlib.pyplot as plt

from generating_instance import generate_transportation_feasible_instance
from transportation_solver import transportation_solver
from revised_simplex_for_transportation import prepare_transportation_for_simplex
from revised_simplex import revised_simplex

np.random.seed(73)

cases = [
    (3, 7),
    (7, 15),    
    (15, 25),
    (25, 50),
    (50, 75),    
    (75, 100),   
    (100, 150),
    (150, 200),
    (200, 250)
]

results = {
    "case_sizes": [],
    "pulp_times": [],
    "pulp_costs": [],
    "simplex_times": [],
    "simplex_costs": []
}

"""
This loop generates random instances of the transportation problem and compares the computation time and cost of the PULP solver and the revised simplex method.
Displays a plot comparing the computation time of both methods for different problem sizes.
Prints to terminal the results of both methods for each problem instance.
Also for integral observation, prints the transportation plan if the problem size is less than or equal to 15x15.
Also again for integer observation, 5 more cases were created.
"""

for idx, (min_size, max_size) in enumerate(cases):
    print(f"\n--- Case {idx + 1} ---")
    num_supply = np.random.randint(min_size, max_size)
    num_demand = np.random.randint(min_size, max_size)
    print(f"Problem Size: {num_supply}x{num_demand}")
    
    supply, demand, cost = generate_transportation_feasible_instance(num_supply, num_demand, 1000, 1000)
    A, b, c = prepare_transportation_for_simplex(supply, demand, cost)
    
    start = time.time()
    transportation_plan, total_cost_pulp = transportation_solver(supply, demand, cost)
    end = time.time()
    pulp_time = end - start
    results["pulp_times"].append(pulp_time)
    results["pulp_costs"].append(total_cost_pulp)
    print(f"PULP Solver Results: Time = {pulp_time:.4f}s, Cost = {total_cost_pulp}")
    if(num_supply <= 15 and num_demand <= 15):
        print("Transportation Plan:")
        for row in transportation_plan:
            print(row)

    start = time.time()
    result, _, status = revised_simplex(A, b, c)
    end = time.time()
    simplex_time = end - start
    simplex_cost = np.dot(c, result)
    results["simplex_times"].append(simplex_time)
    results["simplex_costs"].append(simplex_cost)
    print(f"Revised Simplex Results: Time = {simplex_time:.4f}s, Cost = {simplex_cost}")
    if(num_supply <= 15 and num_demand <= 15):
        print("Transportation Plan:")
        for i in range(num_supply):
            row = result[i * num_demand: (i + 1) * num_demand]
            print(row)
    results["case_sizes"].append((num_supply, num_demand))

case_labels = [f"{supply}x{demand}" for supply, demand in results["case_sizes"]]

plt.figure(figsize=(12, 8))
plt.plot(case_labels, results["pulp_times"], label="PULP Solver")
plt.plot(case_labels, results["simplex_times"], label="Revised Simplex")
plt.xlabel("Case Size (Supply x Demand)")
plt.ylabel("Computation Time (s)")
plt.title("Computation Time vs Case Size")
plt.xticks(rotation=45)
plt.legend()
plt.show()

for i in range(5):

    num_supply = np.random.randint(3, 10)
    num_demand = np.random.randint(3, 10)
    print(f"Problem Size: {num_supply}x{num_demand}")
    supply, demand, cost = generate_transportation_feasible_instance(num_supply, num_demand, 10, 10)

    A, b, c = prepare_transportation_for_simplex(supply, demand, cost)
    result, _, status = revised_simplex(A, b, c)

    simplex_cost = np.dot(c, result)

    print(f"\n--- Case {i + 1} ---")
    print(f"Cost = {simplex_cost}")
    if(num_supply <= 15 and num_demand <= 15):
        print("Transportation Plan:")
        for i in range(num_supply):
            row = result[i * num_demand: (i + 1) * num_demand]
            print(row)