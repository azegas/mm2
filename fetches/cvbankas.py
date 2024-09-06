import requests
from bs4 import BeautifulSoup
import re
import json
from log_config import logger
from config import CVBANKAS_KEYWORDS

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

        # Extract total ads count
        filter_stats = soup.find('span', class_='filter_statistics')
        if filter_stats:
            match = re.search(r'\(view all ([\d,]+) ads\)', filter_stats.text)
            if match:
                total_ads = int(match.group(1).replace(',', ''))

        for article in job_list.find_all('article', class_='list_article'):
            job = {}
            
            # Extract job title
            title_elem = article.find('h3', class_='list_h3')
            job['title'] = title_elem.text.strip() if title_elem else "N/A"
            
            # Extract company name
            company_elem = article.find('span', class_='dib mt5 mr5')
            job['company'] = company_elem.text.strip() if company_elem else "N/A"
            
            # Extract salary
            salary_elem = article.find('span', class_='salary_amount')
            if salary_elem:
                job['salary'] = salary_elem.text.strip()
                
                # Extract salary period and type (Gross/Net)
                salary_period = article.find('span', class_='salary_period')
                salary_type = article.find('span', class_='salary_calculation')
                if salary_period and salary_type:
                    job['salary'] += f" {salary_period.text.strip()} ({salary_type.text.strip()})"
            else:
                job['salary'] = "N/A"
            
            job['keyword'] = keyword
            jobs.append(job)

    logger.info(f"Successfully fetched {len(jobs)} job listings from CVBankas")
    logger.info(f"Total ads on CVBankas: {total_ads}")
    return jobs, total_ads

if __name__ == "__main__":
    jobs, total_ads = fetch_cvbankas_jobs(CVBANKAS_KEYWORDS)
    
    # Create a dictionary with jobs and total_ads
    data_to_save = {
        "total_ads": total_ads,
        "jobs": jobs,
    }
    
    # Save the data to a JSON file
    with open('data/cvbankas_ads.json', 'w', encoding='utf-8') as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)
    
    logger.info(f"Data saved to data/cvbankas_ads.json")
    logger.info(f"Successfully fetched job listings for keywords: {', '.join(CVBANKAS_KEYWORDS)}")
