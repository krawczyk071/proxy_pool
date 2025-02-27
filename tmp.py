import datetime
from util.webRequest import WebRequest
from fetcher.proxyFetcher import ProxyFetcher
import re
from bs4 import BeautifulSoup

def freeProxy03():
    target_urls = ["http://www.kxdaili.com/dailiip.html", "http://www.kxdaili.com/dailiip/2/1.html"]
    for url in target_urls:
        tree = WebRequest().get(url).tree
        for tr in tree.xpath("//table[@class='active']//tr")[1:]:
            ip = "".join(tr.xpath('./td[1]/text()')).strip()
            port = "".join(tr.xpath('./td[2]/text()')).strip()
            yield "%s:%s" % (ip, port)

def freeProxy13():
    target_urls = [
        'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http_checked.txt'
        "https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=10000&country=all&simplified=true",
        "https://www.proxy-list.download/api/v1/get?type=http",
        'https://www.proxy-list.download/api/v1/get?type=https'
        "https://spys.me/proxy.txt",
        "https://api.openproxylist.xyz/http.txt",
        'https://openproxy.space/list/http',
        'https://proxyspace.pro/http.txt',
        'https://proxyspace.pro/https.txt',
        "https://sunny9577.github.io/proxy-scraper/generated/http_proxies.txt",
        'https://cdn.rei.my.id/proxy/HTTP',
        
        'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
        'https://github.com/monosans/proxy-list/raw/main/proxies/http.txt',
        'https://github.com/mmpx12/proxy-list/raw/master/http.txt',
        'https://github.com/mmpx12/proxy-list/raw/master/https.txt',
        'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
        'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt',
        'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
        'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt',
        'https://raw.githubusercontent.com/Noctiro/getproxy/master/file/http.txt',
        'https://raw.githubusercontent.com/Noctiro/getproxy/master/file/https.txt',
        'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt',
        'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/http.txt',
        'https://raw.githubusercontent.com/ArrayIterator/proxy-lists/main/proxies/http.txt',
        'https://raw.githubusercontent.com/ArrayIterator/proxy-lists/main/proxies/https.txt',
        'https://raw.githubusercontent.com/zenjahid/FreeProxy4u/master/http.txt',
        'https://raw.githubusercontent.com/Vann-Dev/proxy-list/main/proxies/http.txt',
        'https://raw.githubusercontent.com/Vann-Dev/proxy-list/main/proxies/https.txt',
        'https://raw.githubusercontent.com/tuanminpay/live-proxy/master/http.txt',
        'https://raw.githubusercontent.com/BreakingTechFr/Proxy_Free/main/proxies/http.txt',
        'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt',
        'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/https.txt',
        'https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt',
        'https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt',
        'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt',
        'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt',
        'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt',

        'https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt',
        'https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt',
        'https://raw.githubusercontent.com/berkay-digital/Proxy-Scraper/main/proxies.txt',
        'https://raw.githubusercontent.com/MrMarble/proxy-list/main/all.txt'
        ]
    proxy_list = []
    for url in target_urls:
        text = WebRequest().get(url).text
        proxy_list += re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}",text)
        proxy_list = list(set(proxy_list))
    for proxy in proxy_list:
        yield proxy
    # return proxy_list

        # r = requests.get(api,timeout=5)
        # if r.status_code == requests.codes.ok :
        #     proxy_list += re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}",r.text)
        #     proxy_dict[type] += list(set(self.proxy_list))

        # tree = WebRequest().get(url).tree
        # for tr in tree.xpath("//table[@class='active']//tr")[1:]:
        #     ip = "".join(tr.xpath('./td[1]/text()')).strip()
        #     port = "".join(tr.xpath('./td[2]/text()')).strip()
        #     yield "%s:%s" % (ip, port)

# x = ProxyFetcher.freeProxy11()

# x = next(x)
# print(x)

# y=freeProxy13()
# y = next(y)
# print(y)
# print(len(y))

# sources
# https://github.com/MuRongPIG/Proxy-Master/blob/main/getproxy.py


def freeProxyCustom7():
    target_urls = [
        'https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt',
        'https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt',
        'https://raw.githubusercontent.com/berkay-digital/Proxy-Scraper/main/proxies.txt',
        'https://raw.githubusercontent.com/MrMarble/proxy-list/main/all.txt'
        ]
    proxy_list = []
    for url in target_urls:
        text = WebRequest().get(url).text
        proxy_list += re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}",text)
        proxy_list = list(set(proxy_list))
    for proxy in proxy_list:
        yield proxy
        
def freeProxyCustom7div():
    target_urls = [f"https://freeproxy.lunaproxy.com/page/{i}.html" for i in range (1,2)]
    #duplicates on all pages
    proxies = []

    for url in target_urls:
        text = WebRequest().get(url).text

        soup = BeautifulSoup(text, "html.parser")
        table = soup.find("div", attrs={"class": "list"})
        for row in table.find_all("div"):
            count = 0
            proxy = ""
            for cell in row.find_all("div", attrs={"class": "td"}):
                if count == 2:
                    break
                proxy += cell.text+":"
                count += 1
            proxy = proxy.rstrip(":")
            if proxy != "":
                proxies.append(proxy)

    proxy_list = list(set(proxies))
    for proxy in proxy_list:
        yield proxy

def freeProxyCustom7table():
    target_urls = [
        'http://sslproxies.org',
        'http://free-proxy-list.net',
        "http://us-proxy.org",
        "http://socks-proxy.net",
        
        ]
    proxies = set()

    for url in target_urls:
        text = WebRequest().get(url).text

        soup = BeautifulSoup(text, "html.parser")
        table = soup.find("table", attrs={"class": "table table-striped table-bordered"})
        for row in table.find_all("tr"):
            count = 0
            proxy = ""
            for cell in row.find_all("td"):
                if count == 1:
                    proxy += ":" + cell.text.replace("&nbsp;", "")
                    proxies.add(proxy)
                    break
                proxy += cell.text.replace("&nbsp;", "")
                count += 1

    proxy_list = list(proxies)  
    print(len(proxy_list))
    for proxy in proxy_list:
        yield proxy

def freeProxyCustom7url():
    target_urls = []
    methods=['http','https']
    anons=['elite','anonymous','transparent']
    for method in methods:
        for anon in anons:
            url = f"https://www.proxy-list.download/api/v1/get?type={method}&anon={anon}"
            target_urls.append(url)
    proxy_list = []
    for url in target_urls:
        text = WebRequest().get(url).text
        proxy_list += re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}",text)
        proxy_list = list(set(proxy_list))
    for proxy in proxy_list:
        yield proxy 

def freeProxyCustom9():
    target_urls = ["https://proxy11.com"
        
        ]
    proxies = []

    for url in target_urls:
        text = WebRequest().get(url).text

        soup = BeautifulSoup(text, "html.parser")
        tbody = soup.find("tbody")
        tr = tbody.find_all("tr")

        for td in tr:
            tds = td.find_all("td")
            ip = tds[0].text
            port = tds[1].text
            px= f"{ip}:{port}"
            proxies.append(px)

    proxy_list = list(set(proxies))  
    for proxy in proxy_list:
        yield proxy



def get_extra():
    proxy_dict={'socks4':[],'socks5':[],'http':[]}
    for q in range(20):
        # count = {'http':0,'socks5':0}
        day = datetime.date.today() + datetime.timedelta(-q)
        r = WebRequest().get('https://checkerproxy.net/api/archive/{}-{}-{}'.format(day.year,day.month,day.day))
        if r.text != '[]': 
            json_result = r.json
            for i in json_result:
                if re.match(r"172\.*\.*\.*",i['ip']):
                    if i['type'] in [1,2] and i['addr'] in proxy_dict['http']:
                        proxy_dict['http'].remove(i['addr'])
                    # if i['type'] == 4 and i['addr'] in proxy_dict['socks5']:
                    #     proxy_dict['socks5'].remove(i['addr'])
                else:
                    if i['type'] in [1,2] :
                        # count['http'] += 1
                        proxy_dict['http'].append(i['addr'])
                    # if i['type'] == 4 :
                    #     count['socks5'] += 1
                    #     proxy_dict['socks5'].append(i['addr'])
    
    # proxy_dict['socks4'] = list(set(proxy_dict['socks4']))
    # proxy_dict['socks5'] = list(set(proxy_dict['socks5']))
    proxy_dict['http'] = list(set(proxy_dict['http']))
    for proxy in proxy_dict['http'] :
        yield proxy
    # return proxy_dict['http']

y = freeProxyCustom9()
y = next(y)

print(y)