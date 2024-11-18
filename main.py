# Import necessary packages
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Dataset
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
    'BloodPressure': [120, 122, 126, 128, 130, 133, 135, 138, 142, 145, 150, 155, 160, 165, 170, 175]
}

# Step 1: Load dataset into pandas DataFrame and explore the data
df = pd.DataFrame(data)

# Check for missing values and display summary statistics
print("Summary Statistics:")
print(df.describe())
print("\nMissing values:\n", df.isnull().sum())

# Step 2: Create a scatter plot of Age vs Blood Pressure
plt.figure(figsize=(8, 6))
plt.scatter(df['Age'], df['BloodPressure'], color='blue', label='Data Points')
plt.xlabel('Age (years)')
plt.ylabel('Blood Pressure (mmHg)')
plt.title('Age vs Blood Pressure')
plt.grid(True)
plt.legend()
plt.show()

# Step 3: Build a simple linear regression model using scikit-learn
# Prepare data for the model
X = df[['Age']].values  # Feature variable (reshape into a 2D array)
y = df['BloodPressure'].values  # Target variable

# Create and train the regression model
model = LinearRegression()
model.fit(X, y)

# Step 4: Display the regression line on the scatter plot
# Generate predictions for the same Age values
y_pred = model.predict(X)

plt.figure(figsize=(8, 6))
plt.scatter(df['Age'], df['BloodPressure'], color='blue', label='Data Points')
plt.plot(df['Age'], y_pred, color='red', label='Regression Line')
plt.xlabel('Age (years)')
plt.ylabel('Blood Pressure (mmHg)')
plt.title('Age vs Blood Pressure with Regression Line')
plt.grid(True)
plt.legend()
plt.show()

# Step 5: Display regression coefficients
print(f"Regression Coefficients:")
print(f"Slope (Coefficient): {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")

# Step 6: Make predictions for example ages
example_ages = np.array([[30], [40], [50], [60]])  # Example ages as a 2D array
predicted_bp = model.predict(example_ages)

print("\nPredictions:")
for age, bp in zip(example_ages.flatten(), predicted_bp):
    print(f"Predicted Blood Pressure for age {age}: {bp:.2f} mmHg")
