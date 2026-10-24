
def check_password(password):
    checks = {
        "Length (at least 8 characters)": len(password) >= 8,
        "Uppercase letter (A-Z)": any(c.isupper() for c in password),
        "Lowercase letter (a-z)": any(c.islower() for c in password),
        "Number (0-9)": any(c.isdigit() for c in password),
        "Symbol (!@#$%^&*)": any(
            not c.isalnum() and not c.isspace()
            for c in password
        )
    }

    print("\nPassword Analysis:")

    for description, satisfied in checks.items():
        status = "Satisfied" if satisfied else "Not satisfied"
        symbol = "✓" if satisfied else "✗"
        print(f"{symbol} {description}: {status}")

    score = sum(checks.values())

    if score == 5:
        strength = "STRONG"
    elif score >= 3:
        strength = "MODERATE"
    else:
        strength = "WEAK"

    print(f"\nPassword Strength: {strength}")


def main():
    print("=== Password Strength Checker ===")

    while True:
        password = input(
            "\nEnter your password (or type 'exit' to quit): "
        )

        if password.lower() == "exit":
            print("Thank you! Goodbye!")
            break

        check_password(password)


if __name__ == "__main__":
    main()
