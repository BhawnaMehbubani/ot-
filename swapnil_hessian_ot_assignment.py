import numpy as np

# Define the function
def function(x, y):
    return x**2 + y**2 + x*y

# Compute the Hessian matrix manually
def compute_hessian(x, y):
    # Second-order partial derivatives
    f_xx = 2  # ∂²f/∂x²
    f_yy = 2  # ∂²f/∂y²
    f_xy = 1  # ∂²f/∂x∂y
    f_yx = f_xy  # Hessian is symmetric

    # Construct Hessian matrix
    H = np.array([[f_xx, f_xy], [f_yx, f_yy]])
    return H

# Concavity classification
def classify_critical_point(H):
    # Compute determinant and eigenvalues
    determinant = np.linalg.det(H)
    eigenvalues = np.linalg.eigvals(H)

    print("\nHessian Matrix:\n", H)
    print("Determinant:", determinant)
    print("Eigenvalues:", eigenvalues)

    # Classification based on determinant and eigenvalues
    if determinant > 0:
        if np.all(eigenvalues > 0):
            print("Classification: Local Minimum (Convex Function)")
        elif np.all(eigenvalues < 0):
            print("Classification: Local Maximum (Concave Function)")
        else:
            print("Classification: Indefinite (Saddle Point)")
    elif determinant < 0:
        print("Classification: Saddle Point")
    elif determinant == 0:
        print("Classification: Inconclusive (Zero Determinant)")
    elif determinant >= 0:
        print("Classification: Possibly a Local Min/Max or Inconclusive")
    elif determinant <= 0:
        print("Classification: Possibly a Saddle Point or Inconclusive")

# Take user input
x_input = float(input("Enter x value: "))
y_input = float(input("Enter y value: "))

# Compute Hessian and classify concavity
Hessian_matrix = compute_hessian(x_input, y_input)
classify_critical_point(Hessian_matrix)
