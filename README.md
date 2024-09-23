# Password Strength Checker Tool 

This Python tool assesses the strength of a password based on various criteria and provides feedback to users about how secure their password is. The tool uses a graphical user interface (GUI) built with `Tkinter`, allowing users to easily input their password and receive feedback on its strength.

## Features
- **Password Strength Assessment**:
  - **Weak**: If the password is shorter than 8 characters or doesn't meet the minimum security criteria.
  - **Moderate**: If the password is decent but could be improved by adding special characters.
  - **Strong**: If the password is long enough and contains a good mix of uppercase, lowercase, digits, and special characters.
  
- **Criteria for Password Strength**:
  1. Minimum 8 characters in length.
  2. At least one uppercase letter.
  3. At least one lowercase letter.
  4. At least one digit.
  5. At least one special character (e.g., `!`, `@`, `#`, `$`).

## Prerequisites

Make sure you have **Python 3.x** installed. The GUI uses the `Tkinter` library, which comes pre-installed with most Python distributions.

## How to Run

1. **Clone the repository**:
   git clone https://github.com/WhiteDevil-0001/Prodigy_CS_03.git

2. Navigate to the directory:
    cd Prodigy_CS_03

3. Run the tool:
    python password_strength_checker.py

## How to Use
Enter a password in the text field.
Click on the Check Password Strength button.
The tool will display the password's strength (Weak, Moderate, or Strong) and provide feedback on how to improve the password if necessary.

## Example
Password: password

Result: Weak - "Password must contain at least one uppercase letter."
Password: Password123

Result: Moderate - "Password is good but could be stronger with special characters."
Password: Pass@1234

Result: Strong - "Your password is strong!"
