#more versatile version which you can edit as needed for specific needs
import requests
from bs4 import BeautifulSoup
from csv import writer

#enter website url into quotes
response = requests.get('')

soup = BeautifulSoup(response.text, 'html.parser')

#inspect web element and add class of div you want to start with
posts = soup.find_all(class_='')

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    #sample headers for content, replace with content you're taking as needed
    headers = ['Title', 'Link', 'Date']
    csv_writer.writerow(headers)

    for post in posts:
        #add same class as above and edit what you want as needed, I've included titles, links and dates
        title = post.find(class_='').get_text().replace('\n', '')
        link = post.find('a')['href']
        date = post.select('.post-date')[0].get_text()
        csv_writer.writerow([title, link, date])
