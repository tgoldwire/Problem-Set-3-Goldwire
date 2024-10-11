import csv

highest_water_level = float('-inf')
lowest_water_level = float('inf')
total_water_level = 0
count = 0
highest_water_date_time = ''
lowest_water_date_time = ''
#initalizes variables with blank values

# Open and read the CSV file
with open('/Users/tavisgoldwire/Desktop/CO-OPS__8729108__wl.csv', 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        # Loop through each row in the CSV file
        try:
            water_level = float(row[1])  # Read the water level from column 2 (index 1)
        except ValueError:
            # If the value is not a valid float, skip this row
            continue
        
        total_water_level += water_level
        count += 1  
        #sums water level and keeps track of counts to average later
        
        # Check for the highest water level
        if water_level > highest_water_level:
            highest_water_level = water_level
            highest_water_date_time = row[0]  # Date is in column 1 (index 0)
        
        # Check for the lowest water level
        if water_level < lowest_water_level:
            lowest_water_level = water_level
            lowest_water_date_time = row[0]  # Date is in column 1 (index 0)

# Calculate the average water level after all values are read
average_water_level = total_water_level / count 

# Print the highest, lowest, and average water levels with dates/times
print(f"The highest water level was {highest_water_level} observed on {highest_water_date_time}.")
print(f"The lowest water level was {lowest_water_level} observed on {lowest_water_date_time}.")
print(f"The average water level over the period was {average_water_level:.2f}.")
