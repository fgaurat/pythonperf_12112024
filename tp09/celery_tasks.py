from celery import Celery
import requests

app = Celery('celery_tasks', broker='pyamqp://guest@localhost//', backend="rpc://")
# celery -A celery_tasks worker --loglevel=INFO -P solo

@app.task
def add(x, y):
    return x + y

@app.task
def download(url):
    response = requests.get(url)
    dict_tosave = {
        "content":response.text,
        "url":url
    }
    
    return dict_tosave

@app.task
def save(dict_tosave):
    log_file = dict_tosave['url'].split('/')[-1]
    content = dict_tosave['content']
    with open(log_file,'w') as f:
        f.write(content)
    