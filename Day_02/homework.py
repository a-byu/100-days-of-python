# Get user input and calculate tax
base_income: float = float(input('Enter your yearly income: '))
tax_rate: float = float(input('Enter your tax rate percentage: ')) / 100
taxed: float = base_income * tax_rate

#Projection
income_2 = base_income * 2
income_3 = base_income * 3

taxed_2 = income_2 * tax_rate
taxed_3 = income_3 * tax_rate

# Display the data
print('=' * 40)
print('Income Tax Calculator')
print('=' * 40)
print(f'Base Income:              ${base_income:,.2f}')
print(f'Tax Rate:                 {tax_rate:.0%}')
print('-' * 40)
print(f'Yearly Tax (Base):        ${taxed:,.2f}')
print('=' * 40)

print(f"\n2x Yearly Income Tax Projection:        ${taxed_2:,.2f}")
print(f"\n3x Yearly Income Tax Projection:        ${taxed_3:,.2f}")