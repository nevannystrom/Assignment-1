# Exercise 2: Credit Score Evaluator
# This program uses conditionals to evaluate credit scores

def main():
    score = int(input("What's your credit score? ").strip())

    # Validate score range
    if score < 300 or score > 850:
        print("Invalid score.")
    # elif = else if
    elif score >= 750:
        print("Excellent - Loan Approved. Interest rate: Low")
    
    elif 700 <= score < 750:
        print("Good - Loan Approved with Review. Interest rate: Low")
    
    elif 600 <= score < 700:
        print("Fair - Loan Conditional. Seek credit improvement.")
    
    else:
        print("Poor - Loan Denied. Seek credit improvement.")

main()