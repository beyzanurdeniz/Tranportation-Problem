import numpy as np

def prepare_transportation_for_simplex(supply, demand, cost):
    """
    This function takes supply, demand, and cost values and prepares them for the revised simplex.

    Args:
        supply (list[int]): Supply values for each supply node.
        demand (list[int]): Demand values for each demand node.
        cost (list[list[int]]): Cost matrix with dimensions [num_supply x num_demand].

    Returns:
        tuple: A tuple containing the following elements:
            - numpy.ndarray: Constraint matrix.
            - numpy.ndarray: Right-hand side vector.
            - numpy.ndarray: Cost vector.
    """

    num_supply = len(supply)
    num_demand = len(demand)

    A = np.zeros((num_supply + num_demand, num_supply * num_demand))
    b = np.zeros(num_supply + num_demand)
    c = np.zeros(num_supply * num_demand)

    for i in range(num_supply):
        for j in range(num_demand):
            A[i, i * num_demand + j] = 1
            A[num_supply + j, i * num_demand + j] = 1
            c[i * num_demand + j] = cost[i][j]

    b[:num_supply] = supply
    b[num_supply:] = demand

    A, b, c = add_artificial_var(A, b, c)

    return A, b, c

def add_artificial_var(A, b, c):
    """
    This function takes A, b, and c and adds artificial variables to the matrix A and vector c, and returns it as a Big M problem.
    Since the max value we decided is 1000, we set the cost coefficient of the artificial variables to 1e6, that should be enough.

    """

    m, n = A.shape

    A_artificial = np.zeros((m, m))
    c_artificial = np.zeros(m)

    for i in range(m):
        A_artificial[i, i] = 1
        c_artificial[i] = 1e6

    A = np.hstack((A, A_artificial))
    c = np.hstack((c, c_artificial))

    return A, b, c
