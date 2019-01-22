import requests as r    
from bs4 import BeautifulSoup as bs
from tqdm import tqdm

def FindLastWebPage(url, headers): ### Create this func
    last_page = 95                 ### It should it should return the number of last page  
    ####some code                  ### of current language search (for exmpl. Now last page for python 95,
    ####some code                  ### but tomorrow it may change up to 100-110)
    ####some code
    return last_page



def parser(base_url, headers, jobs):
    #jobs = [];
    session = r.Session()
    request = session.get(base_url, headers=headers)

    if request.status_code == 200:
        soup = bs(request.content, "html.parser")
        divs = soup.find_all("div", attrs= {"data-qa":"vacancy-serp__vacancy"})
        for div in divs:
            title = div.find('a',attrs = {'data-qa':'vacancy-serp__vacancy-title'}).text
            href = div.find('a',attrs = {'data-qa':'vacancy-serp__vacancy-title'})['href']
            company = div.find('a', attrs = {'data-qa':'vacancy-serp__vacancy-employer'}).text
            #compensation = div.find(...........).text
            #requirement = .........
            #metro-station = .... 
            #etc.....

            jobs.append(
                {'title':title, 'href':href, 'company':company} #+ append all previous items
            )

    else:
        print("Error")


headers = {"accept":"*/*" ,"user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

base_url = "https://hh.ru/search/vacancy?search_period=30&clusters=true&area=1&text=python&enable_snippets=true&page=0"


vacancy = {}
language_list = ['python','ruby','javascript','php','golang']
for lang in tqdm(language_list):
    text_url = "https://hh.ru/search/vacancy?search_period=30&clusters=true&area=1&text=%s&enable_snippets=true&page=0"%lang
    jobs = []
    for i in tqdm(range(0,FindLastWebPage(text_url, headers))):
        url = text_url[:-1] + str(i)
        parser(url,headers, jobs)
        #print(lang,len(jobs))
    vacancy[lang] = jobs
