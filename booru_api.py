import requests
import aiohttp
import json
from urllib.parse import urljoin, urlencode, urlparse
import logging
import itertools

logging.basicConfig(level=logging.INFO)

from config import (
    E621_BASE_URL,
    POSTS_URL,
    TIMEOUT,
    USER_AGENT,
)


class ApiStatusException(Exception):
    pass


class ApiCriticalException(Exception):
    pass


async def execute_get_request(url: str, params: dict) -> dict:
    try:
        async with aiohttp.ClientSession() as session:
            logging.info(params)
            async with session.get(
                url, params=params, timeout=TIMEOUT, headers={"User-Agent": USER_AGENT}
            ) as resp:
                logging.info(f"url: {url}; params: {params}")
                response_text = await resp.text()
                status = resp.status
                if status != 200:
                    raise ApiStatusException(
                        f"Status: {status}; Response: {response_text}"
                    )
                response_json = json.loads(response_text)
                return response_json
    except Exception as exc:
        raise ApiCriticalException(f"Cannot perform request, error: {exc}") from exc


async def get_images_by_tags(
    tags: list[str] = None, limit: int = 50, page: int = 1
) -> list:
    if limit < 1:
        return []
    url = urljoin(E621_BASE_URL, POSTS_URL)
    tags_str = " ".join(tags)
    params = {"tags": tags_str, "limit": limit, "page": page}
    try:
        data = await execute_get_request(url, params)
    except ApiStatusException as exc:
        logging.error(f"Error getting posts: {exc}")
        return []
    except ApiCriticalException as exc:
        logging.error(f"Error performing request: {exc}")
        return []
    images = data["posts"]
    return images


async def get_images_urls(
    tags: list[str] = None, limit: int = 50, page: int = 1
) -> list[str]:
    data = await get_images_by_tags(tags, limit, page)
    urls = [entry["file"]["url"] for entry in data]
    return urls


async def get_url_tags(
    tags: list[str] = None, limit: int = 50, page: int = 1
) -> list[str]:
    data = await get_images_by_tags(tags, limit, page)
    data_with_tags = {entry["file"]["url"]: entry["tags"] for entry in data}
    return data_with_tags
