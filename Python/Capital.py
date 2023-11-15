import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the stock data
dataset_path = input("Enter the path to the dataset file: ")
stock_data = pd.read_csv(dataset_path)

# Preprocess the data
print("Available columns:")
print(stock_data.columns)

features_input = input("Enter the features to use (comma-separated): ")
features = [feature.strip() for feature in features_input.split(',')]

target = input("Enter the target variable: ")

# Split the data into training and testing sets
train_data, test_data = train_test_split(stock_data, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(train_data[features], train_data[target])

# Make predictions on the test data
predictions = model.predict(test_data[features])

# Output the predictions and actual values
print('Predictions:', predictions)
print('Actual Values:', test_data[target].values)
