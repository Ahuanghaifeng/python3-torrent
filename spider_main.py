import url_manager
import html_downloader
import html_parser
import html_outputer
from urllib.parse import quote

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()


    def parser(self, root_url):
        html = self.downloader.download(root_url)
        datas = self.parser.parserTwo(html)
        self.outputer.output_html3(datas)


if __name__ == '__main__':
    url = "http://www.btany.com/search/桃谷绘里香-first-asc-1"
    # 解决中文搜索问题 对于：？=不进行转义
    root_url = quote(url,safe='/:?=')
    obj_spider = SpiderMain()
    obj_spider.parser(root_url)


