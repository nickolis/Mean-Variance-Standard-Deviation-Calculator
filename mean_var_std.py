import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(lst).reshape(3, 3)

    def stats(func):
        return [
            func(arr, axis=0).tolist(),  # columns
            func(arr, axis=1).tolist(),  # rows
            func(arr).item(),            # flattened
        ]

    return {
        'mean': stats(np.mean),
        'variance': stats(np.var),
        'standard deviation': stats(np.std),
        'max': stats(np.max),
        'min': stats(np.min),
        'sum': stats(np.sum),
    }
