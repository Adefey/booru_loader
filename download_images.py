import asyncio

from booru_api import get_images_urls
from utils import download_image


async def main():
    # Download 100 images with tags `amon_(atrolux)`, `kyra_(atrolux)` to folder `images`
    posts = await get_images_urls(
        tags=["amon_(atrolux)", "kyra_(atrolux)"], limit=100, page=1
    )
    folder = "images"
    coroutines = [download_image(post, folder=folder) for post in posts]
    await asyncio.gather(*coroutines)


if __name__ == "__main__":
    asyncio.run(main())
