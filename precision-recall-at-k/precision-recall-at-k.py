def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    top_k_rec = recommended[:k]

    precision = len(list(set(top_k_rec) & set(relevant))) / k
    recall = len(list(set(top_k_rec) & set(relevant))) / len(relevant)
    return [precision,recall]
    pass