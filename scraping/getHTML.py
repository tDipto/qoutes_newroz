import requests

http_proxy  = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy   = "ftp://10.10.1.10:3128"

proxies = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def fetchAndSaveToFile(url,path):
    # r = requests.get(url,proxies=proxies)
    r = requests.get(url, headers=headers)
    with open(path, 'w',encoding="utf-8") as f:
        f.write(r.text)

url = "https://www.goodreads.com/quotes"





fetchAndSaveToFile(url, "qoutes.html")