import tkinter as tk
import re

# Function to assess the strength of the password
def assess_password_strength():
    password = entry_password.get()
    feedback = ""
    
    # Criteria checks
    length_check = len(password) >= 8
    upper_check = re.search(r'[A-Z]', password)
    lower_check = re.search(r'[a-z]', password)
    digit_check = re.search(r'\d', password)
    special_char_check = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    
    # Score calculation
    score = 0
    if length_check:
        score += 1
    if upper_check:
        score += 1
    if lower_check:
        score += 1
    if digit_check:
        score += 1
    if special_char_check:
        score += 1
    
    # Strength evaluation
    if score == 5:
        feedback = "Strong Password!"
        result_label.config(fg="green")
    elif score >= 3:
        feedback = "Moderate Password!"
        result_label.config(fg="orange")
    else:
        feedback = "Weak Password!"
        result_label.config(fg="red")
    
    # Provide detailed feedback
    detailed_feedback = []
    if not length_check:
        detailed_feedback.append("- Password should be at least 8 characters long.")
    if not upper_check:
        detailed_feedback.append("- Password should contain at least one uppercase letter.")
    if not lower_check:
        detailed_feedback.append("- Password should contain at least one lowercase letter.")
    if not digit_check:
        detailed_feedback.append("- Password should contain at least one digit.")
    if not special_char_check:
        detailed_feedback.append("- Password should contain at least one special character.")
    
    result_label.config(text=feedback)
    feedback_label.config(text="\n".join(detailed_feedback))
root = tk.Tk()
root.title("Password Strength Checker")
tk.Label(root, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show="*", width=40)
entry_password.grid(row=0, column=1, padx=10, pady=10)
check_button = tk.Button(root, text="Check Password Strength", command=assess_password_strength)
check_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
feedback_label = tk.Label(root, text="", font=('Arial', 10), justify=tk.LEFT)
feedback_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
root.mainloop()
