# Nobel Prize Analysis

## Project Overview

This project analyzes the history of the Nobel Prize from 1901 to 2020. Using a dataset of all Nobel laureates, we explore patterns and trends in the awards, including the distribution of prizes across categories, the demographics of winners, and how the prize has evolved over time.

## Dataset

*   **Source**: The dataset `nobel_prize_data.csv` contains information on all Nobel Prize winners.
*   **Key Columns**:
    *   `year`: The year the prize was awarded.
    *   `category`: The field in which the prize was awarded (Physics, Chemistry, Medicine, Literature, Peace, Economics).
    *   `full_name`: The name of the laureate.
    *   `birth_country`: The country of birth of the laureate.
    *   `sex`: The gender of the laureate.
    *   `organization_name`: The organization associated with the laureate (if applicable).

## Key Questions Answered

The analysis addresses the following questions:
1.  **What is the most commonly awarded gender and birth country?**
2.  **What decade had the highest proportion of US-born winners?**
3.  **What decade and category pair had the highest proportion of female laureates?**
4.  **Who was the first woman to receive a Nobel Prize, and in what category?**
5.  **Which individuals or organizations have won more than one Nobel Prize?**
6.  **Are there more prizes awarded recently than when the prize was first created?**
7.  **In which fields are the most prizes awarded?**

## Technologies Used

*   **Python**: The primary programming language.
*   **Pandas**: For data manipulation and analysis.
*   **NumPy**: For numerical operations.
*   **Plotly**: For creating interactive visualizations.
*   **Seaborn**: For statistical data visualization.
*   **Matplotlib**: For creating static plots.

## Setup and Usage

1.  **Prerequisites**: Ensure you have Python installed along with the required libraries. You can install them using pip:
    ```bash
    pip install pandas numpy plotly seaborn matplotlib
    ```

2.  **Run the Analysis**: Open the Jupyter Notebook `Nobel_Prize_Analysis.ipynb` to view the code and visualizations.
    ```bash
    jupyter notebook Nobel_Prize_Analysis.ipynb
    ```

## Finding Highlights

*   **Gender Disparity**: The analysis highlights a significant gender gap, with far fewer female laureates compared to male laureates across most categories.
*   **US Dominance**: There is a noticeable trend of increasing US dominance in the scientific categories in the latter half of the 20th century.
*   **Repeat Winners**: The analysis identifies a select group of individuals and organizations (e.g., Marie Curie, the Red Cross) that have been honored multiple times.
