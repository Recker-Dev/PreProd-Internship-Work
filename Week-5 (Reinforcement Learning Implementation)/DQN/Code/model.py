## Seperate model file, to partiularly study the model architecture.

from torch import nn
from torch.nn import functional


class Model(nn.Module):
    """
    Defines a fully connected neural network model for Q-learning with three layers.

    Args:
    - input_features (int): Number of input features (state dimension).
    - output_values (int): Number of output values (action space size).
    """
    def __init__(self, input_features, output_values):
        super(Model, self).__init__()  # Initialize the parent class (nn.Module)

        # First fully connected layer (input layer to hidden layer)
        self.fc1 = nn.Linear(in_features=input_features, out_features=32)

        # Second fully connected layer (hidden layer to another hidden layer)
        self.fc2 = nn.Linear(in_features=32, out_features=32)

        # Third fully connected layer (hidden layer to output layer)
        self.fc3 = nn.Linear(in_features=32, out_features=output_values)

    def forward(self, x):
        """
        Defines the forward pass of the neural network. Applies SELU activation
        on the first two layers, and returns the output from the last layer.

        Args:
        - x (tensor): The input tensor (state).

        Returns:
        - tensor: Output Q-values (predicted action values).
        """
        x = functional.selu(self.fc1(x))  # Apply SELU activation to first layer
        x = functional.selu(self.fc2(x))  # Apply SELU activation to second layer
        x = self.fc3(x)  # No activation after the last layer (output layer)
        return x
