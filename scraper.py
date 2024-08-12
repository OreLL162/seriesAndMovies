import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config

def clean_title(title):
    return re.sub(r'^\d+\.\s*', '', title)

def get_upcoming_items(choice, category):
    try:
        print("Initializing WebDriver...")
        options = webdriver.ChromeOptions()
        options.binary_location = config.WEBDRIVER_PATH
        driver = webdriver.Chrome(options=options)

        print("Setting URL...")
        if choice == 'movies':
            url = f'https://www.imdb.com/chart/top/?ref_=nv_mv_250&genres={category}'
        elif choice == 'series':
            url = f'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250&genres={category}'

        print("Navigating to URL...")
        driver.get(url)
        print("Waiting for items to load...")

        # Allow some time for the page to load before finding elements
        driver.implicitly_wait(5)  # Set an implicit wait

        # Use find_elements directly
        items = driver.find_elements(By.CSS_SELECTOR, 'li.ipc-metadata-list-summary-item.sc-10233bc-0.TwzGn.cli-parent')
        
        print(f"Found {len(items)} items.")
        upcoming_items = []
        for item in items:

            raw_title = item.find_element(By.CSS_SELECTOR, 'a h3').text
            title = clean_title(raw_title)            
            rating = item.find_element(By.CSS_SELECTOR, 'span.ipc-rating-star--rating').text
            release_date = item.find_element(By.CSS_SELECTOR, 'span.cli-title-metadata-item').text.split('|')[0].strip()
            upcoming_items.append({'title': title, 'release_date': release_date, 'rating': rating})
        return upcoming_items

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()