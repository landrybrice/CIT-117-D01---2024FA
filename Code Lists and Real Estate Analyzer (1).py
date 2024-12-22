import csv

# Step 1: Make a function to read data from a CSV file and return it as a list.
def getDataInput(file_path):
    records = []
    # Step 2: Open the file in read mode and use csv reader to read it.
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Step 3: Skip the first row since it has the column names.
        for record in csv_reader:
            records.append(record)  # Step 4: Add each row to the list.
    return records  # Step 5: Return all the records.

# Step 6: Make a function to find the median in a list of numbers.
def getMedian(values):
    values.sort()  # Step 7: Sort the numbers from smallest to largest.
    mid = len(values) // 2  # Step 8: Find the middle position in the list.
    if len(values) % 2 == 0:  # Step 9: If there’s an even number of values,
        # Step 10: Take the average of the two middle numbers.
        return (values[mid - 1] + values[mid]) / 2
    else:
        # Step 11: If there’s an odd number of values, just take the middle one.
        return values[mid]

# Step 12: Make the main function that runs our program.
def main():
    file_path = 'RealEstateData.csv'  # Step 13: Set the path to the CSV file.
    records = getDataInput(file_path)  # Step 14: Call getDataInput to read the file.
    
    # Step 15: Make empty lists and dictionaries to store data.
    property_prices = []  # To keep track of all prices.
    city_totals = {}  # To keep track of total prices for each city.
    property_type_totals = {}  # To keep track of total prices for each property type.
    zip_totals = {}  # To keep track of total prices for each zip code.
    
    # Step 16: Go through each record to get the info we need.
    for record in records:
        city = record[1]  # Step 17: Get the city from this row.
        property_type = record[7]  # Step 18: Get the property type.
        price = float(record[8])  # Step 19: Change the price to a float (decimal).
        
        # Step 20: Add the price to our list of all prices.
        property_prices.append(price)
        
        # Step 21: Update the total price for this city.
        if city in city_totals:
            city_totals[city] += price
        else:
            city_totals[city] = price
        
        # Step 22: Update the total price for this property type.
        if property_type in property_type_totals:
            property_type_totals[property_type] += price
        else:
            property_type_totals[property_type] = price
        
        # Step 23: Update the total price for this zip code.
        zip_code = record[2]
        if zip_code in zip_totals:
            zip_totals[zip_code] += price
        else:
            zip_totals[zip_code] = price
    
    # Step 24: Sort the prices list.
    property_prices.sort()
    
    # Step 25: Find the min, max, total, average, and median prices.
    property_prices = [float(price) for price in property_prices]  # Make sure prices are floats.
    min_price = min(property_prices)
    max_price = max(property_prices)
    total_price = sum(property_prices)
    avg_price = total_price / len(property_prices)
    median_price = getMedian(property_prices)

    # Step 26: Print the basic statistics with labels.
    print("\n--- Real Estate Price Analysis ---")
    print(f"Minimum Price: ${min_price:,.2f}")
    print(f"Maximum Price: ${max_price:,.2f}")
    print(f"Total Price: ${total_price:,.2f}")
    print(f"Average Price: ${avg_price:,.2f}")
    print(f"Median Price: ${median_price:,.2f}")

    # Step 27: Print total prices by city.
    print("\nCity Totals:")
    for city, total in city_totals.items():
        print(f"{city}: ${total:.2f}")
    
    # Step 28: Print total prices by property type.
    print("\nProperty Type Totals:")
    for property_type, total in property_type_totals.items():
        print(f"{property_type}: ${total:.2f}")
    
    # Step 29: Print total prices by zip code.
    print("\nZip Totals:")
    for zip_code, total in zip_totals.items():
        print(f"{zip_code}: ${total:.2f}")

# Step 30: Run the main function to start the program.
if __name__ == "__main__":
    main()
