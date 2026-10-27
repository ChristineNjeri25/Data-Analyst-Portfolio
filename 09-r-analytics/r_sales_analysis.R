# 1. Load the dplyr package
library(dplyr)

# 2. Load the CSV file into a dataframe called 'df'
df <- read.csv("C:/Users/VERONICA NJERI/data-analyst-portfolio/01-excel/sales_commission_model.csv")

# 3. The Pipe: Group by Region and sum the Commission Payout
region_totals <- df %>%
  group_by(Region) %>%
  summarise(Total_Commission = sum(Commission.Payout))

# 4. Print the result
print(region_totals)
