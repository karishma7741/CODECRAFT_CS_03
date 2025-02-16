import re

def check_password_strength(password):
    feedback = []
    strength = 0
    
    # Length check (minimum 8 characters)
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Uppercase letter check
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    # Lowercase letter check
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Number check
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., !, @, #).")
    
    # Assessing overall strength
    if strength == 5:
        feedback.append("Password is strong.")
    elif strength == 4:
        feedback.append("Password is good, but could be improved.")
    elif strength == 3:
        feedback.append("Password is okay, but not very secure.")
    else:
        feedback.append("Password is weak. Consider improving it.")
    
    return feedback

# Main function to interact with the user
def main():
    password = input("Enter your password to check its strength: ")
    feedback = check_password_strength(password)
    
    print("\nPassword Strength Assessment:")
    for line in feedback:
        print(line)

# Run the password checker tool
main()
