## Working in it!



<h2 align="center"> MAO _ PROXY </h2>
<h3>VERSION : 0.1 </h3>

[![Author](https://img.shields.io/badge/Author-MAO2116-blue)](https://github.com/mao2116)
[![Language](https://img.shields.io/badge/Written%20in-Python3-blue)](#)
[![Opensource](https://img.shields.io/badge/Open%20Source-Yes-green)](#)


**THE MAIN AUTHOR OF THIS CODE MAO2116**

#### REQUIREMENTS
* `PYTHON >=3.9.X+`
##### PIP MODULE 
* `REQUESTS`

#### INSTALLATION 
```bash
  pip3 install mproxy 
  ```
#### IMPORT MODULE

```python
from mproxy import proxy

```

#### USE OF mproxy FUNCTION

```python
proxy.mproxy(type="")

```
##### Here type mean your security method of your url it contains 4 types of security method `http,https,socks5 and all`

#### Example Code Of Using This Tool
#### Just a ip printer

```python 
from mproxy import proxy
proxy.mproxy(type="https")

```

#### Realtime Example

```python 
import requests
from mproxy import proxy
ip_addresses = proxy.mproxy(type="http")

def proxy_request(url):
   while True:
      try:
        proxy = random.randint(0, len(ip_addresses) - 1)
        proxies = {"http": ip_addresses(proxy), "https": ip_addresses(proxy)}
        response = requests.get(url, proxies=proxies, timeout=30)
        print(f"Proxy currently being used: {proxy}")
      except:
         print("Error, looking for another proxy")
proxy_requests("http://yoururl.com/")
```

<b>Copyright (c) 2021 MAO-COMMUNITY Under <a href="https://raw.githubusercontent.com/mao2116/mmail/main/LICENSE">MIT LICENSE</a></b>

<div align="center">
<b> GET US IN CLICK </b><br><br>
<a href="https://github.com/mao2116">
  <img width="50px" height="50px" src="https://raw.githubusercontent.com/fh-rabbi/Hack-Box/main/images/git.png">
</a>
<a href="https://www.facebook.com/mao2116/">
  <img width="50px" height="50px" src="https://raw.githubusercontent.com/fh-rabbi/Hack-Box/main/images/fb.png"><!I JUST USE A PIC FROM FH-RABBI >
</a>
</div>  
