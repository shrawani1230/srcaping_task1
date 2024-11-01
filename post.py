import requests

qUrl = "https://httpbin.org/post"
qHeader = {
     'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'user-name' : "['arc',vigo]"

}
qresp = requests.post(url = qUrl,headers = qHeader)
jresp = qresp.json()
print('qresp.content',jresp['headers'])

