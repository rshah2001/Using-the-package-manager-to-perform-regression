# Hospital Patient Data Analysis

This project analyzes the relationship between patients' blood pressure and age using Python and various external libraries for data manipulation, regression modeling, and visualization.

## Project Overview

This analysis includes:
1. Loading and exploring the patient dataset.
2. Visualizing the relationship between age and blood pressure.
3. Building a simple linear regression model to predict blood pressure based on age.
4. Displaying the regression line, coefficients, and predictions.

## Dataset

The dataset used for this analysis contains the following columns:
- **Age**: Patients' ages ranging from 25 to 100 years.
- **BloodPressure**: Blood pressure values ranging from 120 to 175 mmHg.

### Example Data:
| Age | BloodPressure |
|-----|---------------|
| 25  | 120           |
| 30  | 122           |
| ... | ...           |
| 100 | 175           |

## Libraries Used

The following Python libraries were utilized:
- **Pandas**: For data loading, cleaning, and basic exploration.
- **Matplotlib**: For creating scatter plots and visualizing the regression line.
- **Scikit-learn**: For building and evaluating the linear regression model.

## Summary Statistics

Key insights from the data:
- Average Age: 62.5 years
- Average Blood Pressure: 143.38 mmHg
- No missing values in the dataset.

## Features

### Scatter Plot
A scatter plot visualizes the relationship between age and blood pressure.

### Linear Regression
A simple linear regression model predicts blood pressure based on age:
- **Slope (coefficient)**: `Calculated slope value`
- **Intercept**: `Calculated intercept value`

The regression line is overlaid on the scatter plot.

### Predictions
The model predicts blood pressure for specific ages (e.g., 30, 40, 50, 60 years).

## Usage Instructions

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/rshah2001/Using-the-package-manager-to-perform-regression
   ```
2. Install the required Python libraries:
   ```bash
   pip install pandas matplotlib scikit-learn
   ```
3. Run the `hospital_analysis.py` script to perform the analysis:
   ```bash
   python hospital_analysis.py
   ```

## Example Output

- Scatter plot of age vs. blood pressure with the regression line.
- Regression coefficients (slope and intercept).
- Predicted blood pressure values for specific ages.
