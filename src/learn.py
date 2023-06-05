import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load the training data from a CSV file
train_data = pd.read_csv('/data/sber_jan_april_2023.csv', delimiter=';', header=None)

# Preprocess the data
data = train_data.iloc[:, 1:6].values  # Select all candle values
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

# Split the data into input (X) and target (y) variables
X_train = []
y_train = []
n_steps = 10  # Number of time steps to consider for each prediction
for i in range(n_steps, len(scaled_data)):
    X_train.append(scaled_data[i-n_steps:i, :])
    y_train.append(scaled_data[i, :])
X_train, y_train = np.array(X_train), np.array(y_train)

# Build the LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(n_steps, 5)))  # Adjust input shape
model.add(LSTM(50))
model.add(Dense(5))  # Adjust number of units to match the number of candle values
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)
# Save the trained model for future use
model.save('/models/sber_v1.h5')
