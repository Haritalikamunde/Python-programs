import numpy as np

def Marvellous_FC(flat_data):

    # Dynamic weights
    weights = np.ones(len(flat_data), dtype=float)
    bias = -1.0

    print("\nFlatten Input:")
    print(flat_data)

    print("\nWeights:")
    print(weights)

    print("\nBias:")
    print(bias)

    multiplication = flat_data * weights
    result = np.sum(multiplication) + bias

    print("\nInput × Weights:")
    print(multiplication)

    print("\nDetailed FC Calculation:")
    terms = [f"({flat_data[i]:.1f}×{weights[i]:.1f})" for i in range(len(flat_data))]
    print(" + ".join(terms) + f" + ({bias})")

    print("\nSum of weighted inputs =", np.sum(multiplication))
    print("Final Output after adding bias =", result)

    # Prediction
    if result > 0:
        prediction = "Vertical Line"
    else:
        prediction = "Horizontal Line"

    return result

matrix=[[6, 4],
        [8, 6]]

matrix=np.array(matrix)
flatten_matrix=matrix.flatten()
print(flatten_matrix)


FCC=Marvellous_FC(flatten_matrix)
print(FCC)