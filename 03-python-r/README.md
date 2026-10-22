# Python & R Projects

## 1. Hospital Fever Checker (Python Fundamentals)
- **Objective:** Write a Python script to iterate through patient temperatures and flag potential fevers for doctor alerts.
- **Skills Used:** Variables, Lists, `for` loops, `if/elif/else` conditional logic, and f-strings.
- **Key Finding:** The script successfully implemented tiered logic: normal (< 100.4F), fever (>= 100.4F), and critical emergency (>= 105.0F). Order of `if/elif` statements prevents the critical cases from being misclassified.


## 2. Sales Commission Analysis (Pandas & NumPy)
- **Objective:** Load a CSV dataset into a Pandas DataFrame, group sales by region, categorize salespeople into performance tiers, and calculate bonus commissions.
- **Skills Used:** Pandas (`read_csv`, `groupby`, `sum`), custom Python functions (`def`), `.apply()` method, and vectorized math.
- **Key Finding:** The North region generated the highest total commission ($5,600). The custom function categorized 2 Gold, 2 Silver, and 1 Bronze salesperson. Vectorized math calculated a 2% bonus for all salespeople instantly.