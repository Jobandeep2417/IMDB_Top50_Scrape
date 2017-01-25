import urllib2
import sys
from BeautifulSoup import BeautifulSoup
from tqdm import tqdm
year = str(int(raw_input('Enter the year: ')))
sys.stdout = open('IMDB_Top_50_' + year + '.txt', 'w')
opener = urllib2.build_opener()
opener.addheaders = [('User-agent','Mozilla/5.0')]
url = "http://www.imdb.com/search/title?release_date=" + year + "," + year + "&title_type=feature"
ourUrl = opener.open(url).read()
soup = BeautifulSoup(ourUrl)
article = soup.find('div', attrs={'class': 'article'}).find('h1')
print article.contents[0] + ': '
lister_list_contents = soup.find('div', attrs={'class': 'lister-list'})
i = 1
itermovie = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
for div in tqdm(itermovie):
    print str(i) + '.',
    header = div.findChildren('h3', attrs={'class': 'lister-item-header'})
    for item in header:
        title = header[0].findChildren('a')
        print 'Movie: ' + str(title[0].contents[0])
    genre = div.findChildren('span', attrs={'class': 'genre'})
    genre_contents = genre[0].text.encode('utf-8').decode('ascii', 'ignore')
    print 'Genre: ' + genre_contents
    description = div.findChildren('p', attrs={'class': 'text-muted'})
    description_text = description[0].text.encode('utf-8').decode('ascii', 'ignore')
    print 'Description: ' + description_text
    i += 1
