import sys

try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError as e:
    print("Required packages not found. Please install pandas and matplotlib:")
    print("pip install pandas matplotlib")
    sys.exit(1)

def main(csv_file="simulated_sensor_data.csv"):
    try:
        df = pd.read_csv(csv_file)
    except Exception as e:
        print(f"Error reading CSV file '{csv_file}': {e}")
        sys.exit(1)

    if not all(col in df.columns for col in ["timestamp", "temperature", "humidity"]):
        print("CSV file must contain columns: timestamp, temperature, humidity")
        sys.exit(1)

    # Convert timestamp to seconds if it's in ms
    if df["timestamp"].max() > 1e10:
        df["timestamp"] = df["timestamp"] / 1000

    plt.figure(figsize=(10, 5))
    plt.plot(df["timestamp"], df["temperature"], label="Temperature (°C)", color="tab:red")
    plt.plot(df["timestamp"], df["humidity"], label="Humidity (%)", color="tab:blue")
    plt.xlabel("Timestamp")
    plt.ylabel("Value")
    plt.title("Sensor Data: Temperature and Humidity Over Time")
    plt.legend()
    plt.tight_layout()
    plt.grid(True)
    plt.savefig("sensor_data_plot.png")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Plot sensor data from CSV file.")
    parser.add_argument("--csv", type=str, default="simulated_sensor_data.csv", help="Path to CSV file")
    args = parser.parse_args()
    main(args.csv)
