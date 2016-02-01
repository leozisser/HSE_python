__author__ = '123'
import codecs
amh = open ('C:/coding/Python/amhar.tsv','r', encoding='utf-8')
chars = [line.split()for line in amh]
amhdict = {}
for y in chars:
    for x in y:
        amhdict[chars[int(x)][int(y)]]

rerere = str(lines)
res = open ('C:/coding/Python/amhtest.txt','w', encoding = 'utf-8')
res.write(rerere)
setpath = input("set path for in/out", )
with open(setpath, 'r', encoding='utf-8') as inn:
    for line in inn:
        for
for line in lines:
    for i in line:
