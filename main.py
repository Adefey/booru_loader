import asyncio

from booru_api import get_images_urls, get_url_tags


async def main():
    posts = await get_images_urls(
        tags=["amon_(atrolux)", "kyra_(atrolux)"], limit=2, page=1
    )
    print(*posts, sep="\n")
    print("\n")
    posts = await get_url_tags(
        tags=["amon_(atrolux)", "kyra_(atrolux)"], limit=2, page=1
    )
    print([f"{entry}:{posts[entry]}" for entry in posts], sep="\n")


if __name__ == "__main__":
    asyncio.run(main())
