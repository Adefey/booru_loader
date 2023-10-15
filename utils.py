import aiohttp
import aiofiles
from aiofiles.os import makedirs
import os
from PIL import Image

from config import (
    TIMEOUT,
    USER_AGENT,
)


class UtilsStatusException(Exception):
    pass


class UtilsCriticalException(Exception):
    pass


async def download_image(url, folder="."):
    image_name = url[url.rfind("/") + 1 :]
    await makedirs(folder, exist_ok=True)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url, timeout=TIMEOUT, headers={"User-Agent": USER_AGENT}
            ) as resp:
                if resp.status != 200:
                    raise UtilsStatusException(
                        "Image download status is not 200"
                    )
                f = await aiofiles.open(
                    os.path.join(folder, image_name), mode="wb"
                )
                await f.write(await resp.read())
                await f.close()
    except Exception as exc:
        raise UtilsCriticalException(
            f"Cannot perform image download request: {repr(exc)}"
        ) from exc


def fit_to_size(image_path: str, size: tuple):
    image = Image.open(image_path)
    width, height = image.size
    lower_size = min(width, height)  # select to crop by minimal dimention
    left_crop = (width - lower_size) / 2
    top_crop = (height - lower_size) / 2
    right_crop = (width + lower_size) / 2
    bottom_crop = (height + lower_size) / 2
    # crop to center
    cropped_image = image.crop((left_crop, top_crop, right_crop, bottom_crop))
    resized_image = cropped_image.resize(size)
    resized_image.save(image_path)
