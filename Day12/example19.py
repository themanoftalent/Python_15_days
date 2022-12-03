
import asyncio
import re
import time

import aiohttp

from pyquery import PyQuery as pq

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def parse(url):
    html = await fetch(url)
    doc = pq(html)
    title = doc('title').text()
    print('URL: %s => Title: %s' % (url, title))

def main():
    loop = asyncio.get_event_loop()
    urls = ['http://www.baidu.com', 'http://www.sina.com.cn', 'http://www.sohu.com', 'http://www.163.com']
    tasks = [parse(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    main()
