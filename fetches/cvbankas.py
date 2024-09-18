import requests
from bs4 import BeautifulSoup
import json
import os
import sys
from dotenv import load_dotenv
from datetime import datetime

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from log_config import logger
from config import CVBANKAS_KEYWORDS, CVBANKAS_IGNORE_KEYWORDS

load_dotenv()

def fetch_cvbankas_jobs():
    logger.info("##########################################################")
    logger.info("Fetch CVBankas jobs START")

    jobs = []
    for keyword in CVBANKAS_KEYWORDS:
        for page in range(1, 6):
            url = f"https://en.cvbankas.lt/?keyw={keyword}&page={page}"
            
            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.RequestException as e:
                logger.error(f"Error fetching data from CVBankas for {keyword} page {page}: {e}")
                continue

            soup = BeautifulSoup(response.text, 'html.parser')
            job_list = soup.find(id="js_id_id_job_ad_list")
            
            if not job_list:
                logger.warning(f"Could not find job list on the page for {keyword} page {page}")
                continue

            jobs.extend(extract_jobs(job_list, keyword))

        logger.info(f"Fetched jobs for keyword: {keyword}")

    logger.info(f"Successfully fetched {len(jobs)} job listings for keywords: {CVBANKAS_KEYWORDS}")
    logger.info("Fetch CVBankas jobs END")
    logger.info("##########################################################")

    return jobs

def filter_cvbankas_jobs(jobs):
    filtered_jobs = [job for job in jobs if is_salary_above(job['salary'], 3000) and not has_ignored_keywords(job['title'])]
    logger.info(f"Filtered {len(filtered_jobs)} out of {len(jobs)} jobs")
    return filtered_jobs

def extract_jobs(job_list, keyword):
    jobs = []
    for article in job_list.find_all('article', class_='list_article'):
        job = {
            'title': extract_text(article, 'h3', 'list_h3'),
            'company': extract_text(article, 'span', 'dib mt5 mr5'),
            'salary': extract_salary(article),
            'keyword': keyword,
            'image_link': extract_image_link(article)
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

def extract_image_link(article):
    img_elem = article.find('img')
    return img_elem['src'] if img_elem else "N/A"

def is_salary_above(salary, min_salary):
    if salary == "N/A":
        return False
    try:
        # Extract the first number from the salary string
        salary_value = float(''.join(filter(str.isdigit, salary.split('-')[0])))
        return salary_value >= min_salary
    except ValueError:
        return False

def has_ignored_keywords(title):
    return any(keyword.lower() in title.lower() for keyword in CVBANKAS_IGNORE_KEYWORDS)

def save_cvbankas_jobs(jobs):
    data_to_save = {
        "fetch_date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "jobs": jobs
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
    jobs = fetch_cvbankas_jobs()
    filtered_jobs = filter_cvbankas_jobs(jobs)
    save_cvbankas_jobs(filtered_jobs)

if __name__ == "__main__":
    main()
