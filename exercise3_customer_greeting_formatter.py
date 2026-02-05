# Exercise 3: Customer Greeting Formatter
# This function formats customer greetings using strings and functions

def format_greeting(name, title="Customer"):
    # Clean extra spaces
    clean = " ".join(name.split())

    # Handle empty input
    if clean == "":
        return "Hello, Valued Customer!"

    # Extract and format first name
    first_name = clean.split()[0].title()

    return f"Hello, {first_name} ({title})!"

name = input("What's your full name? ").strip()
print(format_greeting(name))
