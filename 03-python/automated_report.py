import pandas as pd
from datetime import datetime

# 1. Load the data
df = pd.read_csv(r"C:\Users\VERONICA NJERI\data-analyst-portfolio\01-excel\sales_commission_model.csv")

# 2. Calculate the KPIs
total_payout = df['Commission Payout'].sum()
average_payout = df['Commission Payout'].mean()
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 3. Create the report text
report = f"""
--- AUTOMATED DAILY REPORT ---
Generated on: {timestamp}

Total Commission Payout: ${total_payout:,.2f}
Average Commission Payout: ${average_payout:,.2f}
"""

# 4. Save it to a text file
with open("daily_report.txt", "w") as file:
    file.write(report)

print("Report generated successfully!")