def differentiate(expression, variable):
    """Compute the derivative of a simple polynomial function with respect to a given variable."""
    terms = expression.split("+")  # Split terms by '+'
    derivative_terms = []

    for term in terms:
        term = term.strip()
        if variable in term:  # Check if the variable is in the term
            if "**" in term:  # Handling powers
                base, exponent = term.split("**")
                exponent = int(exponent)
                new_exponent = exponent - 1
                new_term = f"{exponent}*{base}**{new_exponent}" if new_exponent != 0 else f"{exponent}"
            elif "*" in term:  # Handling coefficients
                coeff, var = term.split("*")
                new_term = coeff if var == variable else term
            else:  # Variable without exponent
                new_term = "1"
            derivative_terms.append(new_term)

    return " + ".join(derivative_terms) if derivative_terms else "0"


def solve_for_x(equation):
    """Solve for x in terms of y given a simple linear equation."""
    equation = equation.replace(" ", "")
    left, right = equation.split("=")

    if "x" in right:  # Ensure 'x' is on the left side
        left, right = right, left

    # Isolate 'x'
    if "+" in left:
        parts = left.split("+")
        for part in parts:
            if "x" not in part:
                right = f"{right} - {part}"
        x_term = [p for p in parts if "x" in p][0]
    elif "-" in left:
        parts = left.split("-")
        x_term = parts[0]  # Assuming x is the first term
        right = f"{right} + {parts[1]}"

    coefficient, _ = x_term.split("*")
    x_value = f"({right}) / {coefficient}"

    return x_value


def evaluate(expression, values):
    """Substitutes values into the expression."""
    for var, val in values.items():
        expression = expression.replace(var, str(val))
    return eval(expression)


def optimize_function():
    # User inputs the objective function and constraint
    f_input = input("Enter the objective function (use 'x' and 'y'): ")
    constraint_input = input("Enter the constraint equation (in terms of x and y, e.g., '2*x + y = 5'): ")

    # Solve for x in terms of y
    x_expr = solve_for_x(constraint_input)

    # Substitute x in the function
    f_y = f_input.replace("x", f"({x_expr})")

    # Differentiate f_y with respect to y
    df_dy = differentiate(f_y, "y")

    # Solve df/dy = 0 (assuming it's a simple equation)
    y_optimal = eval(df_dy + " = 0")

    # Compute the corresponding x value
    x_optimal = eval(x_expr.replace("y", str(y_optimal)))

    # Compute the minimum function value
    min_value = evaluate(f_input, {"x": x_optimal, "y": y_optimal})

    # Display results
    print(f"\nOptimal x: {x_optimal}")
    print(f"Optimal y: {y_optimal}")
    print(f"Minimum Function Value: {min_value}")

# Run the function
optimize_function()
