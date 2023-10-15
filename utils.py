import aiohttp
import aiofiles
import os


class UtilsStatusException(Exception):
    pass


class UtilsCriticalException(Exception):
    pass


async def download_image(url, folder="."):
    image_name = url[url.rfind("/") + 1 :]
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    raise UtilsStatusException("Status is not 200")
                f = await aiofiles.open(os.path.join(folder, image_name), mode="wb")
                await f.write(await resp.read())
                await f.close()
    except Exception as exc:
        raise UtilsCriticalException(f"Cannot perform request: {exc}") from exc
