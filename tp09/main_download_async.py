import requests
from bs4 import BeautifulSoup
import time
import asyncio
import aiohttp

async def aiohttp_download_and_save(url,log_file):
    async with aiohttp.ClientSession() as session:
        url_log_file = f'{url}{log_file}'
        async with session.get(url_log_file) as response:
            with open(log_file,'w') as f:
                f.write(await response.text())

async def download_requests(url,log_file):
    loop = asyncio.get_event_loop()
    resp = await loop.run_in_executor(None, requests.get, url)
    content = resp.text
    # write content to file_name
    with open(log_file,'w') as f:
        f.write(content)
    
async def download_and_save(url,log_file):
    url_log_file = f'{url}{log_file}'
    response = requests.get(url_log_file)# ,verify=False
    with open(log_file,'w') as f:
        f.write(response.text)
    
async def main():
    all=[]
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_logs = [a['href'] for a in soup.find_all('a') if a['href'].endswith(".log")]
    print(all_logs)
    
    for log_file in all_logs:
        # all.append(download_and_save(url, log_file))
        # all.append(aiohttp_download_and_save(url, log_file))
        all.append(download_requests(url, log_file))
    
    r = await asyncio.gather(*all)


    
    end = time.perf_counter()
    print(f'{end-start:.2} s')
    
if __name__=='__main__':
    asyncio.run(main())
    # pip install "aiohttp[speedups]"
    
    
    
    
    