import tkinter as tk
import re

# Function to check the strength of the password
def check_password_strength(password):
    if len(password) < 8:
        return "Weak", "Password must be at least 8 characters long."
    
    if not re.search(r"[A-Z]", password):
        return "Weak", "Password must contain at least one uppercase letter."
    
    if not re.search(r"[a-z]", password):
        return "Weak", "Password must contain at least one lowercase letter."
    
    if not re.search(r"\d", password):
        return "Weak", "Password must contain at least one number."
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Moderate", "Password is good but could be stronger with special characters."

    return "Strong", "Your password is strong!"

# Function to assess password strength and display the result
def assess_password():
    password = entry_password.get()
    strength, feedback = check_password_strength(password)
    
    lbl_strength.config(text=f"Password Strength: {strength}", fg="green" if strength == "Strong" else "red")
    lbl_feedback.config(text=feedback)

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

# Instructions
lbl_instruction = tk.Label(root, text="Enter a password to assess its strength:", font=("Arial", 12))
lbl_instruction.pack(pady=10)

# Password input field
entry_password = tk.Entry(root, show="*", width=30, font=("Arial", 14))
entry_password.pack(pady=10)

# Button to check password strength
btn_check = tk.Button(root, text="Check Password Strength", command=assess_password, font=("Arial", 12))
btn_check.pack(pady=10)

# Label to display password strength result
lbl_strength = tk.Label(root, text="", font=("Arial", 14))
lbl_strength.pack(pady=10)

# Label to display feedback on password strength
lbl_feedback = tk.Label(root, text="", wraplength=300, font=("Arial", 12))
lbl_feedback.pack(pady=10)

# Run the GUI
root.mainloop()
