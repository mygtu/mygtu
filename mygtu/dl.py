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
        path = PATH + "/" + url.split("/uploads/")[1].replace("/", "-")
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
    for url in urls:
        print(f'''
          {__logo__}
          starting download...''')
        start = datetime.now()
        await downloader(url),
        end = datetime.now()
        fin = (end - start)
        for i in tqdm(range(100), unit="KB"):
            pass

    # await write_info(url)
    print(f"downloaded in {(total_url() * fin)} at {PATH}")

# async def write_info(url):
#    info = f'''
#    {__logo__}
#    Total Files : {total_url()} 
#    Path : {check_path(url)}
#    info : {__info__}
#    version: {__version__}
#    [{time.current(strf="%m/%d/%Y, %H:%M:%S")}]
#    '''
#    async with aiofiles.open(PATH + "/info.txt", "w") as inf:
#        await inf.write(info)

async def download(urls):
    await main((urls))


