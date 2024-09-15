import requests
import os
import sys
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from log_config import logger

# Your RescueTime API keys
api_key_ag = os.getenv("AG_RESCUETIME_API_KEY")

# Pick yesterday's date
yesterday_full = datetime.now() - timedelta(days=1)
yesterday_formatted = yesterday_full.strftime("%Y-%m-%d")

def fetch_for_user(api_key, yesterday_formatted):
    # Define the API endpoint URL
    api_url = f"https://www.rescuetime.com/anapi/daily_summary_feed?key={api_key}"

    # Make the API request
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        
        # Filter the data for the specific date
        filtered_data = [entry for entry in data if entry['date'] == yesterday_formatted]
        
        if filtered_data:
            return filtered_data[0]
        else:
            logger.warning(f"No data found for {yesterday_formatted}")
            return None
    else:
        logger.error(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

def save_rescuetime_data(data):
    data_to_save = {
        "fetch_date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "rescuetime_data": data
    }

    base_dir = os.getenv("BASE_DIR")
    file_path = os.path.join(base_dir, "data/rescuetime_data.json")

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)
        logger.info(f"RescueTime data successfully saved to {file_path}")
    except IOError as e:
        logger.error(f"Failed to save RescueTime data to {file_path}: {e}")

def main():
    ag_data = fetch_for_user(api_key_ag, yesterday_formatted)

    combined_data = {
        "ag": ag_data,
    }

    save_rescuetime_data(combined_data)

if __name__ == "__main__":
    main()