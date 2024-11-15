import requests
from bs4 import BeautifulSoup
import time
import threading
import concurrent.futures

def download_and_save(url,log_file):
    url_log_file = f'{url}{log_file}'
    response = requests.get(url_log_file)
    with open(log_file,'w') as f:
        f.write(response.text)
    
def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_logs = [a['href'] for a in soup.find_all('a') if a['href'].endswith(".log")]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_and_save,[url]*len(all_logs),all_logs)
        # executor.submit(download_and_save,args=(url,log))


    # with ThreadPoolExecutor(max_workers=5) as executor:
    #     futures = [executor.submit(download_and_save, log_file, url) for log_file in all_logs]
    #     for future in futures:
    #         future.result()
            
    
    end = time.perf_counter()
    print(f'{end-start:.2} s')
    
if __name__=='__main__':
    main()
