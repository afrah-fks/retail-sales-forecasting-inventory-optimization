import matplotlib.pyplot as plt

def plot_sales(df, forecast):
    plt.figure(figsize=(10,5))  # optional (better size)

    plt.plot(df['date'], df['sales'], label='Actual Sales')
    plt.plot(df['date'], forecast['forecast'], label='Forecasted Sales')

    plt.title("Retail Sales Forecast vs Actual Sales")  # ✅ TITLE
    plt.xlabel("Date")  # ✅ X-axis label
    plt.ylabel("Sales")  # ✅ Y-axis label

    plt.legend()
    plt.grid(True)

    plt.show()