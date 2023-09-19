# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import re

pattern_day10_13 = re.compile('일급 1[0-3]')
pattern_month10_13 = re.compile('월급 1[0-3]')
pattern_ildao = re.compile('일다오')
pattern_day10_15 = re.compile('일급 1[0-5]')
pattern_month10_15 = re.compile('월급 1[0-5]')
pattern_system = re.compile('비계/동바리')
pattern_nego = re.compile('협의')
pattern_null = re.compile('null')

class IldaoTestWithSeleniumPipeline:
    def process_item(self, item, spider):
        if len(pattern_day10_13.findall(item['pay'])) > 0:  # '일급 10 ~ 14' 들어가면 다 뺌
            raise DropItem('\n\nDrop 일급 10 ~ 13 ! 🚯\n')
        elif len(pattern_month10_13.findall(item['pay'])) > 0:  # '월급 10 ~ 14' 들어가면 다 뺌
            raise DropItem('\n\nDrop 월급 10 ~ 13 ! 🚯\n')
        elif item['title'].find('일다오') != -1:    # str.find('문자열') 찾았으면 0 ~ 찾은 첫번째 인댁스 / 못찾았으면 -1 반환
            raise DropItem('\n\nDrop title : 일다오 🚯\n')
        elif len(pattern_ildao.findall(item['detail'])) > 0: # 일부러 str.find와 다르게 해봄
            raise DropItem('\n\nDrop detail : 일다오 🚯\n')
        elif len(item['detail']) < 32: # detail 32자 미만은 빼
            raise DropItem('\n\nDrop detail : 32자 미만 🚯\n')
        elif len(item['title']) < 6: # title 6자 미만은 빼
            raise DropItem('\n\nDrop title : 6자 미만 🚯\n')
        elif (len(pattern_day10_15.findall(item['pay'])) > 0 or len(pattern_month10_15.findall(item['pay'])) > 0) and len(pattern_system.findall(item['type'])) > 0 and item['site'].find('부산') == -1 and item['site'].find('서울') == -1:
            raise DropItem('\n\nDrop 비계/동바리 이면서 단가 15이하 (부산, 서울 제외) 🚯\n')
        elif len(pattern_nego.findall(item['pay'])) > 0 and len(pattern_system.findall(item['type'])) > 0 and item['site'].find('부산') == -1 and item['site'].find('서울') == -1:
            raise DropItem('\n\nDrop 비계/동바리 이면서 협의 (부산, 서울 제외) 🚯 \n')
        elif len(pattern_null.findall(item['site'])) > 0:   # site 에 null 이 들어가면 빼
            raise DropItem('\n\nDrop site : null 🚯\n')
        else:
            return item

# 중복제거
class DuplicatesPipeline:
    def __init__(self):
        self.title_set = set()
        self.phone_set = set()
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter["title"] in self.title_set:
            raise DropItem(f"\n\nDuplicate item (TITLE) found  ♻️ : \n\n{item!r}\n")
        elif adapter["phone"] in self.phone_set:
            raise DropItem(f"\n\nDuplicate item (PHONE) found  ♻️ : \n\n{item!r}\n")
        else:
            self.title_set.add(adapter["title"])
            self.phone_set.add(adapter['phone'])
            return item

# 본문에 '♧일다오 지원하기를 이용해주세요♧' 뺌!!!
# 인원 숫자만 가져와 더해준다. 0 인경우 0명 표기 함!!!
# pay  , 단위 고침!!!
# 조공/보조  고침!!!
# '비계/동바리' 15만원 이하 뺌!!!