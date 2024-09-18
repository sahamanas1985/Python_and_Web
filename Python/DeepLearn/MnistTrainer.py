import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

(x_train, y_train),(x_test, y_test) = keras.datasets.mnist.load_data()

# Show a random sample image in plot along with it's training data label

#image = x_train[12]
#plt.imshow(image, cmap='Greys')
#plt.show()
#print(y_train[12])

# to increase accuracy, scale the image dataset by divinding each pixel value with 255
# so that each pixel value stays between 0 and 1. (Normalization)

x_train = x_train/255
x_test = x_test/255



# create a simple neural network without 1 hidden layer with 100 neurons.
# 784 input neurons, 10 output neurons.
# flatten the 2D array into 1D flat array (neuron input).

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(100, activation = 'relu'),  
    keras.layers.Dense(100, activation = 'relu'), 
    keras.layers.Dense(10, activation = 'sigmoid')
])

model.compile(
    optimizer='adam',
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
)

print('training started')
model.fit(x_train, y_train, epochs=10)
print('training complete')

#save model to disk
model.save('trainedmodel')

# test model with test dataset
evaluate_score = model.evaluate(x_test, y_test)
print(evaluate_score)

