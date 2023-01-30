# Import required libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the data
data = pd.read_csv("data.csv")
# Add your CSV file

# Split the data into training and testing sets
train_data, test_data, train_labels, test_labels = train_test_split(data.drop("target_column", axis=1), data["target_column"], test_size=0.2)

# Train the model
model = RandomForestClassifier()
model.fit(train_data, train_labels)

# Make predictions on the test data
predictions = model.predict(test_data)

# Evaluate the model's accuracy
accuracy = accuracy_score(test_labels, predictions)
print("Accuracy:", accuracy)
