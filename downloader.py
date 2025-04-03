import os
import aiohttp
import asyncio
import config

async def download_image(session, url, filepath):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                with open(filepath, "wb") as f:
                    f.write(await response.read())
    except Exception as e:
        print(f"Error downloading {url}: {e}")

async def download_images(image_urls, hashtag):
    hashtag_dir = os.path.join(config.IMAGE_DIR, hashtag)
    os.makedirs(hashtag_dir, exist_ok=True)

    async with aiohttp.ClientSession() as session:
        tasks = []
        for idx, url in enumerate(image_urls):
            filename = f"{hashtag}_{idx+1}.jpg"
            filepath = os.path.join(hashtag_dir, filename)
            tasks.append(download_image(session, url, filepath))

        await asyncio.gather(*tasks)
