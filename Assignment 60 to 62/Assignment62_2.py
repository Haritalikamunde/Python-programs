import numpy as np

def ReLU(data):

    output = np.maximum(0, data)

    print("\nInput to ReLU:")
    print(data)

    print("\nRule : ReLU(x) = max(0, x)")
    print("\nOutput after ReLU:")
    print(output)

    return output

def Pooling(data):

    rows, cols = data.shape

    output_rows = rows // 2
    output_cols = cols // 2

    output = np.zeros((output_rows, output_cols))

    r = 0
    for i in range(0, rows, 2):
        c = 0
        for j in range(0, cols, 2):

            block = data[i:i+2, j:j+2]

            if block.shape != (2, 2):
                continue

            max_value = np.max(block)
            output[r][c] = max_value

            print(f"\nPooling Block position -> Row:{r} Column:{c}")
            print("\nSelected 2x2 Block:")
            print(block)

            print("\nMaximum value selected =", max_value)

            c += 1
        r += 1

    print("\nFinal Pooling Output:")
    print(output)

    return output

feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]

Relu_output=ReLU(feature_map)
Max_pooling=Pooling(Relu_output)