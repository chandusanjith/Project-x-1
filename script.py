import pandas as pd
import json

# Load the Excel file
df = pd.read_excel('your_file.xlsx')

# Assuming the JSON column is named 'json_data', iterate over each row
for index, row in df.iterrows():
    json_data = row['json_data']  # Assuming 'json_data' is the column name

    # Parse the JSON string
    try:
        json_obj = json.loads(json_data)
    except json.JSONDecodeError:
        print(f"Error parsing JSON in row {index}")
        continue

    # Fetch the desired key-value pairs
    key1 = json_obj.get('key1')  # Replace 'key1' with the actual key
    key2 = json_obj.get('key2')  # Replace 'key2' with the actual key

    # Do something with the key-value pairs
    print(f"Row {index}: key1={key1}, key2={key2}")
