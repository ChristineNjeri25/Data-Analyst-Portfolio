import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data
df = pd.read_csv(r"C:\Users\VERONICA NJERI\data-analyst-portfolio\01-excel\sales_commission_model.csv")

# 2. Set a beautiful theme
sns.set_theme(style="darkgrid")

# 3. Create a LINE Chart
plt.figure(figsize=(10, 6))
sns.lineplot(x='SalesPerson', y='Commission Payout', data=df)

# 4. Add a title and labels
plt.title('Line Chart Test: SalesPerson vs Commission', fontsize=16)
plt.xlabel('Salesperson', fontsize=12)
plt.ylabel('Commission Payout ($)', fontsize=12)

# 5. Show the chart
plt.show()