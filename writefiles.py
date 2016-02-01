__author__ = '123'
import re, os
page = open("C:/coding/Python/internetpage.txt", 'r')
href = re.compile("\?module[^\"\']*")
hrefs = []
batch = []
for line in page:
    result = re.findall(href,line)#.split(href)
    if result != []:
        batch.append(result)
for a in batch:
    if a not in hrefs:
        hrefs.append(a)
print("hrefs: ", hrefs)
print("batch:", batch)
for link in hrefs:
