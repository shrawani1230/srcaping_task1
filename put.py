import requests

qUrl = "https://httpbin.org/put"
qHeader = {
     'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'user-name' : "['tech]"

}
qresp = requests.put(url = qUrl,headers = qHeader)
jresp = qresp.json()
print('qresp.content',jresp['headers'])


