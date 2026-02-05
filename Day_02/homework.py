# tax_bracket = [(10000, 0.10), (40000, 0.12), (float('inf'), 0.22)]

# Get user input and calculate tax

income = float(input("Enter your yearly income: "))

def calculate_tax(income):
    total_tax = 0
# Bracket 1: 0 to 10,000 at 10%
    chunk_1 = min(income, 10000) - 0
    tax_1 = chunk_1 * 0.10
    total_tax = total_tax + tax_1

# Bracket 2: 10,000 to 40,000 at 12%
    chunk_2 = min(income, 40000) - 10000
    tax_2 = chunk_2 * 0.12
    total_tax = total_tax + tax_2

# Bracket 3: 40,000 to infinity at 22%
    chunk_3 = min(income, float('inf')) - 40000
    tax_3 = chunk_3 * 0.22
    total_tax = total_tax + tax_3

    return total_tax

tax_base = calculate_tax(income)
effective_rate = (tax_base / income)

# Display the data
print('=' * 40)
print('Income Tax Calculator')
print('=' * 40)
print(f'Base Income:              ${income:,.2f}')
print(f'Tax Rate:                 {effective_rate:.1%}')
print('-' * 40)
print(f'Yearly Tax (Base):        ${tax_base:,.2f}')
print('=' * 40)

print(f"\n2x Yearly Income Tax Projection:        ${calculate_tax(income * 2):,.2f}")
print(f"\n3x Yearly Income Tax Projection:        ${calculate_tax(income * 3):,.2f}")