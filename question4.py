import csv

previous_water_level = None
# Initialize variable

# Open and read the CSV file
with open('/Users/tavisgoldwire/Desktop/CO-OPS__8729108__wl.csv', 'r') as file:
    csv_reader = csv.reader(file)

    # For loop through each row in the CSV file
    for row in csv_reader:
        
        if row[1] == '': # Check if the row is empty or missing the water level value
            print(f"Warning: No water level reading received at {row[0] if row else 'Unknown time'}.")
            continue

        try:
            water_level = float(row[1])  # Read the water level from column 2 (index 1)
        except ValueError:
            print(f"Warning: Invalid water level reading at {row[0]}.")
            #f string warning with water level reading 
            continue

        # Check if the water level increases more than 0.25 since the previous recording
        if previous_water_level != None:
            if (water_level - previous_water_level) > 0.25:
                print(f"Warning: Water level increased by more than 0.25 at {row[0]} (current level: {water_level:.2f}).")
            elif water_level > 5.0:  # if first if statement false then checks this
                print(f"Warning: Water level exceeds 5.0 at {row[0]} (current level: {water_level:.2f}).")

        # Update the previous water level for the next iteration
        previous_water_level = water_level
