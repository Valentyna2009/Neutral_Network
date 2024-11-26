import numpy as np
import time
import random

class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        # num of neurons in different layers
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
        
    def feed_forward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a) + b)
        return a
    
    # ФУНКИЯ ПОКАЗЫВАЕТ, ЕСТИ ЛИ ВООБЩЕ ТЕСТОВЫЕ ДАННЫЕ
    # training_data это данные для обучения
    # epochs сколько раз нейронная сеть проходит по всему набору данных
    # mini_batch_size маленькие группы данных для обучения
    # eta скорость обучения. чем она выше, тем быстрее она двигается к правильным ответам. если слишком быстро, она может их пропускать.
    # test_data данные для тестирования нейронки
    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data = None):
        if test_data: 
            # remember how many test-data elements we have
            n_test = len(test_data)
        # number of training data elements
        n = len(training_data)
        # the prozess of learing for specified number (заданное количество) of epochs
        for j in range(epochs):
            time1 = time.time()
            # create by random way the new tranings data to learn the machine
            random.shuffle(training_data)
            # данные разбиваються на пакеты нужного размера
            mini_batches = [
                training_data[k: k + mini_batch_size]
                for k in range(0, n, mini_batch_size)]
            # для каждого мини пакета вызывается функция "update_mini_batch", которая обновляет веса и параметры сети,
            # что бы она лучше подходила к данным.
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            time2 = time.time()
            # после каждой эпохи, если есть тестовые данные, выводит, насколько хорошо сеть прошла проверку.
            if test_data:
                print(f'Epoch {j}: {self.evaluate(test_data)} / {n_test}, took {time2 - time1}')
            else:
                print(f'Epoch {j} complete in {time2 - time1}.')

    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w - (eta / len(mini_batch)) * nw 
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b - (eta / len(mini_batch)) * nb 
                       for b, nb in zip(self.weights, nabla_b)]
        

def sigmoid(z):
    return 1.0/(1.0+ np.exp(-z))