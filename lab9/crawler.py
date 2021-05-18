from bs4 import BeautifulSoup
import requests
import os
from os import listdir

#code is very specific and created strictly to crawl www.nature.com articles

LOCAL_PATH = "./articles/"
BASE_PATH = 'https://www.nature.com'
SEARCH_PATH = 'https://www.nature.com/search?article_type=protocols,research,reviews&subject='


def save_article(href, tags):
        filename = LOCAL_PATH+href[len(BASE_PATH)+10:]+".txt"
        with open(filename,"a") as f:
            for tag in tags:        
                f.write((tag.text)+"\n")


def crawl_nature():
    subject = input("Choose subject you want to crawl: ")
    no_to_crawl = int(input("Choose number of articles: "))

    #current page
    page = 1
    #crawled articles count
    cnt = 0
    
    while(1):
        res=requests.get(SEARCH_PATH+subject+f"&page={page}")
        bs = BeautifulSoup(res.content,'lxml')

        #get all articles on a search page
        articles = bs.find_all('li',{'class':'mb20 pb20 cleared'})

        if len(articles) == 0:
            break

        for article in articles:

            #if this span is present then article is open access
            if article.find('span',{'class':'upper text-orange'}):
                article_url = article.find('a',{'itemprop':'url'})['href']
                href = BASE_PATH + article_url

                if article_url[10:]+".txt" not in listdir(LOCAL_PATH):
                    print(href)
                    res=requests.get(href)
                    article_bs=BeautifulSoup(res.content,'lxml')

                    article_title = article_bs.find_all('h1',{'class':'c-article-title'})
                    save_article(href,article_title)
                    


                    #all sections that will be crawled, usually those all all the sections
                    #that contain content we want to obtain, ommiting references etc.
                    sections_found = 0
                    section_titles = (["Abstract","Introduction","Background","Results","Discussion","Data","Model","Results and discussion","Results and applications"
                    "Conclusions","Methods",])

                    for section_title in section_titles:
                            section = article_bs.find('section',{'data-title':section_title})
                            if section:
                                sections_found+=1
                                paragraphs = section.find_all("p")
                                save_article(href,paragraphs)
                
                    if sections_found >=4:            
                        cnt+=1
                    #if article structure didn't follow the standard
                    else:
                        os.remove(LOCAL_PATH+href[len(BASE_PATH)+10:]+".txt")
                    if cnt == no_to_crawl:
                        return
        page+=1

    print("No more articles available")


crawl_nature()





