# LEGO Data Analysis

A comprehensive data analysis project exploring the history and evolution of LEGO sets using Python, Pandas, and Matplotlib. This project analyzes LEGO datasets from Rebrickable to uncover insights about LEGO's product offerings, themes, and growth over time.

## 📊 Project Overview

This project answers several interesting questions about LEGO's history:
- What is the most enormous LEGO set ever created?
- When were the first LEGO sets released?
- Which LEGO theme has the most sets?
- How has LEGO's product offering expanded over time?
- Have LEGO sets grown in size and complexity?

## 🗂️ Dataset

The project uses data from [Rebrickable](https://rebrickable.com/downloads/), which includes:
- **colors.csv**: Information about LEGO colors (135 unique colors)
- **sets.csv**: Details about LEGO sets from 1949 to 2021 (15,710 sets)
- **themes.csv**: LEGO themes and categories

## 🔍 Key Findings

### Historical Insights
- **First LEGO Sets**: Released in 1949 with 5 different sets
- **Largest Set**: "The Ultimate Battle for Chima" (BIGBOX-1) with 9,987 parts
- **Growth**: From 28 sets in 1955 to 840 sets in 2019

### Color Analysis
- 135 unique LEGO colors produced
- 107 opaque colors vs. 28 transparent colors

### Product Evolution
- Significant expansion in product offerings over the decades
- Dramatic increase in both the number of sets and themes released annually
- Modern sets tend to have more parts than earlier releases

## 🛠️ Technologies Used

- **Python 3.7+**
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization
- **Jupyter Notebook**: Interactive development environment

## 📁 Project Structure

```
lego-data-analysis/
│
├── Lego_Analysis.ipynb    # Main analysis notebook
├── data/
│   ├── colors.csv         # LEGO colors dataset
│   ├── sets.csv           # LEGO sets dataset
│   └── themes.csv         # LEGO themes dataset
├── assets/
│   ├── bricks.jpg
│   ├── lego_sets.png
│   ├── lego_themes.png
│   └── rebrickable_schema.png
└── README.md
```

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas matplotlib jupyter
```

### Running the Analysis

1. Clone the repository
2. Navigate to the project directory
3. Launch Jupyter Notebook:
   ```bash
   jupyter notebook Lego_Analysis.ipynb
   ```
4. Run all cells to see the complete analysis

## 📈 Visualizations

The project includes several visualizations:
- **Line chart**: LEGO sets published year-on-year
- **Line chart**: Number of themes released by year
- Both charts show the dramatic expansion of LEGO's product line over time

## 🔑 Key Analysis Techniques

- **Data Exploration**: Using `.head()`, `.tail()`, `.nunique()`, `.groupby()`
- **Aggregation**: Using `.agg()` with custom functions
- **Filtering**: Boolean indexing and conditional selection
- **Sorting**: Using `.sort_values()` for ranking analysis
- **Visualization**: Creating informative line charts with Matplotlib

## 📝 Sample Insights

```python
# Number of sets in first year vs. recent year
Sets in 1955: 28
Sets in 2019: 840
Difference: 812

# Top 5 largest LEGO sets by part count
1. The Ultimate Battle for Chima (9,987 parts)
2. UCS Millennium Falcon (7,541 parts)
3. Hogwarts Castle (6,020 parts)
4. Taj Mahal 2017 (5,923 parts)
5. Taj Mahal 2008 (5,922 parts)
```

## 🎯 Learning Objectives

This project demonstrates:
- Data cleaning and preparation
- Exploratory data analysis (EDA)
- Time series analysis
- Data aggregation and grouping
- Creating meaningful visualizations
- Drawing insights from data

## 📚 Data Source

Data compiled by [Rebrickable](https://rebrickable.com/downloads/) - a comprehensive database of LEGO pieces and sets.

## 🤝 Contributing

This is a learning project from Angela Yu's 100 Days of Code: Python course. Feel free to fork and experiment with your own analyses!

## 📄 License

This project is for educational purposes.

## 🙏 Acknowledgments

- Angela Yu's 100 Days of Code: Python course
- Rebrickable for providing comprehensive LEGO data
- The LEGO community for maintaining detailed records

---

**Note**: This analysis uses data up to late 2020, so 2020 and 2021 data may be incomplete in some visualizations.
