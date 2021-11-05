from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Edge(executable_path='C:\msedgedriver.exe')

Category = []
Image = []
Name = []
Developer = []
Rating = []
Price = []
Game_link = []

count_in_loop = 0
count_by_Find = 0
count1=0
for i in range(1, 4268):
    a = f"https://store.steampowered.com/search/?sort_by=_ASC&sort_order=ASC&page={i}"
    try:
        driver.get(a)
        content = driver.page_source
        soup = BeautifulSoup(content)
        catagory_n = "Game"
        for b in soup.findAll('a',attrs={'data-gpnav':'item'}):
            try:
                Name.append(b.find('span',attrs={'class':'title'}).text)
                
                Category.append(catagory_n)
                try:
                    Developer.append(b.find('span',attrs={'class':'platform_img win'}).attrs('class'))
                except:
                    Developer.append("Not Found")
                try:
                    Rating.append(b.find('span',attrs={'class':'search_review_summary'}).attrs['data-tooltip-html'])
                except:
                    Rating.append("Not Found")
                try:
                    Price.append(b.find('div',attrs={'class':'col search_price responsive_secondrow'}).text)
                except:
                    Price.append('free')
                try:
                    Game_link.append(b.attrs['href'])
                except:
                    Game_link.append("Not Found")
                try:
                    Image.append(b.find('img').attrs['src'])
                except:
                    Image.append("Not Found")
                count_in_loop = count_in_loop + 1
            except:
                print('error')
                        
        count_by_Find = count_by_Find + soup.findAll('a',attrs={'data-gpnav':'item'}).__len__()
        print(f"Count by find={count_by_Find} ---- Count in loop={count_in_loop}")
    except:
        print("page not loaded")
df = pd.DataFrame({'GameName':Name, 'Developer': Developer,'Category':Category,'Rating':Rating,'Price':Price,'Image_link':Image,'Game_link':Game_link})
df.to_csv('Games.csv', index=False, encoding='utf-8')