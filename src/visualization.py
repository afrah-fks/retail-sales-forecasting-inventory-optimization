import matplotlib.pyplot as plt
import os

def plot_sales(df, forecast):
    # Create images folder if not exists
    os.makedirs("images", exist_ok=True)

    plt.figure(figsize=(10,5))

    plt.plot(df['date'], df['sales'], label='Actual Sales')
    plt.plot(df['date'], forecast['forecast'], label='Forecasted Sales')

    plt.title("Retail Sales Forecast vs Actual Sales")
    plt.xlabel("Date")
    plt.ylabel("Sales")

    plt.legend()
    plt.grid(True)

    # ✅ SAVE IMAGE
    plt.savefig("images/forecast_plot.png")

    plt.show()