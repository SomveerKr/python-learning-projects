# 📊 College Majors & Salary Analysis

A data analysis project exploring the relationship between college majors and salary outcomes using **Pandas** in Python. Part of the [100 Days of Code – Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) (Day 72).

## 🎯 Objective

Analyze salary data across 50 undergraduate majors to answer key questions:

- Which majors have the **highest starting** and **mid-career salaries**?
- Which majors have the **lowest earning potential**?
- Which majors carry the **most/least risk** (salary spread)?
- How do salary outcomes differ across **STEM**, **Business**, and **HASS** groups?

## 📁 Project Structure

```
college-majors-salary/
├── salaries_by_college_major.csv   # Dataset (source: PayScale Inc.)
├── salaries_by_college_major.ipynb # Jupyter Notebook with analysis
└── README.md
```

## 📋 Dataset

The CSV contains **51 rows** (50 majors + source attribution) and **6 columns**:

| Column | Description |
|--------|-------------|
| `Undergraduate Major` | Name of the college major |
| `Starting Median Salary` | Median salary at career start |
| `Mid-Career Median Salary` | Median salary at mid-career |
| `Mid-Career 10th Percentile Salary` | 10th percentile mid-career salary |
| `Mid-Career 90th Percentile Salary` | 90th percentile mid-career salary |
| `Group` | Category — STEM, Business, or HASS |

> **Source:** PayScale Inc.

## 🔍 Key Analysis Steps

1. **Data Cleaning** — Dropped rows with `NaN` values (source attribution row)
2. **Highest/Lowest Earners** — Identified top and bottom majors by starting and mid-career salary
3. **Salary Spread** — Computed a `Spread` column (90th – 10th percentile) to quantify risk
4. **Sorting & Ranking** — Ranked majors by spread, mid-career salary, and 90th percentile potential
5. **Group Analysis** — Used `groupby` to compare average starting salaries across STEM, Business, and HASS

## 💡 Key Findings

| Insight | Major | Value |
|---------|-------|-------|
| Highest Starting Salary | Physician Assistant | $74,300 |
| Lowest Starting Salary | Spanish | $34,000 |
| Highest Mid-Career Salary | Chemical Engineering | $107,000 |
| Lowest Mid-Career Salary | Education | $52,000 |
| Highest 90th Percentile | Economics | $210,000 |
| Lowest Salary Spread (safest) | Nursing | $50,700 |
| Highest Salary Spread (riskiest) | Economics | $159,400 |

**Average Starting Salary by Group:**
- **STEM:** $53,863
- **Business:** $44,633
- **HASS:** $37,186

## 🛠️ Technologies Used

- **Python 3**
- **Pandas** — data manipulation and analysis
- **Google Colab** — notebook execution environment

## 🚀 Getting Started

1. Clone the repository
2. Open `salaries_by_college_major.ipynb` in Jupyter Notebook or Google Colab
3. Run all cells to reproduce the analysis

```bash
pip install pandas
```

## 📜 License

This project is for educational purposes as part of the 100 Days of Code Python Bootcamp.
