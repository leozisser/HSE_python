__author__ = '123'
import urllib.request, re, os.path
hrefs = [] #all hrefs that are there on the site
b = urllib.request.Request('http://www.zavety-i.ru', headers = {'User-Agent':"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"})
a = urllib.request.urlopen(b)
page = a.read().decode('utf-8')
wwwpage = open("C:/coding/Python/internetpage.txt", 'w')
hreflist = open("C:/coding/Python/hreflist.txt", 'w')
wwwpage.write(page)
#print(a.getcode)

batch = []
href = re.compile("\?module[^\"\']*")
for line in page:   #почему не находит в page ничего?
    batch = re.findall(href,line)#.split(href)
    for a in batch:
        if a not in hrefs:
            hrefs.append(a)
print (page)
print("hrefs: ", hrefs)
print("batch:", batch)
visited = []
for link in hrefs:
