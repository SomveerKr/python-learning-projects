# Programming Languages Popularity Analysis

A data visualization project analyzing the popularity trends of various programming languages on Stack Overflow from 2008 to 2020.

## 📊 Project Overview

This project analyzes Stack Overflow post data to visualize and understand the popularity trends of 14 major programming languages over time. The analysis reveals fascinating insights into how programming language usage has evolved in the developer community.

## 🎯 Features

- **Data Cleaning & Processing**: Handles raw Stack Overflow query results and transforms them into analyzable format
- **Time Series Analysis**: Tracks programming language popularity from 2008 to 2020
- **Data Visualization**: Creates comprehensive line plots showing trends for all languages
- **Statistical Analysis**: Identifies which languages have the highest total posts and longest tracking periods

## 📁 Project Structure

```
programming-languages-popularity/
│
├── Programming_Languages.ipynb    # Main Jupyter notebook with analysis
├── QueryResults.csv              # Raw data from Stack Overflow
└── README.md                     # Project documentation
```

## 📈 Languages Analyzed

The project tracks the following programming languages:
- **C/C++/C#**: Traditional systems and enterprise languages
- **Java**: Enterprise and Android development
- **JavaScript**: Web development
- **Python**: Data science, web, and general-purpose programming
- **PHP**: Web backend development
- **Ruby**: Web development (Rails)
- **R**: Statistical computing
- **Go**: Modern systems programming
- **Swift**: iOS development
- **Perl**: Text processing and scripting
- **Delphi**: Rapid application development
- **Assembly**: Low-level programming

## 🔍 Key Findings

- **Most Popular Language**: JavaScript has the highest total number of posts across all time periods
- **Fastest Growing**: Python shows remarkable growth, especially in recent years
- **Newest Entrant**: Go has the fewest months of data, being a newer language
- **Data Coverage**: Most languages have 144-145 months of data, spanning from 2008 to 2020

## 🛠️ Technologies Used

- **Python 3.7+**
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization
- **Jupyter Notebook**: Interactive development environment

## 📊 Data Source

The data comes from a Stack Overflow query that counts posts tagged with specific programming languages, grouped by month. The query can be run on [Stack Exchange Data Explorer](https://data.stackexchange.com/stackoverflow/query/675441/popular-programming-languages-per-over-time-eversql-com).

### SQL Query Used:
```sql
SELECT 
    DATEADD(month, DATEDIFF(month, 0, q.CreationDate), 0) m, 
    TagName, 
    COUNT(*)
FROM PostTags pt
JOIN Posts q ON q.Id=pt.PostId
JOIN Tags t ON t.Id=pt.TagId
WHERE TagName IN ('java','c','c++','python','c#','javascript','assembly','php','perl','ruby','visual basic','swift','r','object-c','scratch','go','swift','delphi')
AND q.CreationDate < DATEADD(month, DATEDIFF(month, 0, GETDATE()), 0)
GROUP BY DATEADD(month, DATEDIFF(month, 0, q.CreationDate), 0), TagName
ORDER BY DATEADD(month, DATEDIFF(month, 0, q.CreationDate), 0)
```

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas matplotlib jupyter
```

### Running the Analysis
1. Clone or download this repository
2. Navigate to the project directory
3. Launch Jupyter Notebook:
   ```bash
   jupyter notebook Programming_Languages.ipynb
   ```
4. Run all cells to see the analysis and visualizations

## 📝 Analysis Steps

1. **Data Import**: Load the CSV file containing Stack Overflow query results
2. **Data Exploration**: 
   - Examine data structure and dimensions (1,991 rows × 3 columns)
   - Check for missing values
   - Analyze data distribution
3. **Data Cleaning**:
   - Convert date strings to datetime objects
   - Handle missing values
   - Reshape data for visualization
4. **Data Transformation**:
   - Pivot data to create time series for each language
   - Fill missing values with zeros
5. **Visualization**:
   - Create comprehensive line plots showing all languages
   - Use distinct colors for each language
   - Add proper labels and legends

## 📊 Sample Insights

- **JavaScript** leads in total posts with consistent growth
- **Python** shows exponential growth, especially after 2015
- **Java** maintains steady popularity throughout the period
- **PHP** shows gradual decline in recent years
- **Swift** appears later (2014) due to its release date
- **Assembly** and **Perl** show declining trends

## 🎓 Learning Outcomes

This project demonstrates:
- Working with real-world time series data
- Data cleaning and preprocessing techniques
- Pandas DataFrame manipulation (pivoting, reshaping)
- Creating multi-line visualizations with Matplotlib
- Analyzing trends in technology adoption

## 📚 Part of 100 Days of Code

This project is Day 73 of the "100 Days of Code: The Complete Python Pro Bootcamp" by Angela Yu, focusing on data visualization and analysis using Pandas and Matplotlib.

## 🤝 Contributing

Feel free to fork this project and add your own analysis or visualizations!

## 📄 License

This project is part of a learning exercise and uses publicly available Stack Overflow data.

---

**Note**: The data represents Stack Overflow post counts and may not reflect the complete picture of programming language usage across all platforms and contexts.
