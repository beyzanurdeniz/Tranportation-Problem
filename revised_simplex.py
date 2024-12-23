import numpy as np

def find_entering_var_index(c_b, B, N, c_n):
    """
    Finds the index of the entering variable based on reduced costs.
    Since we are solving a minimization problem, we select the variable with the most positive reduced cost.
    Returns -1 if no entering variable is found.

    Args:
        c_b (numpy.ndarray): Cost coefficients of the basic variables.
        B (numpy.ndarray): Matrix of basic columns.
        N (numpy.ndarray): Matrix of non-basic columns.
        c_n (numpy.ndarray): Cost coefficients of the non-basic variables.

    Returns:
        int: Index of the entering variable.
    """
    B_inv = np.linalg.inv(B)
    reduced_costs = np.dot(c_b, np.dot(B_inv, N)) - c_n
    entering_var = np.argmax(reduced_costs)
    if reduced_costs[entering_var] <= 0:
        return -1 
    return entering_var

def find_leaving_var_index(A_i, B, b):
    """
    Finds the index of the leaving variable based on the minimum ratio test.
    Minimum ratio test is applied only if the lhs of the entering variable is positive, so ignored when it is negative or equals to 0.
    Returns -1 if no leaving variable is found (i.e., the problem is unbounded).

    Args:
        A_i (numpy.ndarray): Column of the entering variable.
        B (numpy.ndarray): Matrix of basic columns.
        b (numpy.ndarray): Right-hand side vector.

    Returns:
        int: Index of the leaving variable.
    """
    B_inv = np.linalg.inv(B)
    nominator = np.dot(B_inv, b)
    denominator = np.dot(B_inv, A_i)
    min_ratio = np.inf
    min_ratio_index = -1
    for i in range(len(denominator)):
        if denominator[i] > 0:
            ratio = nominator[i] / denominator[i]
            if ratio < min_ratio:
                min_ratio = ratio
                min_ratio_index = i
    return min_ratio_index

def revised_simplex(A, b, c):
    """
    This method solves a linear program using the revised simplex method.
    Runs until no entering variable is found or the problem is unbounded.
    This method assumes A, b, and c are given in the standard form, with slacks and surpluses or other necessary variables added.

    Args:
        A (numpy.ndarray): Constraint matrix.
        b (numpy.ndarray): Right-hand side vector.
        c (numpy.ndarray): Cost vector.

    Returns:
        tuple: A tuple containing the following elements:
            - numpy.ndarray: Optimal solution.
            - float: Optimal value.
            - str: Status of the solution ('Optimal' or 'Unbounded').
    """
    m, n = A.shape

    basis_indices = np.arange(n - m, n)
    non_basis_indices = np.arange(n - m)

    B = A[:, basis_indices]
    N = A[:, non_basis_indices]
    c_b = c[basis_indices]
    c_n = c[non_basis_indices]

    while True:
        entering_index = find_entering_var_index(c_b, B, N, c_n)
        if entering_index == -1:
            break 
        
        entering_var = non_basis_indices[entering_index]
        A_i = A[:, entering_var]
        
        leaving_index = find_leaving_var_index(A_i, B, b)
        if leaving_index == -1:
            return None, None, "Unbounded"
        
        leaving_var = basis_indices[leaving_index]

        basis_indices[leaving_index] = entering_var
        non_basis_indices[entering_index] = leaving_var

        B = A[:, basis_indices]
        N = A[:, non_basis_indices]
        c_b = c[basis_indices]
        c_n = c[non_basis_indices]

    B_inv = np.linalg.inv(B)
    x = np.zeros(n)
    x[basis_indices] = np.dot(B_inv, b)
    val = np.dot(c, x)

    return x, val, "Optimal"