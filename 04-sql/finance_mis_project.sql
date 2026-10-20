--Finance MIS Project: GL vs Budget Analysis
-- Create the database
CREATE DATABASE FinanceMIS;
GO

-- Table 1: General Ledger (The actual money spent)
CREATE TABLE GL_Transactions (
    TransactionID INT PRIMARY KEY,
    TransactionDate DATE,
    Department VARCHAR(50),
    AccountCode VARCHAR(10),
    AccountName VARCHAR(100),
    Amount DECIMAL(10, 2),
    TransactionType VARCHAR(10) -- 'Debit' or 'Credit'
);

-- Table 2: Budget (What we planned to spend)
CREATE TABLE Budget (
    Department VARCHAR(50),
    AccountCode VARCHAR(10),
    BudgetAmount DECIMAL(10, 2)
);
GO

-- Insert Budget Data
INSERT INTO Budget (Department, AccountCode, BudgetAmount) VALUES
('IT', '5000', 50000.00),
('Marketing', '6000', 30000.00),
('HR', '7000', 20000.00),
('Operations', '8000', 100000.00);

-- Insert GL Transactions
INSERT INTO GL_Transactions (TransactionID, TransactionDate, Department, AccountCode, AccountName, Amount, TransactionType) VALUES
(1, '2023-10-01', 'IT', '5000', 'Software Subscriptions', 12000.00, 'Debit'),
(2, '2023-10-02', 'IT', '5000', 'Hardware Purchase', 15000.00, 'Debit'),
(3, '2023-10-05', 'Marketing', '6000', 'Facebook Ads', 10000.00, 'Debit'),
(4, '2023-10-06', 'marketing', '6000', 'Google Ads', 25000.00, 'Debit'), -- Notice the lowercase 'm'
(5, '2023-10-10', 'HR', '7000', 'Recruitment Agency', 5000.00, 'Debit'),
(6, '2023-10-12', 'Operations', '8000', 'Fuel', 45000.00, 'Debit'),
(7, '2023-10-15', 'Operations', '8000', 'Truck Repairs', 60000.00, 'Debit'),
(8, '2023-10-20', 'IT', '5000', 'Software Refund', 2000.00, 'Credit'), -- A credit reduces expense
(9, '2023-10-25', 'HR', '7000', 'HR Software', 10000.00, 'Debit'),
(10, '2023-10-28', 'Finance', '9000', 'Audit Fees', 15000.00, 'Debit'); -- Finance has no budget!

select 
	g.Department,
	sum(case when g.TransactionType = 'Debit'
		then g.Amount else -g.Amount end) as [Actual Spend],
	isnull(b.BudgetAmount, 0) as [Budget Amount],
	(isnull(b.BudgetAmount, 0) - sum(case when g.TransactionType = 'Debit'
		then g.Amount else -g.Amount end)) as [Variance]
from dbo.GL_Transactions g
left join dbo.Budget b 
	on g.Department = b.Department
group by g.Department, b.BudgetAmount
order by [Variance] asc;