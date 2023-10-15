import aiohttp
import aiofiles
import os

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
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url, timeout=TIMEOUT, headers={"User-Agent": USER_AGENT}
            ) as resp:
                if resp.status != 200:
                    raise UtilsStatusException("Image download status is not 200")
                f = await aiofiles.open(os.path.join(folder, image_name), mode="wb")
                await f.write(await resp.read())
                await f.close()
    except Exception as exc:
        raise UtilsCriticalException(
            f"Cannot perform image download request: {repr(exc)}"
        ) from exc
