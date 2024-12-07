import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample weather data (Date, Temperature in Celsius, Humidity in %, Rainfall in mm)
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100),
    'Temperature': [15 + i % 10 for i in range(100)],
    'Humidity': [50 + i % 5 for i in range(100)],
    'Rainfall': [5 if i % 7 == 0 else 0 for i in range(100)]
}

# Load data into DataFrame
weather_df = pd.DataFrame(data)
weather_df['Month'] = weather_df['Date'].dt.month

# Function to display average monthly temperature
def average_monthly_temperature():
    monthly_avg_temp = weather_df.groupby('Month')['Temperature'].mean()
    print("Average Monthly Temperature:")
    print(monthly_avg_temp)
    monthly_avg_temp.plot(kind='bar', color='skyblue')
    plt.title("Average Monthly Temperature")
    plt.xlabel("Month")
    plt.ylabel("Temperature (°C)")
    plt.show()

# Function to plot temperature trends over time
def temperature_trend():
    plt.figure(figsize=(10, 5))
    plt.plot(weather_df['Date'], weather_df['Temperature'], color='red', label='Temperature')
    plt.title("Temperature Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.show()

# Function to display rainfall days in a month
def monthly_rainfall_days():
    monthly_rain_days = weather_df[weather_df['Rainfall'] > 0].groupby('Month')['Rainfall'].count()
    print("Monthly Rain Days:")
    print(monthly_rain_days)
    sns.barplot(x=monthly_rain_days.index, y=monthly_rain_days.values, color='blue')
    plt.title("Monthly Rain Days")
    plt.xlabel("Month")
    plt.ylabel("Number of Rain Days")
    plt.show()

# Sample interactions
average_monthly_temperature()
temperature_trend()
monthly_rainfall_days()

