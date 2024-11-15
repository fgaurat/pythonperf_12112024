import requests
from bs4 import BeautifulSoup
import time
import threading

def download_and_save(url,log_file):
    url_log_file = f'{url}{log_file}'
    response = requests.get(url_log_file)
    with open(log_file,'w') as f:
        f.write(response.text)
    
def main():
    ths=[]
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_logs = [a['href'] for a in soup.find_all('a') if a['href'].endswith(".log")]
    print(all_logs)
    
    for log_file in all_logs:
        th = threading.Thread(target=download_and_save,args=(url,log_file))
        ths.append(th)
        th.start()
    
    [t.join() for t in ths]
    end = time.perf_counter()
    print(f'{end-start:.2} s')
    
if __name__=='__main__':
    main()
