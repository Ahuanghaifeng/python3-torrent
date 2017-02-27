from bs4 import BeautifulSoup
import re
import urllib.parse


class HtmlParser(object):

    # 解析种子文件
    def parserTwo(self,html):
        if html is None:
            return
        soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
        res_datas = self._get_data(soup)
        return res_datas

    # 将种子文件的标题，磁力链接和迅雷链接进行封装
    def _get_data(self,soup):
        res_datas = []
        all_data = soup.findAll('a',href=re.compile(r"/detail"))
        all_data2 = soup.findAll('a', href=re.compile(r"magnet"))
        all_data3 = soup.findAll('a',href=re.compile(r"thunder"))
        for i in range(len(all_data)):
            res_data = {}
            res_data['title'] = all_data[i].get_text()
            res_data['cl'] = all_data2[i].get('href')
            res_data['xl'] = all_data3[i].get('href')
            res_datas.append(res_data)
        return res_datas