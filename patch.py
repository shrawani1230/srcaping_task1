import requests 

dUrl = 'https://httpbin.org/patch'

dHeader = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'user-name' : "['arc']"

}
qResp = requests.patch(url = dUrl,headers = dHeader)

jResp = qResp.json()

print('qResp.content',jResp['headers'])


