import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
import random
training_data, validation_data, test_data = \
mnist.load_data_wrapper()

class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        # random float num from 2. num from sizes list to the last num
        self.biases = [np.random.randn(y,1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)  
                        for y, x in zip(sizes[1:], sizes[:-1])]
        
    #find a = vector of activation second layer 
    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a
    
    # mini stochastic gradient descent. learning the model
    # eta = time of working
    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data = None):
        if test_data:
            n_test = len(test_data)
        n = len(training_data) 
        
        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [training_data[k:k+mini_batch_size] for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            
            if test_data:
                print("Epoch {0}: {1} / {2}".format(
                    j, self.evaluate(test_data), n_test))
            else:
                print("Epoch {0} complete".format(j))

    def update_mini_batch()


# the sigmoid function 1 / 1 + e^-x. answer will be between 0 and 1. shows the activation of neurons. ob er aktiv oder nicht ist
def sigmoid(x):
    return 1/(1+np.exp(-x))

net = Network([2, 4, 1])

# print(net.weights[0])

print(net.biases[1])
#[4, 1]
#[2, 4]
# print(net.sizes[1:])

# [2,4]
# print(net.sizes[:-1])

x = np.linspace(-10, 10)   
p = sigmoid(x)
plt.xlabel("x") 
plt.ylabel("Sigmoid(x)")  
plt.plot(x, p) 
plt.show()