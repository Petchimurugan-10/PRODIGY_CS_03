import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Check the length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check for digits
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Password should include at least one digit.")

    # Check for special characters
    if re.search(r'[\W_]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Strength Levels
    strength_level = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]

    # Ensure that strength does not exceed the maximum index of strength_level
    if strength > 4:
        strength = 4

    if strength == 4:
        feedback.append("Your password is very strong.")

    return strength_level[strength], feedback

def main():
    # Prompt the user to enter a password
    password = input("Enter your password: ")

    # Assess the password strength
    strength, feedback = assess_password_strength(password)

    # Output the results
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for comment in feedback:
            print(f"- {comment}")

if __name__ == "__main__":
    main()
