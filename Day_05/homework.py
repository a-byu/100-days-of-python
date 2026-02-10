# 1. Get the user input for the total bill amount
print('\nWelcome to Expense Splitter™!')
total_bill = input('1. Enter the total bill you would like to split: ')
bill_str = str(total_bill)

while bill_str == '':
    total_bill = input('\n1. Enter the total bill you would like to split: ')
    bill_str = str(total_bill)
    if not bill_str == '':
        break

while bill_str == '0':
    total_bill = input('\n1. You can not enter 0 damnit!. please try again: ')
    bill_str = str(total_bill)
    if not bill_str == '0':
        break

bill_float = float(bill_str)

# 2. Add the participants to the bill
people: list[str] = []
print('\n2. Add participants (press Enter on an empty line when finished):')
while True:
    input_name: str = input('Name: ').lower()
    if input_name.strip() == '':
        break

    # Check for duplicate names
    if input_name in people:
        print('That name is already listed. Please add a different name.')
    else:
        people.append(input_name)

# 3. Splitting the bill
print('\n3. Now, specify the percentage each person will pay.')
print('(Type "even" at any time to split the bill equally.)')

# Create a dictionary that holds how much each person owes
people_dict: dict[str, float] = {}
total_percent: float = 100.0

# Get inputs for each person
for person in people:
    percent_input: str = input(f'[{total_percent:.0f}% remaining] {person.capitalize()}: ').lower()

    # If you tap on enter, 0 will be the default value
    if percent_input.strip() == '':
        percent_input = '0'

    # Typing 'even' will split the bill evenly
    if percent_input.strip() == 'even':
        for nested_person in people:
            people_dict[nested_person] = (1 / len(people)) * bill_float
        break

    people_dict[person] = (float(percent_input) / 100) * bill_float
    total_percent -= float(percent_input)

# 4. Display the information
print('\n--- Split Summary ---')
for name, share in people_dict.items():
    print(f'{name.capitalize():10}: ${share:,.2f}')
print('---------------------')