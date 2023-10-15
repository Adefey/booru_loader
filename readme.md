# Simple Booru Loader
Allows you to download any images by their tags. Also can be used to creade datasets with image url and tags
## Examples
Here are some examples how to use this library
### Download 100 images with tags `amon_(atrolux)`, `kyra_(atrolux)` to folder `images`
```
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
```
### Download 100 images with tags `amon_(atrolux)`, `kyra_(atrolux)` and save in json formated as url:tags
```
import asyncio

from booru_api import get_url_tags

import json


async def main():
    # Download 100 images with tags `amon_(atrolux)`, `kyra_(atrolux)` and save in json formated as url:tags
    posts = await get_url_tags(
        tags=["amon_(atrolux)", "kyra_(atrolux)"], limit=100, page=1
    )
    with open("dataset.json", mode="w", encoding="UTF-8") as file:
        json.dump(posts, file, indent=4)


if __name__ == "__main__":
    asyncio.run(main())
```
### Download all images with tags `amon_(atrolux)`, `solo` to folder `images`
```
import asyncio

from booru_api import get_images_urls
from utils import download_image


async def main():
    # Download all images with tags `amon_(atrolux)`, `solo` to folder `images`
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
```
