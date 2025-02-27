import sympy as sp  # Importing sympy for symbolic computation

def optimize_function():
    # Define symbols
    x, y = sp.symbols('x y')

    # User inputs the objective function and constraint
    f_input = input("Enter the objective function (use 'x' and 'y'): ")
    constraint_input = input("Enter the constraint equation (in terms of x and y): ")

    # Convert input strings to sympy expressions
    f = sp.sympify(f_input)
    constraint_eq = sp.sympify(constraint_input)

    # Solve for x in terms of y using the constraint equation
    x_expr = sp.solve(constraint_eq, x)[0]

    # Substitute x in the function so that it depends only on y
    f_y = f.subs(x, x_expr)

    # Differentiate f with respect to y
    df_dy = sp.diff(f_y, y)

    # Solve df/dy = 0 to find the optimal y value
    y_optimal = sp.solve(df_dy, y)[0]

    # Compute the corresponding x value
    x_optimal = x_expr.subs(y, y_optimal)

    # Compute the minimum function value
    min_value = f.subs({x: x_optimal, y: y_optimal})

    # Display results
    print(f"\nOptimal x: {x_optimal}")
    print(f"Optimal y: {y_optimal}")
    print(f"Minimum Function Value: {min_value}")

# Run the function
optimize_function()
