#!/usr/bin/env python3

import os
import subprocess

currency1 = "GBP"
c1icon = "£"
currency2 = "PHP"
c2icon = "₱"

home_directory = os.getenv('HOME')  # Gets the value of the HOME environment variable
file_path = os.path.join(home_directory, '.config/hypr/waybar/scripts/Currency/rate_history')

def read_rate(file_path):
    """Read the last conversion rate from rate_history."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if not lines:
                raise ValueError("Rate history file is empty.")
            last_rate_str = lines[-1].strip()
            return float(last_rate_str)  # Convert the last entry to float
    except Exception as e:
        print(f"Error: Failed to read rate from file: {e}")
        return None

def launch_yad(currency1='', currency2='', converted='', cur2='', cur1=''):
    """Launch YAD dialog for currency conversion with pre-filled values."""
    dialog_command = [
        "yad", "--form", "--title=Currency Converter", "--text=Enter the amount:",
        f"--field={currency2} {c2icon}", cur2,
        f"--field={currency1} {c1icon}", cur1,
        "--field=Converts to:RO", converted,
        "--button=Convert!gtk-ok:0", "--button=Exit:1"
    ]

    try:
        # Run the dialog and capture user input
        yad_output = subprocess.check_output(dialog_command, text=True)
        yad_output = yad_output.strip()
        cur2_value, cur1_value, _ = (yad_output.split('|') + ['', '', ''])[:3]
        return cur2_value, cur1_value

    except subprocess.CalledProcessError as e:
        if e.returncode != 1:  # 1 is the exit button code
            print(f"Error: Failed to launch or get input from YAD: {e}")
        return None, None

def main():
    rate = read_rate(file_path)
    if rate is None:
        return

    cur2, cur1, converted = '', '', ''

    while True:
        cur2, cur1 = launch_yad(currency1, currency2, converted, cur2, cur1)
        
        if cur2 is None and cur1 is None:
            break  # User chose to exit

        try:
            if cur2 and not cur1:
                cur2_value = float(cur2)
                converted_value = cur2_value / rate
                converted = f"{converted_value:.2f} {currency1}"
            elif cur1 and not cur2:
                cur1_value = float(cur1)
                converted_value = cur1_value * rate
                converted = f"{converted_value:.2f} {currency2}"
            else:
                converted = "Please enter a value in one field only."
        except ValueError:
            converted = "Invalid input, please enter a numeric value."

if __name__ == "__main__":
    main()
