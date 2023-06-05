import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

# Load the test data from a CSV file
test_data = pd.read_csv('/data/sber_may_2023.csv', delimiter=';', header=None)

# Preprocess the data
data = test_data.iloc[:, 1:6].values  # Select all candle values
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

# Split the data into input (X) and target (y) variables
X_test = []
y_test = []
n_steps = 10  # Number of time steps to consider for each prediction
for i in range(n_steps, len(scaled_data)):
    X_test.append(scaled_data[i-n_steps:i, :])
    y_test.append(scaled_data[i, :])
X_test, y_test = np.array(X_test), np.array(y_test)

# Load the trained model
model = load_model('/models/sber_v1.h5')

# Perform predictions on the test data
y_pred = model.predict(X_test)

# Rescale the predicted values back to their original scale
y_pred = scaler.inverse_transform(y_pred)

# Calculate the percentage change for each predicted value
y_test_orig = scaler.inverse_transform(y_test)
percent_change = ((y_pred - y_test_orig) / y_test_orig) * 100

# Print the predicted values and compare with the actual values
for i in range(len(y_pred)):
    print('Predicted:', y_pred[i])
    print('Actual:', y_test[i])
    print('Percentage Change:', percent_change[i])
    print('---------------------')
