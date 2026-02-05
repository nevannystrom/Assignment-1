# helper function (returns True/False)
def is_profitable(revenue, cost):
    return revenue > cost


def categorize_product(category_input):
    name = category_input.strip().lower()

    match name:
        case "electronics" | "gadget":
            return "High Margin"
        case _ if name.startswith("tech"):
            return "High Margin"
        case "clothing" | "apparel":
            return "Medium Margin"
        case "food" | "grocery":
            return "Low Margin"
        case _:
            return "Uncategorized"


def main():
    revenue = float(input("Enter business revenue: "))
    cost = float(input("Enter business cost: "))
    category_input = input("Enter product category: ")

    category = categorize_product(category_input)

    if is_profitable(revenue, cost):
        profit = revenue - cost
        print(f"Profitable! Profit: ${profit:.2f}")

        match category:
            case "High Margin":
                print("Suggestion: Reinvest")
            case "Medium Margin":
                print("Suggestion: Maintain inventory")
            case "Low Margin":
                print("Suggestion: Reduce costs")
            case _:
                print("Suggestion: Review business strategy")

    else:
        print("Not profitable. Review pricing or expenses.")


main()
