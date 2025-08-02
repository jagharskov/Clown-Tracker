from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time
import csv
import os

# Enter the streamer username here
CHANNEL_NAME = 'quin69'

# Enter the number of seconds between every check here.
# The page usually updates viewer count every 30 seconds it seems
POLL_INTERVAL = 10  

def get_csv_filename():
    current_date = datetime.now().strftime("%Y-%m-%d")
    return f"{CHANNEL_NAME}_viewer_scrape_{current_date}.csv"

def initialize_csv(filename):
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['uptime', 'viewer_count'])

def get_viewer_count(driver):
    try:
        element = driver.find_element(By.XPATH, '//span[contains(@class, "ScAnimatedNumber") and contains(@class, "jAIlLI")]')
        viewer_text = element.text.replace(',', '')
        return int(viewer_text)
    except NoSuchElementException:
        return None
        
def get_stream_time(driver):
    try:
        element = driver.find_element(By.XPATH, '//span[contains(@class, "live-time")]//span[@aria-hidden="true"]')
        time_text = element.text  # e.g., "8:10:11"
        return time_text
    except NoSuchElementException:
        return None

def main():
    url = "https://www.twitch.tv/" + CHANNEL_NAME
    loading_time = 10
    err_check = 0
    
    options = FirefoxOptions()
    options.add_argument("--headless")

    csv_file = get_csv_filename()
    initialize_csv(csv_file)

    driver = webdriver.Firefox(options=options)
    print(f"Fetching {url} and waiting {loading_time} seconds for it to load...") 
    driver.get(url)
    time.sleep(loading_time)  # Let the page load
    
 
    while True:
        
        try:
            if err_check > 4:
                print("Viewer count could not be found after repeated attempts. \
                The stream is either offline, or twitch has changed it's layout and \
                you need to replace 'element' in the get_viewer_count() function. Exiting...")
                break
                
            uptime = get_stream_time(driver)
            viewers = get_viewer_count(driver)
            
            if viewers is not None:
                err_check = 0
                print(f"[{uptime}] Viewers: {viewers}")
                with open(csv_file, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([uptime, viewers])
            else:
                err_check += 1
                print(f"[{uptime}] Viewer count not found. Hold on checking again...")
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main()
    
    
# global.storline_array[0] = 0
# global.storline_array[1] = 1
# global.storline_array[2] = 0
# global.storline_array[3] = 0
# global.storline_array[4] = 0
# global.storline_array[5] = 2
# global.storline_array[6] = 0
# global.storline_array[7] = 1
# global.storline_array[8] = 0
# global.storline_array[9] = 0
# global.storline_array[10] = 0
# global.storline_array[11] = 0
