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


async def download_requests(queue_download:asyncio.Queue,queue_save:asyncio.Queue):
    loop = asyncio.get_event_loop()
    while True:
        url,log_file = await queue_download.get()
        resp = await loop.run_in_executor(None, requests.get, url)
        content = resp.text
        dict_message = {
            'log_file':log_file,
            'content':content,
        }
        queue_save.put_nowait(dict_message)
        queue_download.task_done()

async def download(queue_download:asyncio.Queue,queue_save:asyncio.Queue):
    while True:
        url,log_file = await queue_download.get()
        async with aiohttp.ClientSession() as session:
            url_log_file = f'{url}{log_file}'
            async with session.get(url_log_file) as response:
                content = await response.text()
                dict_message = {
                    'log_file':log_file,
                    'content':content,
                }
                # queue_save.put_nowait(dict_message)
                await queue_save.put(dict_message)
        queue_download.task_done()
                
                
                
                
async def save(queue_save:asyncio.Queue):
    while True:
        dict_message = await queue_save.get()
        log_file = dict_message['log_file']
        content = dict_message['content']
        with open(log_file,'w') as f:
            f.write(content)
        queue_save.task_done()
    
async def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    #region truc
    queue_download = asyncio.Queue()
    queue_save = asyncio.Queue()
    nb_download_workers = 10
    nb_save_workers = 5
    #endregion
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_logs = [a['href'] for a in soup.find_all('a') if a['href'].endswith(".log")]
    
    tasks = []
    for i in range(nb_download_workers):
        task = asyncio.create_task(download(queue_download,queue_save))
        tasks.append(task)

    for i in range(nb_save_workers):
        task = asyncio.create_task(save(queue_save))
        tasks.append(task)
    
    
    for log_file in all_logs:
        t = url, log_file
        queue_download.put_nowait(t)
    
    await queue_download.join()
    await queue_save.join()
    
    [task.cancel() for task in tasks]
    
    
    end = time.perf_counter()
    print(f'{end-start:.2} s')
    
if __name__=='__main__':
    asyncio.run(main())
    # pip install "aiohttp[speedups]"
    
    
    
    
    