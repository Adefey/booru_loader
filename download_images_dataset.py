import asyncio

from booru_api import get_url_tags

import json


async def main():
    # Download 100 images with tags "amon_(atrolux)", "kyra_(atrolux)"
    # and save in json formated as url:tags
    posts = await get_url_tags(
        tags=["amon_(atrolux)", "kyra_(atrolux)"], limit=100, page=1
    )
    with open("dataset.json", mode="w", encoding="UTF-8") as file:
        json.dump(posts, file, indent=4)


if __name__ == "__main__":
    asyncio.run(main())
