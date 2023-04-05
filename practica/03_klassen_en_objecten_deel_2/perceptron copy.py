import numpy as np

# OPDDRACHT
# Voeg de ontbrekende code toe zodanig dat je met deze
# class Perceptron objecten kunt maken
# Zie test_perceptron.py voor testcases

# BONUS OPDRACHT
# Voeg de methode display toe om de perceptron te visualiseren
# kijk in perceptron.dot hoe je dat met de graphviz library
# kunt doen


class Perceptron:

    """
    Perceptron class to simulate a Neuron
    """

    # Constructor
    # 'dunder init'
    def __init__(self):
        self.weightVector = None
        self.bias = 0

    def initialize(self, nrOfFeatures):
        """Initialize w and b as zero"""

        # Create initial weight vector for each feature
        self.weightVector = np.zeros(nrOfFeatures)

        # Initialize bias
        self.bias = 0

    def train(self, X, y, epochs=10, learningRate=0.1):
        """
        Train the perceptron using the inputVector
        and target labels
        """
        # Initialize weights and bias
        nrOfFeatures = X.shape[1]
        self.initialize(nrOfFeatures)

        epochs = range(0, epochs)

        # for each epoch
        for epoch in epochs:
            
            # For each inputVector
            for inputVector, label in zip(X, y):
    
                # Predict output
                prediction = self.predict(inputVector)
               
                # Determine error
                error = label - prediction
                
                # update weight and b
                deltaWeight = learningRate*error*inputVector
                self.weightVector = self.weightVector + deltaWeight
                 
                deltaBias = learningRate*error
                self.bias = self.bias + deltaBias

                print()

    def predict(self, inputVector):
        """
        Determin outputvalue by multiplying
        inputvector with weightvector
        """
        activation = np.dot(inputVector, self.weightVector) + self.bias
        
        return 1 if activation > 0 else 0
