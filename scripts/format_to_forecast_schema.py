import pandas as pd
import argparse
import os

def format_forecast_schema(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    # Drop rows with missing values
    df.dropna(subset=['date', 'store_nbr', 'item_nbr', 'unit_sales'], inplace=True)

    # Rename and format columns
    df['timestamp'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    df['item_id'] = df['store_nbr'].astype(str) + "_" + df['item_nbr'].astype(str)
    df['target_value'] = df['unit_sales'].clip(lower=0)  # Replace negative values with 0

    # Select required columns
    forecast_df = df[['item_id', 'timestamp', 'target_value']]

    # Save to output
    forecast_df.to_csv(output_csv, index=False)
    print(f"Saved formatted data to {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to raw train.csv")
    parser.add_argument("--output", default="formatted_forecast.csv", help="Output CSV path")
    args = parser.parse_args()

    format_forecast_schema(args.input, args.output)
