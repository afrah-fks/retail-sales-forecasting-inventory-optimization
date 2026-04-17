from src.data_preprocessing import load_data
from src.feature_engineering import create_features
from src.forecasting import train_model, predict_sales
from src.inventory import calculate_inventory
from src.visualization import plot_sales
import os

# Create output folder
os.makedirs("outputs", exist_ok=True)

print("Loading data...")
df = load_data("data/raw/sales.csv")

print("Creating features...")
df = create_features(df)

print("Training model...")
model = train_model(df)

print("Generating forecast...")
forecast_df = predict_sales(model, df)

print("Calculating inventory...")
inventory_df = calculate_inventory(forecast_df)

# Save outputs
forecast_df.to_csv("outputs/forecast.csv", index=False)
inventory_df.to_csv("outputs/inventory.csv", index=False)

print("Files saved in outputs/ folder")

# Show few rows
print("\nSample Inventory Data:")
print(inventory_df.head())

# Plot graph
plot_sales(df, forecast_df)