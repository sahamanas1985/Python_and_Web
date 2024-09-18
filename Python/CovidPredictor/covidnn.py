import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
 
# Load your dataset
df = pd.read_excel('covid_trainer_data.xlsx')
 
# Preprocess the data
X = df[['Body_Temp', 'SPO2', 'Cough_Severity']].values
y = df['Result_description'].values

#print(X[1])
#print(y)
 
# Encode the labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

#print(y_encoded)
 
# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
 
# Scale the features

print (X_test)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print (X_test_scaled)


# Build the neural network model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(len(label_encoder.classes_), activation='softmax')
])
 
# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
 
# Train the model
model.fit(X_train_scaled, y_train, epochs=50)
 
# Evaluate the model
loss, accuracy = model.evaluate(X_test_scaled, y_test)
print(f'Test accuracy: {accuracy:.2f}')
 
# Function to make predictions on new data
def predict_condition(new_data):
    new_data_scaled = scaler.transform(new_data)
    predictions = model.predict(new_data_scaled)
    predicted_class = label_encoder.inverse_transform([tf.argmax(predictions, axis=-1).numpy()[0]])
    return predicted_class
 
# Example usage:
new_patient_data = [[97, 99, 0]]  # Replace with actual new data
print(predict_condition(new_patient_data))

