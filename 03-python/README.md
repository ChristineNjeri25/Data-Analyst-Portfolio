# Python & R Projects

## 1. Hospital Fever Checker (Python Fundamentals)
- **Objective:** Write a Python script to iterate through patient temperatures and flag potential fevers for doctor alerts.
- **Skills Used:** Variables, Lists, `for` loops, `if/elif/else` conditional logic, and f-strings.
- **Key Finding:** The script successfully implemented tiered logic: normal (< 100.4F), fever (>= 100.4F), and critical emergency (>= 105.0F). Order of `if/elif` statements prevents the critical cases from being misclassified.


## 2. Sales Commission Analysis (Pandas & NumPy)
- **Objective:** Load a CSV dataset into a Pandas DataFrame, group sales by region, categorize salespeople into performance tiers, and calculate bonus commissions.
- **Skills Used:** Pandas (`read_csv`, `groupby`, `sum`), custom Python functions (`def`), `.apply()` method, and vectorized math.
- **Key Finding:** The North region generated the highest total commission ($5,600). The custom function categorized 2 Gold, 2 Silver, and 1 Bronze salesperson. Vectorized math calculated a 2% bonus for all salespeople instantly.


## 3. Sales Commission Visualization (Matplotlib & Seaborn)
- **Objective:** Generate a professional bar chart using Python code instead of a BI tool.
- **Skills Used:** `matplotlib.pyplot`, `seaborn.barplot`, and `plt.savefig()` to save the chart as a PNG for reporting.
- **Key Finding:** Eve generated the highest commission payout ($4,250), followed by Bob ($3,000). The visual output is saved as `commission_chart.png`.


## 4. Line Chart vs. Bar Chart (Visualization Logic)
- **Objective:** Demonstrate why line charts are inappropriate for categorical data.
- **Skills Used:** `sns.lineplot`, comparing visual outputs.
- **Key Finding:** Connecting categorical data (SalesPersons) with a line creates a misleading visual zig-zag. Line charts must be reserved for continuous data (like time series) to show trends, while bar charts are for comparison.

## 5. Automated Daily Report (Python Scripting & Task Scheduler)
- **Objective:** Automate the generation of a daily KPI summary report to eliminate manual Excel work.
- **Skills Used:** Python file handling (`open`, `write`), `datetime` module, and Windows Task Scheduler for automated execution.
- **Key Finding:** The script successfully calculates the total ($12,150) and average ($2,430) commission payouts and writes a timestamped report to a text file automatically.

## 6. Real-Time Weather API (Python & Requests)
- **Objective:** Connect to a live, external REST API to pull real-time data instead of relying on static CSVs.
- **Skills Used:** `requests` library, handling JSON responses, and parsing nested dictionaries.
- **Key Finding:** Successfully pulled the current temperature (25.7°C) and wind speed (7.2 km/h) for Nairobi's GPS coordinates using the Open-Meteo API.