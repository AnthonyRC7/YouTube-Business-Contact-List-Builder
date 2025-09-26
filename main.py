import time
from selenium import webdriver
from bs4 import BeautifulSoup
import xlsxwriter

urls = [
  'https://www.youtube.com/results?search_query=people+who+make+side+hustle+videos'
  'https://www.youtube.com/results?search_query=Stay+at+home+mum+with+side+hustles'
]

times = 0
row = 0
t = v = d = []
driver = webdriver.Chrome(executable_path='path_of_chrome_driver')
for url in urls:
    driver.get('{}/videos?view=0&sort=p&flow=grid'.format(url))
    while times < 5:
        time.sleep(1)   
        driver.execute_script(
            "window.scrollTo(0, document.documentElement.scrollHeight);")
        times += 1
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')

#Title
titles = soup.findAll('a', id='video-title')
t =[]
for i in titles:
    t.append(i.text)

#Views
views = soup.findAll('span', class_='style-scope ytd-grid-video-renderer')
v = []
count = 0
for i in range(len(views)):
    if i%2 == 0:
        v.append(views[i].text)
    else:
        continue

#Duration
duration = soup.findAll(
    'span', class_='style-scope ytd-thumbnail-overlay-time-status-renderer')
d = []
for i in duration:
    d.append(i.text)

workbook = xlsxwriter.Workbook('file.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, "Title")
worksheet.write(0, 1, "Views")
worksheet.write(0, 2, "Duration")

row = 1
for title, view, dura in zip(t,v,d):
    worksheet.write(row, 0, title)
    worksheet.write(row, 1, view)
    worksheet.write(row, 2, dura)
    row += 1

workbook.close()
