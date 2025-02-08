#!/usr/bin/env python3

import requests
import json
import os

api_token = 'Add your READ ONLY wise.com API key here'  # API Key.
currency1 = "GBP"                                   # Source currency.
currency2 = "PHP"                                   # Target currency.
icon = "₱"                                          # Target currency icon $ £ ₱ etc
goodrate = 73.99                                    # Warn when above.

home_directory = os.getenv('HOME')  # Gets the value of the HOME environment variable
file_path = os.path.join(home_directory, '.config/hypr/waybar/scripts/Currency/rate_history')




def get_exchange_rate():
    # Set your API token here
    url = f'https://api.wise.com/v1/rates?source={currency1}&target={currency2}'
    
    headers = {
        'Authorization': f'Bearer {api_token}'
    }
    
    # Make the API request
    response = requests.get(url, headers=headers)
    
    try:
        # Parse the JSON response
        response_data = response.json()
    except json.JSONDecodeError:
        return json.dumps({'error': 'Invalid JSON response from API'})

    # Extract the exchange rate
    if response_data and isinstance(response_data, list):
        rate = response_data[0].get('rate')
        if rate is not None:
            # Format the rate to two decimal places
            formatted_rate = f'{rate:.3f}'
            current_rate = float(formatted_rate)

            # Get the previous rate from the rate_history file
            previous_rate = None
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    if lines:
                        # Get the last entry in the rate history
                        previous_rate = float(lines[-1].strip())
                        
            if previous_rate is not None:
                if current_rate > previous_rate:
                    result_text = f'󰜷 {icon}:{formatted_rate}'
                    status = 'caution'
                elif current_rate < previous_rate:
                    result_text = f'󰜮 {icon}:{formatted_rate}'
                    status = 'warning'
                else:
                    result_text = f'󰜴 {icon}:{formatted_rate}'
                    status = 'disabled'
            else:
                result_text = f'No data.'
                status = 'warning'
                
            # Conditional logic for rate comparison
            if current_rate > goodrate:
                status = 'enabled'

            # Append the current rate to the rate_history file if it's different from the previous rate
            if current_rate != previous_rate:
                with open(file_path, 'a') as file:
                    file.write(f'{formatted_rate}\n')

            result = {
                'text': result_text,
                'class': status
            }
            return json.dumps(result)
        
    return json.dumps({'error': 'Unable to fetch the exchange rate'})

if __name__ == '__main__':
    # Get and print the exchange rate in JSON format
    result_json = get_exchange_rate()
    print(result_json)