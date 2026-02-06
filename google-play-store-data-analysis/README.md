# Google Play Store App Analytics

This project analyzes the Android app market using a dataset of over 10,000 apps from the Google Play Store. The analysis explores various aspects such as app categories, ratings, size, installs, and pricing to gain insights into the mobile app ecosystem.

## Project Overview

The goal of this notebook is to perform a comprehensive analysis of the Google Play Store apps. The data was scraped from the Google Play Store in 2018.

**Key Analyses & Visualizations:**
*   **Data Cleaning:** Handling missing values (NaNs) and removing duplicate entries.
*   **Data Exploration:** Examining the structure of the dataset (rows, columns, data types).
*   **Content Rating Analysis:** Visualizing the distribution of content ratings (Everyone, Teen, Mature 17+, etc.) using interactive Pie and Donut charts with Plotly.
*   **Installs & Popularity:** Analyzing the number of installs to identify the most popular apps and converting installation numbers to numeric types for further analysis.
*   **Pricing & Revenue:** Investigating app prices, identifying the most expensive apps (filtering out "junk" apps), and estimating potential revenue.

## Technologies Used

*   **Python:** The core programming language.
*   **Pandas:** For data manipulation, cleaning, and analysis.
*   **Plotly Express:** For creating interactive and visually appealing charts (Pie, Donut).

## Dataset

The dataset (`apps.csv`) contains details of approximately 10,841 apps, including:
*   `App`: Application name
*   `Category`: Category the app belongs to
*   `Rating`: Overall user rating (as when scraped)
*   `Reviews`: Number of user reviews for the app
*   `Size_MBs`: Size of the app in MegaBytes
*   `Installs`: Number of user downloads/installs
*   `Type`: Paid or Free
*   `Price`: Price of the app
*   `Content_Rating`: Age group the app is targeted at - Children / Mature 21+ / Adult
*   `Genres`: An app can belong to multiple genres (apart from its main category)

## How to Run

1.  Ensure you have Python installed along with the required libraries:
    ```bash
    pip install pandas plotly
    ```
2.  Open the Jupyter Notebook:
    ```bash
    jupyter notebook "Google Play Store App Analytics.ipynb"
    ```
3.  Run the cells sequentially to reproduce the analysis and visualizations.

## Key Findings (Examples)

*   **Highest Rated Apps:** Identification of apps with 5.0 ratings.
*   **Largest Apps:** Finding apps with the largest file size.
*   **Most Reviewed:** Apps with the highest number of user reviews.

---
*This project is part of the 100 Days of Code - The Complete Python Pro Bootcamp.*
