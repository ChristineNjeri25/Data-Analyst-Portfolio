import pandas as pd

# 1. Load the data
df = pd.read_csv(r"C:\Users\VERONICA NJERI\data-analyst-portfolio\01-excel\sales_commission_model.csv")

# 2. Group by Region and sum the Commission Payout
region_totals = df.groupby('Region')['Commission Payout'].sum()

# 3. Print the result
print(region_totals)


# Create a function to categorize sales
def get_tier(sales):
    if sales >= 60000:
        return "Gold"
    elif sales >= 40000:
        return "Silver"
    else:
        return "Bronze"

# Apply the function to the 'Total Sales' column
df['Sales_Tier'] = df['Total Sales'].apply(get_tier)

# Print the SalesPerson, Total Sales, and the new Sales_Tier column
print(df[['SalesPerson', 'Total Sales', 'Sales_Tier']])