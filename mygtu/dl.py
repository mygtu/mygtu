# not tested.

import aiohttp
import aiofiles
import asyncio
from datetime import datetime
from tqdm import tqdm
from .utils.time import time
from .utils.profile import __logo__, __info__, __version__
from .utils.constants import PATH

def total_url(urls):
    return int(len(urls))

def check_path(url):
    if "uploads" in url:
        path = PATH + url.split("/uploads/")[1].replace("/", "-")
    else:
        path = url.split("//")[1].replace("/", "-")
    return str(path)


async def downloader(url):
    async with aiofiles.open(check_path(url), 'wb') as mad:
          await mad.write(await fetch(url))

async def fetch(url):
    async with aiohttp.request("GET", url) as r:
        return await r.read()

async def main(urls):
    print(f'''
          {__logo__}
          starting download...''')
    for url in urls:
        start = datetime.now()
        await downloader(url),
        end = datetime.now()
        fin = (end - start)
        for i in tqdm(range(100), unit="KB"):
            pass
    print(f"downloaded in {(total_url(urls) * fin)} at {PATH}")
