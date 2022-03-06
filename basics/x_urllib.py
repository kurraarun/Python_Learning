
import urllib3


#**********************
#pip install urllib3
#*****************

http = urllib3.PoolManager()
r = http.request('GET', 'https://www.online.citibank.co.in')
#r.status
print(r.status)
print(r.data)
