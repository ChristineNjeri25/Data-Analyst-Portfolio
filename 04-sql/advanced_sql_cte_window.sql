-- Advanced SQL: CTEs and Window Functions
USE FinanceMIS;
GO

WITH SalesData AS (
    SELECT 
        Department AS Region, 
        AccountName AS SalesPerson, 
        Amount AS Total_Sales
    FROM dbo.GL_Transactions
    WHERE TransactionType = 'Debit'
)

SELECT 
    Region, 
    SalesPerson, 
    Total_Sales,
    RANK() OVER (PARTITION BY Region ORDER BY Total_Sales DESC) AS Rank_In_Region
FROM SalesData;