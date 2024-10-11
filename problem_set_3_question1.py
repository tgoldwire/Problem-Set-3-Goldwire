import csv
#import 
highest_water_level = 0
highest_water_date_time = 0
#initalizes variables

with open('/Users/tavisgoldwire/Desktop/CO-OPS__8729108__wl.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    for row in csv_reader:
        # Loop through each row (i) in the CSV file
        try:
            water_level = float(row[1])
             # Try to read the water level from column 2 (index 1)
        except ValueError:
            # If the value is not a valid float, skip this row
            continue
        
        # If water level is higher than the current highest, update the record
        if water_level > highest_water_level:
            highest_water_level = water_level
            highest_water_date_time = row[0]  

# After the loop, print the highest water level and corresponding date/time
print(f"The highest water level was {highest_water_level} observed on {highest_water_date_time}.")

