# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     proxyFetcher
   Description :
   Author :        JHao
   date：          2016/11/25
-------------------------------------------------
   Change Activity:
                   2016/11/25: proxyFetcher
-------------------------------------------------
"""
__author__ = 'JHao'

import datetime
import re
import json
from time import sleep

from bs4 import BeautifulSoup

from util.webRequest import WebRequest


class ProxyFetcher(object):
    """
    proxy getter
    """

    @staticmethod
    def freeProxy01():
        """
        站大爷 https://www.zdaye.com/dayProxy.html
        """
        start_url = "https://www.zdaye.com/dayProxy.html"
        html_tree = WebRequest().get(start_url, verify=False).tree
        latest_page_time = html_tree.xpath("//span[@class='thread_time_info']/text()")[0].strip()
        from datetime import datetime
        interval = datetime.now() - datetime.strptime(latest_page_time, "%Y/%m/%d %H:%M:%S")
        if interval.seconds < 300:  # 只采集5分钟内的更新
            target_url = "https://www.zdaye.com/" + html_tree.xpath("//h3[@class='thread_title']/a/@href")[0].strip()
            while target_url:
                _tree = WebRequest().get(target_url, verify=False).tree
                for tr in _tree.xpath("//table//tr"):
                    ip = "".join(tr.xpath("./td[1]/text()")).strip()
                    port = "".join(tr.xpath("./td[2]/text()")).strip()
                    yield "%s:%s" % (ip, port)
                next_page = _tree.xpath("//div[@class='page']/a[@title='下一页']/@href")
                target_url = "https://www.zdaye.com/" + next_page[0].strip() if next_page else False
                sleep(5)

    @staticmethod
    def freeProxy02():
        """
        代理66 http://www.66ip.cn/
        """
        url = "http://www.66ip.cn/"
        resp = WebRequest().get(url, timeout=10).tree
        for i, tr in enumerate(resp.xpath("(//table)[3]//tr")):
            if i > 0:
                ip = "".join(tr.xpath("./td[1]/text()")).strip()
                port = "".join(tr.xpath("./td[2]/text()")).strip()
                yield "%s:%s" % (ip, port)

    @staticmethod
    def freeProxy03():
        """ 开心代理 """
        target_urls = ["http://www.kxdaili.com/dailiip.html", "http://www.kxdaili.com/dailiip/2/1.html"]
        for url in target_urls:
            tree = WebRequest().get(url).tree
            for tr in tree.xpath("//table[@class='active']//tr")[1:]:
                ip = "".join(tr.xpath('./td[1]/text()')).strip()
                port = "".join(tr.xpath('./td[2]/text()')).strip()
                yield "%s:%s" % (ip, port)

    @staticmethod
    def freeProxy04():
        """ FreeProxyList https://www.freeproxylists.net/zh/ """
        url = "https://www.freeproxylists.net/zh/?c=CN&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=50"
        tree = WebRequest().get(url, verify=False).tree
        from urllib import parse

        def parse_ip(input_str):
            html_str = parse.unquote(input_str)
            ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', html_str)
            return ips[0] if ips else None

        for tr in tree.xpath("//tr[@class='Odd']") + tree.xpath("//tr[@class='Even']"):
            ip = parse_ip("".join(tr.xpath('./td[1]/script/text()')).strip())
            port = "".join(tr.xpath('./td[2]/text()')).strip()
            if ip:
                yield "%s:%s" % (ip, port)

    @staticmethod
    def freeProxy05(page_count=1):
        """ 快代理 https://www.kuaidaili.com """
        url_pattern = [
            'https://www.kuaidaili.com/free/inha/{}/',
            'https://www.kuaidaili.com/free/intr/{}/'
        ]
        url_list = []
        for page_index in range(1, page_count + 1):
            for pattern in url_pattern:
                url_list.append(pattern.format(page_index))

        for url in url_list:
            tree = WebRequest().get(url).tree
            proxy_list = tree.xpath('.//table//tr')
            sleep(1)  # 必须sleep 不然第二条请求不到数据
            for tr in proxy_list[1:]:
                yield ':'.join(tr.xpath('./td/text()')[0:2])

    @staticmethod
    def freeProxy06():
        """ 冰凌代理 https://www.binglx.cn """
        url = "https://www.binglx.cn/?page=1"
        try:
            tree = WebRequest().get(url).tree
            proxy_list = tree.xpath('.//table//tr')
            for tr in proxy_list[1:]:
                yield ':'.join(tr.xpath('./td/text()')[0:2])
        except Exception as e:
            print(e)

    @staticmethod
    def freeProxy07():
        """ 云代理 """
        urls = ['http://www.ip3366.net/free/?stype=1', "http://www.ip3366.net/free/?stype=2"]
        for url in urls:
            r = WebRequest().get(url, timeout=10)
            proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
            for proxy in proxies:
                yield ":".join(proxy)

    @staticmethod
    def freeProxy08():
        """ 小幻代理 """
        urls = ['https://ip.ihuan.me/address/5Lit5Zu9.html']
        for url in urls:
            r = WebRequest().get(url, timeout=10)
            proxies = re.findall(r'>\s*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*?</a></td><td>(\d+)</td>', r.text)
            for proxy in proxies:
                yield ":".join(proxy)

    @staticmethod
    def freeProxy09(page_count=1):
        """ 免费代理库 """
        for i in range(1, page_count + 1):
            url = 'http://ip.jiangxianli.com/?country=中国&page={}'.format(i)
            html_tree = WebRequest().get(url, verify=False).tree
            for index, tr in enumerate(html_tree.xpath("//table//tr")):
                if index == 0:
                    continue
                yield ":".join(tr.xpath("./td/text()")[0:2]).strip()

    @staticmethod
    def freeProxy10():
        """ 89免费代理 """
        r = WebRequest().get("https://www.89ip.cn/index_1.html", timeout=10)
        proxies = re.findall(
            r'<td.*?>[\s\S]*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})[\s\S]*?</td>[\s\S]*?<td.*?>[\s\S]*?(\d+)[\s\S]*?</td>',
            r.text)
        for proxy in proxies:
            yield ':'.join(proxy)

    @staticmethod
    def freeProxy11():
        """ 稻壳代理 https://www.docip.net/ """
        r = WebRequest().get("https://www.docip.net/data/free.json", timeout=10)
        try:
            for each in r.json['data']:
                yield each['ip']
        except Exception as e:
            print(e)

    # @staticmethod
    # def wallProxy01():
    #     """
    #     PzzQz https://pzzqz.com/
    #     """
    #     from requests import Session
    #     from lxml import etree
    #     session = Session()
    #     try:
    #         index_resp = session.get("https://pzzqz.com/", timeout=20, verify=False).text
    #         x_csrf_token = re.findall('X-CSRFToken": "(.*?)"', index_resp)
    #         if x_csrf_token:
    #             data = {"http": "on", "ping": "3000", "country": "cn", "ports": ""}
    #             proxy_resp = session.post("https://pzzqz.com/", verify=False,
    #                                       headers={"X-CSRFToken": x_csrf_token[0]}, json=data).json()
    #             tree = etree.HTML(proxy_resp["proxy_html"])
    #             for tr in tree.xpath("//tr"):
    #                 ip = "".join(tr.xpath("./td[1]/text()"))
    #                 port = "".join(tr.xpath("./td[2]/text()"))
    #                 yield "%s:%s" % (ip, port)
    #     except Exception as e:
    #         print(e)

    # @staticmethod
    # def freeProxy10():
    #     """
    #     墙外网站 cn-proxy
    #     :return:
    #     """
    #     urls = ['http://cn-proxy.com/', 'http://cn-proxy.com/archives/218']
    #     request = WebRequest()
    #     for url in urls:
    #         r = request.get(url, timeout=10)
    #         proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\w\W]<td>(\d+)</td>', r.text)
    #         for proxy in proxies:
    #             yield ':'.join(proxy)

    # @staticmethod
    # def freeProxy11():
    #     """
    #     https://proxy-list.org/english/index.php
    #     :return:
    #     """
    #     urls = ['https://proxy-list.org/english/index.php?p=%s' % n for n in range(1, 10)]
    #     request = WebRequest()
    #     import base64
    #     for url in urls:
    #         r = request.get(url, timeout=10)
    #         proxies = re.findall(r"Proxy\('(.*?)'\)", r.text)
    #         for proxy in proxies:
    #             yield base64.b64decode(proxy).decode()

    # @staticmethod
    # def freeProxy12():
    #     urls = ['https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1']
    #     request = WebRequest()
    #     for url in urls:
    #         r = request.get(url, timeout=10)
    #         proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
    #         for proxy in proxies:
    #             yield ':'.join(proxy)

    @staticmethod
    def freeProxyCustom1():
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

    @staticmethod
    def freeProxyCustom2():
        target_urls = [
            'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http_checked.txt'
            ]
        proxy_list = []
        for url in target_urls:
            text = WebRequest().get(url).text
            proxy_list += re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}",text)
            proxy_list = list(set(proxy_list))
        for proxy in proxy_list:
            yield proxy

    @staticmethod
    def freeProxyCustom3():
        target_urls = [
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
            'http://www.proxylists.net/http_highanon.txt'            
            ]
        proxy_list = []
        for url in target_urls:
            text = WebRequest().get(url).text
            proxy_list += re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}",text)
            proxy_list = list(set(proxy_list))
        for proxy in proxy_list:
            yield proxy

    @staticmethod
    def freeProxyCustom4():
        target_urls = [
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
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/all.txt",
            'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt',

            ]
        proxy_list = []
        for url in target_urls:
            text = WebRequest().get(url).text
            proxy_list += re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}",text)
            proxy_list = list(set(proxy_list))
        for proxy in proxy_list:
            yield proxy
                           
    @staticmethod
    def freeProxyCustom5():
        proxy_dict={'socks4':[],'socks5':[],'http':[]}
        for q in range(20):
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
                            proxy_dict['http'].append(i['addr'])
                        # if i['type'] == 4 :
                        #     proxy_dict['socks5'].append(i['addr'])
        
        # proxy_dict['socks4'] = list(set(proxy_dict['socks4']))
        # proxy_dict['socks5'] = list(set(proxy_dict['socks5']))
        proxy_dict['http'] = list(set(proxy_dict['http']))

        for proxy in proxy_dict['http'] :
            yield proxy
    @staticmethod
    def freeProxyCustom6():
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
            
    @staticmethod
    def freeProxyCustom7():
        target_urls = [
            'http://sslproxies.org',
            'http://free-proxy-list.net',
            "https://free-proxy-list.net/uk-proxy.html",
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
        for proxy in proxy_list:
            yield proxy

    @staticmethod
    def freeProxyCustom8():
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

    @staticmethod
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

if __name__ == '__main__':
    p = ProxyFetcher()
    for _ in p.freeProxy06():
        print(_)

# http://nntime.com/proxy-list-01.htm

# https://github.com/gitrecon1455/ProxyScraper/blob/main/scraper.py