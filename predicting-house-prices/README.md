# Predicting House Prices with Multivariable Regression 🏠

## Project Description
This project focuses on building a multivariable regression model to estimate house prices in Boston using the famous Boston Housing dataset. The goal is to understand how various property characteristics—such as the number of rooms, crime rates, and distance to employment centers—affect property values.

The project takes you through the entire data science workflow:
1.  **Data Exploration & Cleaning**: Checking for missing values, duplicates, and understanding the dataset structure.
2.  **Exploratory Data Analysis (EDA)**: Visualizing distributions and relationships between variables using Seaborn and Plotly.
3.  **Model Building**: Implementing a Multivariable Linear Regression model using Scikit-Learn.
4.  **Model Evaluation**: Analyzing coefficients, calculating R-squared values, and inspecting residuals for potential bias.
5.  **Model Improvement**: Applying data transformations (Log Transformation) to the target variable to improve model performance and residual normality.

## Key Features
*   **Data Visualization**: Uses histograms, jointplots, and pairplots to visualize data distributions and correlations.
*   **Multivariable Regression**: Training a model with multiple features to predict a continuous target variable (Price).
*   **Model Assessment**: Evaluating model performance using R-squared and visual inspection of residuals (Actual vs. Predicted, Residuals vs. Predicted).
*   **Data Transformation**: Demonstrates how log-transforming skewed target data can lead to a better-fitting model.

## Technologies Used
*   **Python**
*   **Pandas** & **NumPy** (Data Manipulation)
*   **Seaborn** & **Matplotlib** (Static Visualization)
*   **Plotly** (Interactive Visualization)
*   **Scikit-Learn** (Machine Learning: Linear Regression, Train/Test Split)
*   **Jupyter Notebook**

## Getting Started
1.  Ensure you have the required libraries installed:
    ```bash
    pip install pandas numpy seaborn matplotlib plotly scikit-learn
    ```
2.  Open the notebook `Multivariable_Regression_and_Valuation_Model.ipynb` in Jupyter Notebook or Google Colab.
3.  Run the cells to execute the analysis and see the model predictions.

## Dataset
The dataset (`boston.csv`) is included in the project and contains 506 entries with 14 attributes, including:
*   `CRIM`: Per capita crime rate by town
*   `RM`: Average number of rooms per dwelling
*   `DIS`: Weighted distances to five Boston employment centres
*   `LSTAT`: Percentage of lower status of the population
*   `PRICE`: Median value of owner-occupied homes
