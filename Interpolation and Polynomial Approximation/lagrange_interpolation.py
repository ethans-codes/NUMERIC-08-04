from colors import bcolors


def lagrange_interpolation(x_data, y_data, x):
    """
    Lagrange Interpolation

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x (float): The x-value where you want to evaluate the interpolated polynomial.

    Returns:
    float: The interpolated y-value at the given x.
    """
    n = len(x_data)
    result = 0.0

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term

    return result

if __name__ == '__main__':
    x_data = [0.35, 0.4, 0.55, 0.65, 0.7]
    y_data = [-3.5991, -2.4416, -0.9375, 4.0256, 2.6711]
    x_a = 0.45
    x_b = 0.6
    y_a = lagrange_interpolation(x_data, y_data, x_a)
    y_b = lagrange_interpolation(x_data, y_data, x_b)
    print(bcolors.OKBLUE, "\nInterpolated value at xa =", x_a, "is ya =", y_a, bcolors.ENDC)
    print(bcolors.OKBLUE, "\nInterpolated value at xb =", x_b, "is yb =", y_b, bcolors.ENDC)


