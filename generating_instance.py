import numpy as np

def generate_transportation_feasible_instance(num_supply, num_demand, max_cost, max_demand_supply):
    """
    Generates a feasible instance of the transportation problem with integer values.

    This function creates a random cost matrix, supply values, and demand values for 
    a transportation problem instance. The total supply is adjusted to equal total demand 
    to ensure feasibility.

    Args:
        num_supply (int): Number of supply nodes.
        num_demand (int): Number of demand nodes.
        max_cost (int): Maximum possible transportation cost (c_ij).
        max_demand_supply (int): Maximum possible demand or supply of a node (a_i or b_j).

    Returns:
        tuple: A tuple containing the following elements:
            - list[int]: Supply values for each supply node.
            - list[int]: Demand values for each demand node.
            - list[list[int]]: Cost matrix with dimensions [num_supply x num_demand].
    """
    supply = [np.random.randint(1, max_demand_supply) for _ in range(num_supply)]
    demand = [np.random.randint(1, max_demand_supply) for _ in range(num_demand)]

    total_supply = sum(supply)
    total_demand = sum(demand)

    diff = total_supply - total_demand

    if diff > 0: # More supply than demand, remove supply until no diff remains
        i = np.random.randint(0, num_supply)
        while diff > 0:
            to_remove = min(supply[i]-1, diff)
            supply[i] -= to_remove
            diff -= to_remove
            i = np.random.randint(0, num_supply)

    elif diff < 0: # More demand than supply, remove demand until no diff remains
        i = np.random.randint(0, num_demand)
        while diff < 0:
            to_remove = min(demand[i]-1, -diff)
            demand[i] -= to_remove
            diff += to_remove
            i = np.random.randint(0, num_demand)

    cost = [[np.random.randint(0, max_cost) for _ in range(num_demand)] for _ in range(num_supply)] #cost[i][j] = cost of transporting from supply i to demand j

    return supply, demand, cost