# Google Trends and Data Visualization

A comprehensive data analysis project exploring the relationship between Google search trends and real-world metrics including stock prices, cryptocurrency values, and unemployment rates.

## 📊 Project Overview

This project analyzes Google Trends data to identify correlations between search popularity and various economic indicators. The analysis includes:

- **Tesla Stock Analysis**: Comparing Tesla web search trends with stock price movements
- **Bitcoin Analysis**: Examining the relationship between Bitcoin news searches and price fluctuations
- **Unemployment Analysis**: Investigating how searches for "Unemployment Benefits" correlate with actual unemployment rates

## 🎯 Learning Objectives

- Data cleaning and preprocessing with Pandas
- Time series data manipulation and resampling
- Data visualization using Matplotlib
- Correlation analysis between different datasets
- Working with datetime objects in Python

## 📁 Dataset Sources

The project uses data from multiple authoritative sources:

- [Unemployment Rate from FRED](https://fred.stlouisfed.org/series/UNRATE/)
- [Google Trends](https://trends.google.com/trends/explore)
- [Yahoo Finance - Tesla Stock Price](https://finance.yahoo.com/quote/TSLA/history?p=TSLA)
- [Yahoo Finance - Bitcoin Price](https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD)

## 📦 Files Included

- `Google Trends and Data Visualisation.ipynb` - Main Jupyter notebook with analysis
- `TESLA Search Trend vs Price.csv` - Tesla search trends and stock prices (monthly data)
- `Bitcoin Search Trend.csv` - Bitcoin news search trends (monthly data)
- `Daily Bitcoin Price.csv` - Daily Bitcoin closing prices and volume
- `UE Benefits Search vs UE Rate 2004-19.csv` - Unemployment benefits searches vs actual rates (2004-2019)
- `UE Benefits Search vs UE Rate 2004-20.csv` - Extended dataset through 2020

## 🔧 Technologies Used

- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **Jupyter Notebook** - Interactive development environment

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas matplotlib jupyter
```

### Running the Analysis

1. Clone or download this repository
2. Ensure all CSV files are in the same directory as the notebook
3. Open the Jupyter notebook:
   ```bash
   jupyter notebook "Google Trends and Data Visualisation.ipynb"
   ```
4. Run all cells to see the complete analysis

## 📈 Key Features

### Data Exploration
- Shape and structure analysis of datasets
- Statistical summaries using `.describe()`
- Data type conversions (strings to datetime objects)
- Handling missing values

### Data Cleaning
- Identifying and removing null values
- Converting date strings to datetime objects
- Resampling daily data to monthly frequency
- Handling different time series periodicities

### Data Visualization
- Dual-axis line charts comparing search trends with prices
- Time series plots with proper date formatting
- Custom styling and formatting for professional visualizations

## 🔍 Analysis Highlights

### Tesla Analysis
- Monthly search trends from 2010-2020
- Comparison with stock closing prices
- Search popularity ranges from 2 to 31 (Google Trends scale)

### Bitcoin Analysis
- Monthly news search trends from 2014-2020
- Daily price data resampled to monthly
- Search popularity peaks at 100 during major price movements

### Unemployment Analysis
- Monthly data from 2004-2020
- Correlation between benefit searches and actual unemployment rates
- Search popularity peaks at 100 during economic crises

## 📊 Sample Insights

The analysis reveals interesting patterns such as:
- Search interest often precedes or coincides with major price movements
- Economic uncertainty drives increased search activity
- Public interest correlates with market volatility

## 🎓 Skills Demonstrated

- **Data Wrangling**: Cleaning, transforming, and preparing data for analysis
- **Time Series Analysis**: Working with temporal data and resampling techniques
- **Data Visualization**: Creating clear, informative charts
- **Statistical Analysis**: Understanding correlations and trends
- **Python Programming**: Efficient use of Pandas and Matplotlib libraries

## 📝 Notes

- Google Trends values are normalized on a scale of 0-100, where 100 represents peak popularity
- The data periodicity varies (monthly for trends, daily for Bitcoin prices)
- Missing values in the Bitcoin price dataset were identified and removed

## 🤝 Contributing

This is a learning project from the Angela Yu 100 Days of Code Python course. Feel free to fork and experiment with the code!

## 📄 License

This project is part of educational coursework and is available for learning purposes.

## 🙏 Acknowledgments

- Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp
- Data providers: FRED, Google Trends, Yahoo Finance
