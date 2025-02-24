ProxyPool Crawler Proxy IP Pool
=======
[![Build Status](https://travis-ci.org/jhao104/proxy_pool.svg?branch=master)](https://travis-ci.org/jhao104/proxy_pool)
[![](https://img.shields.io/badge/Powered%20by-@j_hao104-green.svg)](http://www.spiderpy.cn/blog/)
[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg)](https://github.com/jhao104/proxy_pool/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/jhao104/proxy_pool.svg)](https://github.com/jhao104/proxy_pool/graphs/contributors)
[![](https://img.shields.io/badge/language-Python-green.svg)](https://github.com/jhao104/proxy_pool)

    ______                        ______             _
    | ___ \_                      | ___ \           | |
    | |_/ / \__ __   __  _ __   _ | |_/ /___   ___  | |
    |  __/|  _// _ \ \ \/ /| | | ||  __// _ \ / _ \ | |
    | |   | | | (_) | >  < \ |_| || |  | (_) | (_) || |___
    \_|   |_|  \___/ /_/\_\ \__  |\_|   \___/ \___/ \_____\
                           __ / /
                          /___ /

### ProxyPool

A crawler proxy IP pool project whose main function is to periodically collect free proxies published online, validate them before storing, and continuously check stored proxies to ensure their availability. It provides both API and CLI usage methods. You can also extend the proxy sources to improve the quality and quantity of the proxy pool.

* Documentation: [document](https://proxy-pool.readthedocs.io/zh/latest/) [![Documentation Status](https://readthedocs.org/projects/proxy-pool/badge/?version=latest)](https://proxy-pool.readthedocs.io/zh/latest/?badge=latest)

* Supported Versions:
[![](https://img.shields.io/badge/Python-2.7-green.svg)](https://docs.python.org/2.7/)
[![](https://img.shields.io/badge/Python-3.5-blue.svg)](https://docs.python.org/3.5/)
[![](https://img.shields.io/badge/Python-3.6-blue.svg)](https://docs.python.org/3.6/)
[![](https://img.shields.io/badge/Python-3.7-blue.svg)](https://docs.python.org/3.7/)
[![](https://img.shields.io/badge/Python-3.8-blue.svg)](https://docs.python.org/3.8/)
[![](https://img.shields.io/badge/Python-3.9-blue.svg)](https://docs.python.org/3.9/)
[![](https://img.shields.io/badge/Python-3.10-blue.svg)](https://docs.python.org/3.10/)
[![](https://img.shields.io/badge/Python-3.11-blue.svg)](https://docs.python.org/3.11/)

* Test Address: http://demo.spiderpy.cn (Please do not overload the server, thanks)

* Recommended Paid Proxy: [luminati-china](https://get.brightdata.com/github_jh). BrightData (formerly known as Luminati) is considered the market leader in proxy services, covering 72 million IPs worldwide, mostly real residential IPs, with high success rates. Various paid plans are available. If you need high-quality proxy IPs, register and contact the Chinese customer service. [Apply for a free trial](https://get.brightdata.com/github_jh) (currently offering a 50% discount). (PS: If you are unsure how to use it, refer to this [tutorial](https://www.cnblogs.com/jhao/p/15611785.html)).

### Running the Project

##### Download Code:

* Clone using git:
```bash
git clone git@github.com:jhao104/proxy_pool.git
```

* Download from releases:
```bash
https://github.com/jhao104/proxy_pool/releases (download the corresponding zip file)
```

##### Install Dependencies:
```bash
pip install -r requirements.txt
```

##### Update Configuration:
```python
# setting.py is the project configuration file

# API service configuration
HOST = "0.0.0.0"  # IP
PORT = 5000  # Listening port

# Database configuration
DB_CONN = 'redis://:pwd@127.0.0.1:8888/0'

# ProxyFetcher configuration
PROXY_FETCHER = [
    "freeProxy01",  # These are the enabled proxy fetch methods, all fetch methods are in fetcher/proxyFetcher.py
    "freeProxy02",
    # ....
]
```

#### Start the Project:
```bash
# If all dependencies are installed, start the project using proxyPool.py
# The program consists of two parts: schedule (scheduler) and server (API service)

# Start the scheduler
python proxyPool.py schedule

# Start the web API service
python proxyPool.py server
```

### Docker Image
```bash
docker pull jhao104/proxy_pool

docker run --env DB_CONN=redis://:password@ip:port/0 -p 5010:5010 jhao104/proxy_pool:latest
```

### Using docker-compose
Run the following command in the project directory:
```bash
docker-compose up -d
```

### Usage

* API
After starting the web service, the default configuration enables an API service at http://127.0.0.1:5010:

| API | Method | Description | Params |
| ---- | ---- | ---- | ---- |
| / | GET | API Introduction | None |
| /get | GET | Get a random proxy | Optional: `?type=https` to filter HTTPS proxies |
| /pop | GET | Get and remove a proxy | Optional: `?type=https` to filter HTTPS proxies |
| /all | GET | Get all proxies | Optional: `?type=https` to filter HTTPS proxies |
| /count | GET | Check proxy count | None |
| /delete | GET | Delete a proxy | `?proxy=host:ip` |

For further details, refer to the full translated document.

