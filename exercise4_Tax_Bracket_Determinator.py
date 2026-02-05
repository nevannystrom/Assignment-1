# Exercise 4: Tax Bracket Determiner
# This program uses conditionals and functions returning bool/values

def get_tax_bracket(income):
    if income < 0:
        return "Invalid income"

    if income < 50000:
        tax_bracket = "Low (10%)"
    elif 50000 <= income < 100000:
        tax_bracket = "Medium (20%)"
    else:
        tax_bracket = "High (30%)"

    # ternary bonus
    tax_bracket = tax_bracket + " (Deduction Eligible)" if int(income) % 2 == 0 else tax_bracket

    return tax_bracket


def main():
    income = float(input("What is your annual income? "))
    tax_bracket = get_tax_bracket(income)

    if tax_bracket == "Invalid income":
        print(tax_bracket)
        return

    if "10%" in tax_bracket:
        rate = 0.10
    elif "20%" in tax_bracket:
        rate = 0.20
    else:
        rate = 0.30

    estimated_tax = income * rate
    print(f"Based on an income of ${income}, your estimated tax is ${estimated_tax:.2f}.")
    print(f"Your tax bracket is {tax_bracket} with a tax rate of {rate * 100}%.")


main()

