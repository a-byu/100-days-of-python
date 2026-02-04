print("This is miles to kilometers converter and vice versa")

# User input
miles_input = input("\nEnter miles to convert")
kilometers_input = input("Enter kilometers to convert")

# Conversion
miles_to_km = miles_input * 1.60934
km_to_miles = kilometers_input * 0.621371

# Display
print(f'{miles_input} miles -> {miles_to_km} Km')
print(f'{kilometers_input} Km -> {km_to_miles} miles')