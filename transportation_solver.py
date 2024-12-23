import pulp

def transportation_solver(supply, demand, cost):
    """
    This function formulates an LP for the transportation problem and solves it using the PULP library.

    Args:
        supply (list[int]): Supply values for each supply node.
        demand (list[int]): Demand values for each demand node.
        cost (list[list[int]]): Cost matrix with dimensions [num_supply x num_demand].

    Returns:
        tuple: A tuple containing the following elements:
            - list[list[int]]: Optimal transportation plan with dimensions [num_supply x num_demand].
            - int: Total cost of the optimal transportation plan.
    """

    transportationLP = pulp.LpProblem("transportation_problem", pulp.LpMinimize)
    cost_matrix = {(i, j): cost[i][j] for i in range(len(supply)) for j in range(len(demand))}
    possible_routes = [(i, j) for i in range(len(supply)) for j in range(len(demand))]
    decision_vars = pulp.LpVariable.dicts("route", possible_routes, lowBound=0, cat='Continuous')
    
    transportationLP += pulp.lpSum(decision_vars[route] * cost_matrix[route] for route in possible_routes), "Total Cost of Transportation"

    for i in range(len(supply)):
        transportationLP += pulp.lpSum(decision_vars[(i, j)] for j in range(len(demand))) == supply[i], f"Supply Constraint {i}"

    for j in range(len(demand)):
        transportationLP += pulp.lpSum(decision_vars[(i, j)] for i in range(len(supply))) == demand[j], f"Demand Constraint {j}"

    transportationLP.solve(pulp.PULP_CBC_CMD(msg=False))
    total_cost = pulp.value(transportationLP.objective)
    transportation_plan = [[pulp.value(decision_vars[(i, j)]) for j in range(len(demand))] for i in range(len(supply))]

    return transportation_plan, total_cost