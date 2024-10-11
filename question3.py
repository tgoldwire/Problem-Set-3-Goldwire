import csv

# Initialize variables
previous_water_level = None
fastest_rise = float('-inf')
fastest_rise_date_time = ''
fastest_rise_change = 0

# Open and read the CSV file
with open('/Users/tavisgoldwire/Desktop/CO-OPS__8729108__wl.csv', 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
         # Loop through each row in the CSV file
        try:
            water_level = float(row[1])  
            # Read the water level from column 2 (index 1)
        except ValueError:
            # If the value is not a valid float, skip
            continue
        
        # If there is a previous water level, calculate the rise
        if previous_water_level != None:
            rise = water_level - previous_water_level
            
            # Check if this rise is the fastest (largest) rise so far
            if rise > fastest_rise:
                fastest_rise = rise
                fastest_rise_date_time = row[0]  # Date/time is in column 1 (index 0)
                fastest_rise_change = rise  # Track the change in water level
        
        # Update the previous water level to the current one for the next iteration
        previous_water_level = water_level

# After the loop, print the fastest rise and corresponding date/time
print(f"The fastest rise in water level was {fastest_rise_change:.2f} observed on {fastest_rise_date_time}.")
