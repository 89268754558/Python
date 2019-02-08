import requests as r    
from bs4 import BeautifulSoup as bs
import time
from tqdm import tqdm
import sqlite3

####SQLITE PART STARTED###########

conn = sqlite3.connect('hh_parse.db') 
cur = conn.cursor() 

def db_creation():
    cur.execute("CREATE TABLE IF NOT EXISTS  parseData (lang TEXT,title TEXT, href TEXT, company TEXT, req TEXT, comp TEXT)")


def dynamic_data_add(lang, title, href, company, req, comp):
    cur.execute("INSERT INTO parseData VALUES('%s', '%s','%s', '%s','%s', '%s')"%(lang, title, href, company,req,comp))
    conn.commit()

#####SQLITE PART FINISHED#######


db_creation()

def find_count(language):
    url = "https://hh.ru/search/vacancy?search_period=30&clusters=true&area=1&text=%s&enable_snippets=true&page=0"%(language)
    session = r.Session()
    request = session.get(url, headers=headers)
    if request.status_code == 200: 
        soup = bs(request.content, "html.parser")
        try:
            pager = soup.find_all("a", attrs = {"data-qa":"pager-page"})
            return int(pager[-1].text)-1
        except :
            return -1

def parser(language, base_url, headers, jobs):
    print("Parser is working!")
    #jobs = [];
    session = r.Session()
    request = session.get(base_url, headers=headers)

    if request.status_code == 200:
        soup = bs(request.content, "lxml")
        divs = soup.find_all("div", attrs= {"data-qa":"vacancy-serp__vacancy"})
        for div in divs:
            try:
                title = div.find('a',attrs = {'data-qa':'vacancy-serp__vacancy-title'}).text
                href = div.find('a',attrs = {'data-qa':'vacancy-serp__vacancy-title'})['href']
                company = div.find('a', attrs = {'data-qa':'vacancy-serp__vacancy-employer'}).text
                compensation = div.find('a', attrs = {'data-qa':'vacancy-serp__vacancy-compensation'}).text
                requirements = div.find('a', attrs = {'data-qa':'vacancy-serp__vacancy_snippet_requirement'}).text

                dynamic_data_add(language, title, href, company,compensation, requirements)  
            except :
                pass
    else:
        print("Error")


def url_changer(language):
    return "https://hh.ru/search/vacancy?search_period=30&clusters=true&area=1&text=%s&enable_snippets=true&page=0"%(language)

def parse_all(language):
    jobs = []
    last_page = find_count(language)
    url_worked = url_changer(language)
    for i in range(0, last_page):
        url = url_worked[:-1] + str(i)
        parser(language , url, headers, jobs)

    return jobs








headers = {"accept":"*/*" ,"user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
#print(parse_all("Php"))

languages = ['Python','Golang','JavaScript','Rust','Ruby','Java','PHP','Haskel']
for i in languages:
    parse_all(i)


cur.close()
conn.close()  