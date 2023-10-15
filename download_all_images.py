import asyncio

from booru_api import get_images_urls
from utils import download_image


async def main():
    # Download 100 images with tags "amon_(atrolux)", "kyra_(atrolux)"
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


if __name__ == "__main__":
    asyncio.run(main())
