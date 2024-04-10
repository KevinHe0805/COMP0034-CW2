import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
import pickle

# Load the data
data = pd.read_csv('oil_and_gas_file.csv')

# Extract year, month, and day from the date column
data['year'] = pd.to_datetime(data['date']).dt.year
data['month'] = pd.to_datetime(data['date']).dt.month
data['day'] = pd.to_datetime(data['date']).dt.day
print(data.isnull().sum())
data.fillna(data.mean(), inplace=True)

# Encode the type column
le = LabelEncoder()
data['type_encoded'] = le.fit_transform(data['type'])

# Split the data into training and testing sets
X = data[['year', 'month', 'day', 'type_encoded']]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a decision tree regression model
dtr = DecisionTreeRegressor()
dtr.fit(X_train, y_train)

# Evaluate the model on the testing data
y_pred = dtr.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean squared error: {mse:.2f}")

# Save the trained model using pickle
with open('ml_model.pkl', 'wb') as f:
    pickle.dump(dtr, f)
