import numpy as np
def cumulative_returns(returns: list) -> list:
    """
    Returns the compounded cumulative return after every period.
    """
    # Write code here
    
    result = []
    w=1
    for r in returns:
        w = w*(1+r)
        result.append(w-1)
    return result
    pass