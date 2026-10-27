# SQL Projects
This folder contains my SQL/SSMS projects. 

## 1. Finance MIS Project (GL vs Budget Analysis)
- **Objective:** Analyze General Ledger spending against allocated budgets and calculate variances.
- **Skills Used:** Database creation, Data cleaning (UPDATE), Aggregations (GROUP BY), Conditional logic (CASE WHEN), and Joins (LEFT JOIN).
- **Key Finding:** Identified overspending in Marketing and Operations, and flagged unbudgeted spending in the Finance department.

## 2. Advanced SQL: CTEs and Window Functions
- **Objective:** Use a Common Table Expression (CTE) to create a temporary dataset, and use the `RANK()` window function to find the top spenders in each department.
- **Skills Used:** `WITH` (CTE), `RANK() OVER (PARTITION BY ... ORDER BY ...)`, and column aliasing.
- **Key Finding:** Successfully identified the highest expenditure in each department (e.g., Hardware Purchase in IT, Truck Repairs in Operations) without collapsing the data into a single aggregate row.
