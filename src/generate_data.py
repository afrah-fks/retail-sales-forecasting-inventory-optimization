import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Create date range (1 year)
dates = pd.date_range(start="2023-01-01", end="2023-12-31")

# Products list
products = ['Product_A', 'Product_B', 'Product_C']

data = []

for product in products:
    base_sales = np.random.randint(20, 50)  # base demand
    
    for i, date in enumerate(dates):
        # Trend (increasing over time)
        trend = i * 0.05
        
        # Seasonality (weekly pattern)
        seasonality = 10 if date.weekday() >= 5 else 0  # weekends boost
        
        # Random noise
        noise = np.random.normal(0, 5)
        
        sales = base_sales + trend + seasonality + noise
        
        data.append([
            date,
            product,
            max(0, int(sales))  # avoid negative sales
        ])

# Create DataFrame
df = pd.DataFrame(data, columns=["date", "product", "sales"])

# Save dataset
df.to_csv("data/raw/sales.csv", index=False)

print("Dataset generated successfully!")