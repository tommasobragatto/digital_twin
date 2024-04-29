import json

# Load the JSON data from the file
file_path = "received_5.json"  # Replace with the actual path to your JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract all "Pa" values from all lines
all_pa_values = []

for line in data["Lines"]:
    pa_values_line = line["Pa"]["Value"]
    all_pa_values.extend(pa_values_line)

# Calculate the sum of all "Pa" values
sum_of_all_pa_values = sum(all_pa_values)

# Print the result
print("Sum of all Pa values across all lines:", sum_of_all_pa_values)
