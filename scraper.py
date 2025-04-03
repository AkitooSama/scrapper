import time
import random
import config
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_instagram_images(hashtag):
    url = f"https://www.instagram.com/explore/tags/{hashtag}/"
    image_urls = []

    options = webdriver.ChromeOptions()
    if config.HEADLESS_BROWSER:
        options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(5)  # Allow images to load

    # Scroll multiple times to get more images
    for _ in range(3):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

    images = driver.find_elements(By.TAG_NAME, "img")
    selected_images = random.sample(images, min(len(images), config.MAX_IMAGES_PER_HASHTAG))

    for img in selected_images:
        src = img.get_attribute("src")
        if src:
            image_urls.append(src)

    driver.quit()
    return image_urls
