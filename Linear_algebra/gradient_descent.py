import numpy as np
import matplotlib.pyplot as plt

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)  # Derivative of sigmoid (for backpropagation)

# Training data (X = inputs, y = expected outputs)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # 2 input neurons
y = np.array([[0], [1], [1], [0]])  # XOR output

# Initialize weights randomly
np.random.seed(42)
weights_input_hidden = np.random.randn(2, 2)  # 2 inputs → 2 hidden neurons
weights_hidden_output = np.random.randn(2, 1)  # 2 hidden neurons → 1 output

learning_rate = 0.5
epochs = 10000  # Training iterations

# Lists to store weight changes for visualization
weight_history_input_hidden = []
weight_history_hidden_output = []

# Training process
for epoch in range(epochs):
    # *Forward Propagation*
    hidden_layer_input = np.dot(X, weights_input_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)
    
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
    predicted_output = sigmoid(output_layer_input)

    # *Calculate Error*
    error = y - predicted_output  

    # *Backward Propagation*
    d_predicted_output = error * sigmoid_derivative(predicted_output)  # Gradient at output layer
    d_hidden_layer = d_predicted_output.dot(weights_hidden_output.T) * sigmoid_derivative(hidden_layer_output)  # Gradient at hidden layer

    # *Update Weights*
    weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate

    # Store weight changes
    weight_history_input_hidden.append(weights_input_hidden.copy())
    weight_history_hidden_output.append(weights_hidden_output.copy())

    # Print error every 1000 epochs
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}: Error = {np.mean(np.abs(error)):.4f}")

# *Final Predictions*
print("\nFinal Predictions:")
print(predicted_output)

# *Plot Weight Changes*
weight_history_input_hidden = np.array(weight_history_input_hidden)
weight_history_hidden_output = np.array(weight_history_hidden_output)

plt.figure(figsize=(10, 5))

# Plot input-to-hidden weights
for i in range(2):  # Two input neurons
    for j in range(2):  # Two hidden neurons
        plt.plot(weight_history_input_hidden[:, i, j], label=f'Input {i+1} → Hidden {j+1}')

# Plot hidden-to-output weights
for i in range(2):  # Two hidden neurons
    plt.plot(weight_history_hidden_output[:, i, 0], linestyle='dashed', label=f'Hidden {i+1} → Output')

plt.xlabel("Epochs")
plt.ylabel("Weight Value")
plt.title("Weight Changes During Training")
plt.legend()
plt.show()