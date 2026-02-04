def main():
    revenue_input = input("What's the revenue? ").split()
    cost_input = input("What's the cost? ").split()

    # Convert first value to float
    revenue = float(revenue_input[0])
    cost = float(cost_input[0])

    # Check for valid revenue
    if revenue > 0:
        profit = revenue - cost
        margin = (profit / revenue) * 100

        print(f"Profit: ${profit:,.2f} | Margin: {margin:.2f}%")
    else:
        print("Invalid revenue.")

main()