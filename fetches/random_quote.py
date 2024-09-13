import requests
import ssl
import json
import os
from datetime import datetime

def fetch_random_quote():
    url = "https://api.quotable.io/random"
    try:
        # Create a custom SSL context that doesn't verify certificates
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        response = requests.get(url, verify=False)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return {
            "content": data["content"],
            "author": data["author"]
        }
    except requests.RequestException as e:
        print(f"Error fetching quote: {e}")
        return {
            "content": "An error occurred while fetching the quote.",
            "author": "Unknown"
        }

def write_quote_to_file(quote):
    output = {
        "quote": quote,
        "timestamp": datetime.now().isoformat()
    }
    
    file_path = os.path.join("data", "random_quote.json")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, "w") as f:
        json.dump(output, f, indent=4)

if __name__ == "__main__":
    # Suppress the InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    
    quote = fetch_random_quote()
    write_quote_to_file(quote)
