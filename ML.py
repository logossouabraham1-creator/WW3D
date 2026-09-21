# Simple machine learning project: linear regression
# Goal: learn a relationship between study hours and exam score

# Training data: hours studied -> score
X = [1, 2, 3, 4, 5]
Y = [30, 50, 70, 90, 110]

# Model parameters
weight = 0.0
bias = 0.0
learning_rate = 0.01
epochs = 1000

# Train the model using gradient descent
for _ in range(epochs):
    predictions = [weight * x + bias for x in X]
    errors = [pred - target for pred, target in zip(predictions, Y)]

    dW = sum(2 * error * x for error, x in zip(errors, X)) / len(X)
    dB = sum(2 * error for error in errors) / len(X)

    weight -= learning_rate * dW
    bias -= learning_rate * dB

# Make a prediction
hours = 1
predicted_score = weight * hours + bias

print(f"Learned model: score = {weight:.2f} * hours + {bias:.2f}")
print(f"If a student studies {hours} hours, predicted score is {predicted_score:.2f}")