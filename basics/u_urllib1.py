import urllib.request
import urllib.parse
#x = urllib.request.urlopen('https://www.python.org/')
# print(f.read(100).decode('utf-8'))

#print(x.read().decode('utf-8'))
'''
url = 'http://pythonprogramming.net'

values ={'q':'basic'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

req = urllib.request.Request(url,data)

resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)

'''

try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')

    print(x.read())

except Exception as e:
    print(str(e))


try:
   url = 'https://www.google.com/search?q=test'

   headers = {}
   headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

#'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36' 

   req = urllib.request.Request(url,headers=headers)
   resp = urllib.request.urlopen(req)

   respData = resp.read()
#   print(respData)
   saveFile = open ('Webpage.txt','w')
   saveFile.write(str(respData))
   saveFile.close()
except Exception as e:
    print(str(e))
    


   

