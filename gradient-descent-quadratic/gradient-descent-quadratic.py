def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Track current position 
    x = x0 

    for i in range(steps):
        # Calculate the gradient AT THE CURRENT x 
        gradient = 2 * a * x + b 
        #Update x 
        x = x - (gradient * lr)  
    return x
