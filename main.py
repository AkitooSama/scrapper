import asyncio
import config
from google_sheets import get_hashtags
from scraper import scrape_instagram_images
from downloader import download_images
from drive_uploader import upload_to_google_drive
from db_handler import initialize_db, save_image_url

def main():
    initialize_db()
    hashtags = get_hashtags()

    for hashtag in hashtags:
        print(f"Scraping images for #{hashtag}...")
        image_urls = scrape_instagram_images(hashtag)

        if not image_urls:
            print(f"No images found for #{hashtag}. Skipping.")
            continue

        for url in image_urls:
            save_image_url(hashtag, url)

        asyncio.run(download_images(image_urls, hashtag))
        upload_to_google_drive(f"{config.IMAGE_DIR}/{hashtag}")

        print(f"Completed processing for #{hashtag}!\n")

if __name__ == "__main__":
    main()
