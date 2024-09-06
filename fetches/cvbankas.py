import requests
from bs4 import BeautifulSoup
import re
import json
import os
from log_config import logger
from config import CVBANKAS_KEYWORDS
from dotenv import load_dotenv

load_dotenv()

def fetch_cvbankas_jobs():
    keywords = CVBANKAS_KEYWORDS
    jobs = []
    total_ads = 0
    for keyword in keywords:
        url = f"https://en.cvbankas.lt/?keyw={keyword}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Error fetching data from CVBankas for {keyword}: {e}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        job_list = soup.find(id="js_id_id_job_ad_list")
        
        if not job_list:
            logger.warning(f"Could not find job list on the page for {keyword}")
            continue

        total_ads = extract_total_ads(soup)
        jobs.extend(extract_jobs(job_list, keyword))

    logger.info(f"Successfully fetched {len(jobs)} job listings from CVBankas")
    logger.info(f"Total ads on CVBankas: {total_ads}")

    # Save the fetched jobs
    save_cvbankas_jobs(jobs, total_ads)

    return jobs, total_ads

def extract_total_ads(soup):
    filter_stats = soup.find('span', class_='filter_statistics')
    if filter_stats:
        match = re.search(r'\(view all ([\d,]+) ads\)', filter_stats.text)
        if match:
            return int(match.group(1).replace(',', ''))
    return 0

def extract_jobs(job_list, keyword):
    jobs = []
    for article in job_list.find_all('article', class_='list_article'):
        job = {
            'title': extract_text(article, 'h3', 'list_h3'),
            'company': extract_text(article, 'span', 'dib mt5 mr5'),
            'salary': extract_salary(article),
            'keyword': keyword
        }
        jobs.append(job)
    return jobs

def extract_text(article, tag, class_name):
    element = article.find(tag, class_=class_name)
    return element.text.strip() if element else "N/A"

def extract_salary(article):
    salary_elem = article.find('span', class_='salary_amount')
    if not salary_elem:
        return "N/A"
    
    salary = salary_elem.text.strip()
    salary_period = extract_text(article, 'span', 'salary_period')
    salary_type = extract_text(article, 'span', 'salary_calculation')
    
    if salary_period and salary_type:
        return f"{salary} {salary_period} ({salary_type})"
    return salary

def save_cvbankas_jobs(jobs, total_ads):
    data_to_save = {
        "total_ads": total_ads,
        "jobs": jobs,
    }

    base_dir = os.getenv("BASE_DIR")
    file_path = os.path.join(base_dir, "data/cvbankas_ads.json")

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)
        logger.info(f"Data successfully saved to {file_path}")
    except IOError as e:
        logger.error(f"Failed to save data to {file_path}: {e}")

def main():
    jobs, total_ads = fetch_cvbankas_jobs()
    print(jobs)
    print(total_ads)
    breakpoint()
    logger.info(f"Successfully fetched job listings for keywords: {', '.join(CVBANKAS_KEYWORDS)}")

if __name__ == "__main__":
    main()
