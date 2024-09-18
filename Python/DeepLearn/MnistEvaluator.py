from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
from numpy import array

(x_train, y_train),(x_test, y_test) = keras.datasets.mnist.load_data()

# to increase accuracy, scale the image dataset by divinding each pixel value with 255
# so that each pixel value stays between 0 and 1. (Normalization)
x_test = x_test/255

# load the model from disk
model = keras.models.load_model('trainedmodel')

# take a random image and predict the number.
randomimage = x_test[15]
plt.imshow(randomimage, cmap='Greys')
plt.show()

# convert 2D Array to 3D array as model was trained with 3D array.
testimage = array([x_test[15]])
print(testimage.shape)

#Predict and print
prediction = model.predict(testimage)

print(prediction)

indexOfMaxScore = np.argmax(prediction)
print('Prediction is : ' + str(indexOfMaxScore))
