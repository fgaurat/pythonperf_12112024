from celery import Celery,signature,chain,group
from bs4 import BeautifulSoup

import requests



def main():
    app = Celery('celery_tasks', broker='pyamqp://guest@localhost//', backend="rpc://")
    result = app.send_task("celery_tasks.add",  args=[2,5])
    print(result.get())
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_logs = [url+a['href'] for a in soup.find_all('a') if a['href'].endswith(".log")]
    
    # download = signature('celery_tasks.download')
    # r = download.delay(all_logs[0])
    # print(r.get())
    
    # #Download
    # download_tasks = [signature('celery_tasks.download',args=[url]) for url in logs]
    # download_group =group(download_tasks)
    # result = download_group()
    # all_downloads = result.get()

    # #Save
    # save_tasks = [signature('celery_tasks.save',args=[to_save]) for to_save in all_downloads]
    # save_group =group(save_tasks)
    # save_group()    
    for url in all_logs:
        chain(
        signature('celery_tasks.download',args=[url]),
        signature('celery_tasks.save')
    )()      
if __name__=='__main__':
    main()
