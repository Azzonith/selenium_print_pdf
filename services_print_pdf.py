import base64
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def navigate_links(driver, links):
    for link in links:
        driver.get(link)
        time.sleep(5)  # Wait for the page to load
        fl = driver.print_page()
        file_name = link.split('/')[-1]
        with open(f'{file_name}.pdf', "wb") as outfile:
            outfile.write(base64.b64decode(fl))


def main():
    options = Options()
    options.add_argument('--headless=new')  # Run Chrome in headless mode
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    try:
        driver = webdriver.Chrome(options=options)
        url = f'https://www.example.com/knowledge-base.html'
        driver.get(url)
        time.sleep(5)  # Wait for the page to load
        elements = driver.find_elements(By.CLASS_NAME, 'class_name_goes_here')
        link_urls = [link.get_attribute('href') for link in elements]
        print(f'found the links on page: {link_urls}')
        navigate_links(driver, link_urls)
        driver.quit()
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
