from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
header = {'User-Agent' : 'Mozilla/5.0'}
#a = urlopen("https://www.melon.com/chart/index.htm"+header)
urladd = "https://www.melon.com/chart/index.htm"
mod_url = urllib.request.Request(urladd, headers = header)
print(mod_url)

htmlcontent1 = urllib.request.urlopen(mod_url).read()
verification1 = BeautifulSoup(htmlcontent1, "html.parser")


music_title = verification1.select('.ellipsis.rank01')

tot_count = 0
for count in music_title:
    tot_count +=1
print(tot_count)
for song in range(tot_count):
    print(str(song), music_title[song].text, end = "")
print("=====================")
"""
soup = BeautifulSoup(response.read(), "html.parser")
print(soup.title)

music = soup.find_all('div','ellipsis rank01')

print(music)
"""
"""
i=1
for a in music:
    print("%d위 : %s"%(i, a.find('a').text))
    i = i+1
"""