import os
import time
import datetime
import platform
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from tools import smart_decode


def get_dom_html():
    dom_html = ''
    print('set options')
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('blink-settings=imagesEnabled=false')

    print('set driver')
    thor_main_dir = os.path.dirname(os.path.dirname(__file__))
    if platform.system().lower() == 'windows':
        driver_path = os.path.join(thor_main_dir, 'public', 'chromedriver.exe')
    else:
        driver_path = os.path.join(thor_main_dir, 'public', 'chromedriver')
    print('driver path is: %s' % driver_path)
    driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
    driver.maximize_window()

    try:
        print('send get request')
        base_url = "https://free.leisu.com/"
        driver.get(base_url)
        datetime_string = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        print('waiting for dom render...')
        table_dom = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "screen-view")))
        print('waiting for another 5 seconds...')
        time.sleep(5)
        print('create html file')
        file_path = os.path.join(thor_main_dir,
                                 'data',
                                 '%s.html' % datetime_string)
        print('create html file: %s' % file_path)
        dom_html = smart_decode(table_dom.get_attribute('outerHTML')).encode('utf8')
        with open(file_path, 'w') as file:
            file.write(dom_html)

        # print('save page png')
        # png_path = os.path.join(os.path.dirname(os.getcwd()),
        #                         'data',
        #                         'img',
        #                         '%s.png' % datetime_string)
        # driver.save_screenshot(png_path)
    except Exception, e:
        print('*' * 25 + 'Error' + '*' * 25)
        print(traceback.format_exc())
    finally:
        print('close drive')
        driver.close()
        driver.quit()
        return dom_html


if __name__ == '__main__':
    get_dom_html()