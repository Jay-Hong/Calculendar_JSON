import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re; import time; import random
from ildao_test_with_selenium.items import IldaoTestWithSeleniumItem
#~/Documents/Calculendar_JSON/ildao_test_with_selenium/ildao_test_with_selenium/spiders/ildao_multi.py
class IldaoMultiSpider(scrapy.Spider):
    
    dotdcom = "o.com/r"
    recrudit = "ecruit"
    ilbdao = "lda"

    name = "ildao_multi"
    allowed_domains = ["i"+ilbdao+"o.com"]
    start_urls = ["https://i"+ilbdao+dotdcom+recrudit]

    USER_AGENTS = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Whale/3.20.182.12 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15e148 Kakaotalk 9.5.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15e148 Safari/604.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/71.0.3578.89 Mobile/15E148 Safari/605.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/94.0.4606.52 Mobile/15e148 Safari/604.1',
        'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG-SM-G950N/KSU3CRJ1 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/8.2 Chrome/63.0.3239.111 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 11; SM-A908N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 13; SM-S918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 13; SM-S911) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 13; SM-S916) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 13; SM-S901) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 13; SM-S906) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 13; SM-S908) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36'
    ]
    
    WINDOW_SIZES = [
        'window-size=1920x1080',
        'window-size=1400x800',
        'window-size=3066x1330',
        'window-size=3620x1600',
        'window-size=2930x1440',
        'window-size=1390x1280',
        'window-size=2375x1240',
        'disable-gpu'
    ]

    LANG = [
        'lang=ko_KR',
        'lang=en_US',
        'lang=ko_KR',
        'lang=ja_JP',
        'lang=ko_KR',
        'lang=zh-CN',
        'lang=ko_KR'
    ]

    def __init__(self):
        headlessoptions = webdriver.ChromeOptions()
        headlessoptions.add_argument('headless')
        headlessoptions.add_argument(random.choice(IldaoMultiSpider.LANG))
        headlessoptions.add_argument(random.choice(IldaoMultiSpider.WINDOW_SIZES))
        headlessoptions.add_argument(f"User-Agent: {random.choice(IldaoMultiSpider.USER_AGENTS)}")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=headlessoptions)
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(random.randint(2, 5))
        # time.sleep(2)

        # ildao_items 가져오기
        ildao_items = self.driver.find_elements(By.CSS_SELECTOR, "div.scrollsection > div.box.pointer")

        for i in range(88):
            try:
                print(f"목록가져오기{i} : {ildao_items[-1].location_once_scrolled_into_view}")
            except Exception as e:
                print('\n\n - - - - - - - - 목록가져오기 예외처리 됨 !! - - - - - - - - \n\n')
                time.sleep(random.randint(3, 7))
                # time.sleep(2.2)
            else:
                time.sleep(random.randint(3, 7))
                # time.sleep(2.2)
                ildao_items = self.driver.find_elements(By.CSS_SELECTOR, "div.scrollsection > div.box.pointer")

        # ildao_items의 '간편지원' 값을 확인하기위해 'simple_text_items'에 해당 값을 담는다
        first_no_simple = 0
        simple_text_items = list()  # '간편지원>' 구분 가능한 문자 리스트
        simple_items = self.driver.find_elements(By.CSS_SELECTOR, "div.scrollsection > div.box.pointer div.scrap_wrap.ft12.col_ora01")
        for index, simple_item in enumerate(simple_items):
            simple_text_items.append(simple_item.text.split('\n')[0])
            
        # 첫번째 '간편지원'이 아닌 값을 'first_no_simple'에 저장
        for index, simple_text_item in enumerate(simple_text_items):    # '간편지원' 이 아닌 첫번재 값 구함
            if first_no_simple == 0 and simple_text_item.find('D-') == -1 and simple_text_item.find('간편지원') == -1 and simple_text_item.find('상시') == -1:
                first_no_simple = index

        print(f"\nfirst_no_simple : [{first_no_simple}]\n")# 간편지원 아닌 index 출력

        pattern_day10_17 = re.compile('일급 1[0-7]')
        pattern_month10_17 = re.compile('월급 1[0-7]')
        pattern_nego = re.compile('협의')
        pattern_day10_16 = re.compile('일급 1[0-6]')
        pattern_month10_16 = re.compile('월급 1[0-6]')
        pattern_system = re.compile('비계/동바리')
        pattern_seoul = re.compile('서울')

        # 간편지원 아닌 첫 index로 이동 (일반 17만원 이상 '비계/동바리'는 18만원 이상 가져오기)
        print(f"중단가기  : {ildao_items[first_no_simple].location_once_scrolled_into_view}")
        time.sleep(random.randint(2, 5))
        # time.sleep(2)
        for index, job_item in enumerate(ildao_items):
            if index >= first_no_simple and simple_text_items[index].find('간편지원') == -1:
                try:
                    job_item.location_once_scrolled_into_view
                    time.sleep(random.randint(1, 4));job_item.click();time.sleep(.5)
                    # time.sleep(.3);job_item.click();time.sleep(.3)
                    
                    title_sel = self.driver.find_element(By.CSS_SELECTOR, "#detail_info div.ft5.NotoSansM")
                    title_pre = re.sub('[^a-zA-Z0-9가-힣一-龥_\s\(\)\[\]\-\~\/\,\.\ㆍ\&]', ' ', title_sel.text)
                    title = re.sub('\s{2,9}', ' ', title_pre).strip(' _-~/,.ㆍ&').lstrip(')]').rstrip('([').upper()

                    site_sel = self.driver.find_element(By.CSS_SELECTOR, "div.time.ft11.col_gra04.NotoSansL")
                    site_pre = re.sub('[a-z]+_[a-z]+\s', '', site_sel.text) # "location_on " 없애기
                    site = re.sub('세종 세종', '세종시', site_pre)
    
                    type_sel = self.driver.find_element(By.CSS_SELECTOR, "#detail_info div.ft11 div.ft10")
                    type_pre = re.sub('조공/잡부', '조공/보조', type_sel.text)
                    type = re.sub('시스템/비계', '비계/동바리', type_pre)
    
                    pay_sel = self.driver.find_element(By.CSS_SELECTOR, "#detail_info div.col_blu02.ft10 > div")
                    pay_pre1 = re.sub('\n', ' ', re.sub('0 원', '0원', pay_sel.text))
                    pay_pre2 = re.sub('0,000', '만', pay_pre1)
                    if pay_pre2.find(',000') == -1:
                        pay = re.sub(',', '', pay_pre2)
                    else:
                        pay = re.sub('', '', pay_pre2)
    
                    etcs_sel = self.driver.find_elements(By.CSS_SELECTOR, "#detail_info div.ft11.col_blu02")

                    etc1 = '';etc2 = '';etc3 = ''
                    etc_set = set()
                    for etc in etcs_sel:
                        etc_set.add(etc.text.strip(','))

                    if '숙식제공' in etc_set:
                        etc1 = '숙식제공'
                        if '4대보험' in etc_set:
                            etc2 = '4대보험'
                            if '출퇴근가능' in etc_set:
                                etc3 = '출퇴근가능'
                            elif '장기근무' in etc_set:
                                etc3 = '장기근무'
                        elif '출퇴근가능' in etc_set:
                           etc2 = '출퇴근가능'
                           if '장기근무' in etc_set:
                              etc3 = '장기근무'
                        elif '장기근무' in etc_set:
                           etc2 = '장기근무'
                    elif '4대보험' in etc_set:
                        etc1 = '4대보험'
                        if '출퇴근가능' in etc_set:
                           etc2 = '출퇴근가능'
                           if '장기근무' in etc_set:
                                 etc3 = '장기근무'
                        elif '장기근무' in etc_set:
                            etc2 = '장기근무'
                    elif '출퇴근가능' in etc_set:
                        etc1 = '출퇴근가능'
                        if '장기근무' in etc_set:
                            etc2 = '장기근무'
                    elif '' in etc_set:
                        etc1 = '장기근무'

                    numpeople_int = 0;numpeople_pre = 0
                    num_pattern = re.compile('[0-9]')
                    numpeople_sel_list = self.driver.find_elements(By.CSS_SELECTOR, "#detail_info div.ft11 div.ft10[style='display: flex;']")
                    for numpeople_sel in numpeople_sel_list:
                        if len(num_pattern.findall(numpeople_sel.text)) > 0:    # 숫자가 들어있는 문자열만 가져온다
                            numpeople_int = re.sub('[^0-9]', '', numpeople_sel.text)    # 숫자를 제외한 문자 삭제
                            #print(f"numpeople_int : {numpeople_int}")
                            numpeople_pre += int(numpeople_int)                 # 초보+조공+준공+기공 = 총인원
                    numpeople = f"{numpeople_pre}명"
    
                    phone_sel = self.driver.find_element(By.CSS_SELECTOR, "#detail_info div.ft11 div.ft10.RobotoM")
                    phone = re.sub('', '', phone_sel.text)
    
                    detail_sel = self.driver.find_element(By.CSS_SELECTOR, "#detail_info p.ft10.lin_h2")
                    detail_pre1 = re.sub('\n\n\n\n+', '\n\n\n', detail_sel.text)
                    detail_pre2 = re.sub(' *\*\) *', '\n• ', re.sub(' *\*\] *', '\n• ', detail_pre1)) # 특정 소개소 detail 작성 양식 때문에 바꿔줌 '*]타일용접' (나중에 없애도 됨)
                    detail_pre3 = re.sub(' *\#\)', '◎', re.sub(' *\#\]', '◎', detail_pre2))
                    detail_pre4 = re.sub(' *\@\)', '◎', re.sub(' *\@\]', '◎', detail_pre3))
                    detail_pre5 = re.sub('잇', '있',re.sub('업슴', '없음',re.sub('잇슴', '있음', detail_pre4)))
                    detail_pre6 = re.sub('\n\n\n+', '\n\n',re.sub('//', '/',re.sub('\n {1,9}', '/', detail_pre5)))
                    if detail_pre6.find('• ') != -1:
                        detail = re.sub('', '', detail_pre6)
                    else:
                        detail = re.sub('', '', detail_pre1)
                
                    imageURL_sel = '';imageURL = ''
                    try:
                        imageURL_sel = self.driver.find_element(By.CSS_SELECTOR, "#detail_info > div > div > div > div > img")
                    except Exception as e:
                        imageURL = ''
                    else:
                        imageURL = imageURL_sel.get_attribute('src')
                
                    # '시스템비계는 10~17'뺌 / '시스템비계 아니면 10~16뺌' / '협의'뺌
                    if ((len(pattern_system.findall(type)) > 0 and len(pattern_day10_17.findall(pay)) == 0 and len(pattern_month10_17.findall(pay)) == 0) or (len(pattern_system.findall(type)) == 0 and len(pattern_day10_16.findall(pay)) == 0 and len(pattern_month10_16.findall(pay)) == 0)) and len(pattern_nego.findall(pay)) == 0 or len(pattern_seoul.findall(site)) > 0:
                        job_item = IldaoTestWithSeleniumItem()
                        job_item['title'] = title
                        job_item['site'] = site
                        job_item['type'] = type
                        job_item['pay'] = pay
                        job_item['etc1'] = etc1
                        job_item['etc2'] = etc2
                        job_item['etc3'] = etc3
                        #print(etc_set)
                        job_item['numpeople'] = numpeople
                        job_item['phone'] = phone
                        job_item['detail'] = detail
                        job_item['imageURL'] = imageURL
                        job_item['time'] = ''
                        job_item['sponsored'] = ''
                        yield job_item
                
                except Exception as e:
                    print(f"\n\n - - - - - - - - 예외처리 됨 !! (1) - - - - - - - - \n\n{e}\n\n")
                
                else:
                    pass
                    
        # NO_간편지원 and 18만원 이상 완료  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        
        # scrollsection 가장 상단 가기
        '''
        print(f"상단가기  : {ildao_items[0].location_once_scrolled_into_view}")
        time.sleep(2)
        for index, job_item in enumerate(ildao_items):
            if index < first_no_simple:
                job_item.location_once_scrolled_into_view
                time.sleep(.3);job_item.click();time.sleep(.3)
                
        '''
        # 간편지원 and 18만원 이상 완료  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        time.sleep(random.randint(5, 8))
        # 간편지원 아닌 첫 index로 다시 이동 not(일반 17만원 이상 '비계/동바리'는 18만원 이상 가져오기)
        print(f"중단가기  : {ildao_items[first_no_simple].location_once_scrolled_into_view}")
        time.sleep(random.randint(4, 7))
        # time.sleep(2)
        for index, job_item in enumerate(ildao_items):
            if index >= first_no_simple and simple_text_items[index].find('간편지원') == -1:
                try:
                    job_item.location_once_scrolled_into_view
                    time.sleep(random.randint(1, 4));job_item.click();time.sleep(.5)
                    # time.sleep(.3);job_item.click();time.sleep(.3)

                    title_sel = self.driver.find_element(By.CSS_SELECTOR, "#detail_info div.ft5.NotoSansM")
                    title_pre = re.sub('[^a-zA-Z0-9가-힣一-龥_\s\(\)\[\]\-\~\/\,\.\ㆍ\&]', ' ', title_sel.text)
                    title = re.sub('\s{2,9}', ' ', title_pre).strip(' _-~/,.ㆍ&').lstrip(')]').rstrip('([').upper()

                    site_sel = self.driver.find_element(By.CSS_SELECTOR, "div.time.ft11.col_gra04.NotoSansL")
                    site_pre = re.sub('[a-z]+_[a-z]+\s', '', site_sel.text) # "location_on " 없애기
                    site = re.sub('세종 세종', '세종시', site_pre)
    
                    type_sel = self.driver.find_element(By.CSS_SELECTOR, "#detail_info div.ft11 div.ft10")
                    type_pre = re.sub('조공/잡부', '조공/보조', type_sel.text)
                    type = re.sub('시스템/비계', '비계/동바리', type_pre)
    
                    pay_sel = self.driver.find_element(By.CSS_SELECTOR, "#detail_info div.col_blu02.ft10 > div")
                    pay_pre1 = re.sub('\n', ' ', re.sub('0 원', '0원', pay_sel.text))
                    pay_pre2 = re.sub('0,000', '만', pay_pre1)
                    if pay_pre2.find(',000') == -1:
                        pay = re.sub(',', '', pay_pre2)
                    else:
                        pay = re.sub('', '', pay_pre2)
    
                    etcs_sel = self.driver.find_elements(By.CSS_SELECTOR, "#detail_info div.ft11.col_blu02")

                    etc1 = '';etc2 = '';etc3 = ''
                    etc_set = set()
                    for etc in etcs_sel:
                        etc_set.add(etc.text.strip(','))

                    if '숙식제공' in etc_set:
                        etc1 = '숙식제공'
                        if '4대보험' in etc_set:
                            etc2 = '4대보험'
                            if '출퇴근가능' in etc_set:
                                etc3 = '출퇴근가능'
                            elif '장기근무' in etc_set:
                                etc3 = '장기근무'
                        elif '출퇴근가능' in etc_set:
                           etc2 = '출퇴근가능'
                           if '장기근무' in etc_set:
                              etc3 = '장기근무'
                        elif '장기근무' in etc_set:
                           etc2 = '장기근무'
                    elif '4대보험' in etc_set:
                        etc1 = '4대보험'
                        if '출퇴근가능' in etc_set:
                           etc2 = '출퇴근가능'
                           if '장기근무' in etc_set:
                                 etc3 = '장기근무'
                        elif '장기근무' in etc_set:
                            etc2 = '장기근무'
                    elif '출퇴근가능' in etc_set:
                        etc1 = '출퇴근가능'
                        if '장기근무' in etc_set:
                            etc2 = '장기근무'
                    elif '' in etc_set:
                        etc1 = '장기근무'

                    numpeople_int = 0;numpeople_pre = 0
                    num_pattern = re.compile('[0-9]')
                    numpeople_sel_list = self.driver.find_elements(By.CSS_SELECTOR, "#detail_info div.ft11 div.ft10[style='display: flex;']")
                    for numpeople_sel in numpeople_sel_list:
                        if len(num_pattern.findall(numpeople_sel.text)) > 0:    # 숫자가 들어있는 문자열만 가져온다
                            numpeople_int = re.sub('[^0-9]', '', numpeople_sel.text)    # 숫자를 제외한 문자 삭제
                            # print(f"numpeople_int : {numpeople_int}")
                            numpeople_pre += int(numpeople_int)                 # 초보+조공+준공+기공 = 총인원
                    numpeople = f"{numpeople_pre}명"
    
                    phone_sel = self.driver.find_element(By.CSS_SELECTOR, "#detail_info div.ft11 div.ft10.RobotoM")
                    phone = re.sub('', '', phone_sel.text)
    
                    detail_sel = self.driver.find_element(By.CSS_SELECTOR, "#detail_info p.ft10.lin_h2")
                    detail_pre1 = re.sub('\n\n\n\n+', '\n\n\n', detail_sel.text)
                    detail_pre2 = re.sub(' *\*\) *', '\n• ', re.sub(' *\*\] *', '\n• ', detail_pre1)) # 특정 소개소 detail 작성 양식 때문에 바꿔줌 '*]타일용접' (나중에 없애도 됨)
                    detail_pre3 = re.sub(' *\#\)', '◎', re.sub(' *\#\]', '◎', detail_pre2))
                    detail_pre4 = re.sub(' *\@\)', '◎', re.sub(' *\@\]', '◎', detail_pre3))
                    detail_pre5 = re.sub('잇', '있',re.sub('업슴', '없음',re.sub('잇슴', '있음', detail_pre4)))
                    detail_pre6 = re.sub('\n\n\n+', '\n\n',re.sub('//', '/',re.sub('\n {1,9}', '/', detail_pre5)))
                    if detail_pre6.find('• ') != -1:
                        detail = re.sub('', '', detail_pre6)
                    else:
                        detail = re.sub('', '', detail_pre1)
                
                    imageURL_sel = '';imageURL = ''
                    try:
                        imageURL_sel = self.driver.find_element(By.CSS_SELECTOR, "#detail_info > div > div > div > div > img")
                    except Exception as e:
                        imageURL = ''
                    else:
                        imageURL = imageURL_sel.get_attribute('src')
                
                    # not ('시스템비계는 10~17'뺌 / '시스템비계 아니면 10~16뺌' / '협의'뺌)
                    if not(((len(pattern_system.findall(type)) > 0 and len(pattern_day10_17.findall(pay)) == 0 and len(pattern_month10_17.findall(pay)) == 0) or (len(pattern_system.findall(type)) == 0 and len(pattern_day10_16.findall(pay)) == 0 and len(pattern_month10_16.findall(pay)) == 0)) and len(pattern_nego.findall(pay)) == 0 or len(pattern_seoul.findall(site)) > 0):
                        job_item = IldaoTestWithSeleniumItem()
                        job_item['title'] = title
                        job_item['site'] = site
                        job_item['type'] = type
                        job_item['pay'] = pay
                        job_item['etc1'] = etc1
                        job_item['etc2'] = etc2
                        job_item['etc3'] = etc3
                        # print(etc_set)
                        job_item['numpeople'] = numpeople
                        job_item['phone'] = phone
                        job_item['detail'] = detail
                        job_item['imageURL'] = imageURL
                        job_item['time'] = ''
                        job_item['sponsored'] = ''
                        yield job_item

                except Exception as e:
                    print(f"\n\n - - - - - - - - 예외처리 됨 !! (2) - - - - - - - - \n\n{e}\n\n")
                
                else:
                    pass
                    
        
        # NO_간편지원 and 그외 완료  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        # scrollsection 가장 상단 가기
        '''
        print(f"상단가기  : {ildao_items[0].location_once_scrolled_into_view}")
        time.sleep(2)
        for index, job_item in enumerate(ildao_items):
            if index < first_no_simple:
                job_item.location_once_scrolled_into_view
                time.sleep(.3);job_item.click();time.sleep(.3)
                
        '''
        # 간편지원 and 그외 완료  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
        time.sleep(random.randint(2, 22))
        print(f"\n\n\nfirst_no_simple : [{first_no_simple}]\n")# 간편지원 아닌 index 출력
        print(f"\n # # # # # # # # # # # # # # # # # # # # # #   정상종료   # # # # # # # # # # # # # # # # # # # # # #\n\n")
        self.driver.quit()
        pass
