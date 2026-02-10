# Dr. Semmelweis Handwashing Discovery

## Project Overview
This project involves a data analysis of the historical records from the Vienna General Hospital in the 1840s, focusing on the work of Dr. Ignaz Semmelweis. Dr. Semmelweis is known as the "saviour of mothers" for discovering the lifesaving power of handwashing.

The analysis explores the tragicly high mortality rates from childbed fever (puerperal fever) in maternity wards and investigates the effect of handwashing on these rates. Through data manipulation and visualization, this project retraces the steps of Dr. Semmelweis's groundbreaking discovery.

## Data Sources
The project uses two CSV datasets:
- `annual_deaths_by_clinic.csv`: Contains annual data on the number of births and deaths in the two maternity clinics at the Vienna General Hospital.
- `monthly_deaths.csv`: Contains monthly data, allowing for a more granular analysis of the timeline, specifically focusing on the period before and after mandatory handwashing was instituted.

## Technologies Used
- **Python**: Core programming language.
- **Pandas**: For data extraction, cleaning, and manipulation.
- **NumPy**: For numerical operations.
- **Matplotlib & Seaborn**: For static data visualization.
- **Plotly**: For interactive visualizations.
- **SciPy**: For statistical analysis.

## Key Analysis Steps
1. **Data Loading & Cleaning**: Importing CSV data and handling dates/types.
2. **Exploratory Data Analysis**:
   - Calculating mortality rates.
   - Comparing Clinic 1 (staffed by medical students) vs. Clinic 2 (staffed by midwives).
3. **Visualizations**:
   - Plotting yearly and monthly trends in births and deaths.
   - Using twin-axis charts to compare births and deaths simultaneously.
   - Highlighting the dramatic drop in mortality after the introduction of handwashing.
4. **Statistical Testing**: (Implied by imports, likely t-tests to confirm significance).

## How to Run
1. Ensure you have Python installed along with the required libraries:
   ```bash
   pip install pandas numpy plotly seaborn matplotlib scipy
   ```
2. Clone or download this repository.
3. Open `Dr_Semmelweis_Handwashing_Discovery.ipynb` in Jupyter Notebook, JupyterLab, or VS Code.
4. Run the cells sequentially to see the analysis and charts.

## Usage
This project serves as an educational example of how data analysis can be used to solve real-world problems and the importance of data-driven decision making in medicine.
