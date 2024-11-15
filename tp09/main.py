import requests
from bs4 import BeautifulSoup
import time

def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    # all_a = soup.find_all('a')
    # for a in all_a:
    #     # print(a.get('href'))
    #     print(a['href'])
    
    all_logs = [a['href'] for a in soup.find_all('a') if a['href'].endswith(".log")]
    print(all_logs)
    
    
    for log_file in all_logs:
        url_log_file = f'{url}{log_file}'
        response = requests.get(url_log_file)
        with open(log_file,'w') as f:
            f.write(response.text)

    end = time.perf_counter()
    print(f'{end-start:.2} s')
    
if __name__=='__main__':
    main()
