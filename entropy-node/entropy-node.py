import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    y=np.asarray(y)
    if len(y) == 0:
        return 0.0
    __, counts = np.unique(y,return_counts = True)
    c = counts / len(y)
    return float(-np.sum(c * np.log2(c)))
    pass