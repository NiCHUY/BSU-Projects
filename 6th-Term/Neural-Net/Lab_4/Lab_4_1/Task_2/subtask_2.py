import numpy as np

def nonlin(x, deriv=False):
    if deriv:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

y = np.array([[0, 0, 1, 1]]).T
np.random.seed(1)

# Define the weights for each layer
syn0 = 2 * np.random.random((3, 4)) - 1  # First layer weights
syn1 = 2 * np.random.random((4, 4)) - 1  # Second layer weights
syn2 = 2 * np.random.random((4, 1)) - 1  # Output layer weights

for iter in range(1000000):
    # Forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    l3 = nonlin(np.dot(l2, syn2))

    # Backpropagation
    l3_error = y - l3
    l3_delta = l3_error * nonlin(l3, True)

    l2_error = l3_delta.dot(syn2.T)
    l2_delta = l2_error * nonlin(l2, True)

    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * nonlin(l1, True)

    # Update weights
    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print("Output After Training:")
print(l3)

print("Error After Training:")
print(l3_error)
