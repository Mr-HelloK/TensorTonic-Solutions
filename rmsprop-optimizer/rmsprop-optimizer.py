import numpy as np

def rmsprop_step(
    w: list,
    g: list,
    s: list,
    lr: float = 0.001,
    beta: float = 0.9,
    eps: float = 1e-8,
) -> tuple[list, list]:
    """
    Returns (new_w, new_s) with the same shapes as the inputs.
    """
    # Write code here
    w = np.asarray(w)
    g = np.asarray(g)
    s =np.asarray(s)
    st = beta*s+(1-beta)*(g*g)
    wt = w - (lr/np.sqrt(st+eps))*g
    return np.round(wt,6).tolist(),np.round(st,6).tolist()
    pass