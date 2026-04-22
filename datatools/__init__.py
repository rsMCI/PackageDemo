import numpy as np

def describe(data):
    data = np.array(data)

    return {
        "mean": np.mean(data),
        "std": np.std(data),
        "min": np.min(data),
        "max": np.max(data)
    }

def normalize(data):
    data = np.array(data)
    return (data - np.mean(data)) / np.std(data)