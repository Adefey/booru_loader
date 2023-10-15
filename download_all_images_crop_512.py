import asyncio
import os

from booru_api import get_images_urls
from utils import download_image, fit_to_size


async def main():
    # Download all images with tags `amon_(atrolux)`, `solo` to folder `images` and crop to 512x512
    posts = []
    for i in range(1, 700):
        new_posts = await get_images_urls(
            tags=["amon_(atrolux)", "solo"], limit=100, page=i
        )
        if not new_posts:
            break
        posts += new_posts
    folder = "images"
    coroutines = [download_image(post, folder=folder) for post in posts]
    await asyncio.gather(*coroutines)
    dimentions = (512, 512)
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            fit_to_size(filepath, dimentions)


if __name__ == "__main__":
    asyncio.run(main())
