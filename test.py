from mygtu import dl, gf
import asyncio

async def main():
    db = gf.database()
    urls = gf.gather_url(db)
    await dl.download(urls)

asyncio.run(main())
