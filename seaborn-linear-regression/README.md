# Seaborn and Linear Regression: Movie Budget vs. Revenue Analysis

## Project Overview

This project analyzes the relationship between film budgets and box office revenue. Using a dataset of movie budgets and financial performance, we investigate whether higher film budgets actually lead to higher box office returns. The analysis utilizes Python's data science stack, including Pandas, Matplotlib, Seaborn, and Scikit-learn.

## Dataset

The dataset (`cost_revenue_dirty.csv`) contains movie budget and financial performance data scraped from [the-numbers.com](https://www.the-numbers.com/movie/budgets) on **May 1st, 2018**.

Key columns include:
- `Rank`: Ranking of the movie by production cost.
- `Release_Date`: Date the movie was released.
- `Movie_Title`: Title of the movie.
- `USD_Production_Budget`: Estimated production budget in USD.
- `USD_Worldwide_Gross`: Worldwide gross revenue in USD.
- `USD_Domestic_Gross`: Domestic gross revenue (USA) in USD.

## Prerequisites

To run this analysis, you need the following Python libraries:

- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`

You can install them using pip:

```bash
pip install pandas matplotlib seaborn scikit-learn
```

## Key Analysis Questions

The notebook addresses several questions and challenges:
1.  **Data Cleaning**: Handling missing values, duplicates, and converting currency strings to numeric types.
2.  **Descriptive Statistics**: Calculating average budgets, revenues, and identifying extremes.
3.  **Zero Revenue Films**: Investigating films that grossed $0 domestically or worldwide.
4.  **Unreleased Films**: Filtering out films that hadn't been released at the time of data collection.
5.  **Financial Analysis**: Identifying films that lost money (production cost > worldwide gross).
6.  **Visualization**: Using Seaborn to create bubble charts to visualize the relationship between budget and revenue.
7.  **Linear Regression**: (Implied by the title) Fitting a linear regression model to quantify the relationship.

## Usage

1.  Clone the repository or download the project files.
2.  Ensure you have the `cost_revenue_dirty.csv` file in the same directory.
3.  Open the Jupyter Notebook `Seaborn_and_Linear_Regression_(start).ipynb`.
4.  Run the cells sequentially to perform the analysis.

## Credits

-   **Data Source**: [The Numbers](https://www.the-numbers.com/movie/budgets)
-   **Course**: Angela Yu's 100 Days of Code - Python Bootcamp
