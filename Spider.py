#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scrapy
from mySpider.items import ItcastItem
# 创建一个爬虫类
class ItcastSpider(scrapy.Spider):
    # 爬虫名
    name = "itcast"
    # 允许爬虫作用的范围
    allowd_domains = ["http://www.itcast.cn/"]
    # 爬虫起始的url
    start_urls = [
        "http://www.itcast.cn/channel/teacher.shtml#",
    ]
    def parse(self, response):
        teacher_list = response.xpath('//div[@class="li_txt"]')
        # 所有老师信息的列表集合
        teacherItem = []
        # 遍历根节点集合
        for each in teacher_list:
            # Item对象用来保存数据的
            item = ItcastItem()
            # name, extract() 将匹配出来的结果转换为Unicode字符串
            # 不加extract() 结果为xpath匹配对象
            name = each.xpath('./h3/text()').extract()
            # title
            title = each.xpath('./h4/text()').extract()
            # info
            info = each.xpath('./p/text()').extract()
            item['name'] = name[0].encode("gbk")
            item['title'] = title[0].encode("gbk")
            item['info'] = info[0].encode("gbk")
            teacherItem.append(item)
        return teacherItem