import re
from urllib import request


class Spider:
    url = 'https://www.panda.tv/cate/lol'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    nick_name_pattern = '<span class="video-nickname" title="([\s\S]*?)">'
    watch_number_pattern = '<span class="video-number"><i class="ricon ricon-eye"></i>([\s\S]*?)</span>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        html = re.findall(self.root_pattern, htmls)
        info_list = []
        for info in html:
            nick_name = re.findall(self.nick_name_pattern, info)
            watch_number = re.findall(self.watch_number_pattern, info)
            info_dict = {'nick_name': nick_name[0].strip(), 'watch_number': watch_number[0]}
            info_list.append(info_dict)
        return info_list

    def __refine(self, info_list):
        pass

    def __sort(self, info_list):
        return sorted(info_list, key=self.__sort_seed, reverse=True)

    def __sort_seed(self, info):
        r = re.findall('[\d+\.\d]*', info['watch_number'])
        number = float(r[0])
        if '万' in info['watch_number']:
            number = number * 10000
        return number

    def __show(self, info_list):
        for info in range(0, len(info_list)):
            print('主播：' + info_list[info]['nick_name'] + '                    观看人数:' + info_list[info]['watch_number'] +
                  '                    排行：' + str(info + 1))

    def go(self):
        htmls = self.__fetch_content()
        info_list = self.__analysis(htmls)
        info_list = self.__sort(info_list)
        self.__show(info_list)


spider = Spider()
spider.go()
