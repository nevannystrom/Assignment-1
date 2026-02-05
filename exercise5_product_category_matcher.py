def categorize_product(product_name):
    # clean input
    name = product_name.strip().lower()

    # match categories
    match name:
        case "electronics" | "gadget":
            category = "High Margin"
        case _ if name.startswith("tech"):
            category = "High Margin"
        case "clothing" | "apparel":
            category = "Medium Margin"
        case "food" | "grocery":
            category = "Low Margin"
        case _:
            category = "Uncategorized - Review Needed"

    return name, category


def main():
    product = input("What's the product name? ")
    name, category = categorize_product(product)

    print(f"Product: {name} | Category: {category}")


main()
