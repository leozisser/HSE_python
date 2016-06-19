__author__ = '123'
#-*- coding: utf-8 -*-
import re, os, urllib.request

startinglink = ("http://zavety-i.ru/")
links = []
done_links = []

regex = re.compile("\?module[^\"\']*")

dirr = input('input path to save files:')


#done = open(os.path.join(dirr,"done.txt"),"a+")
#done1 = re.findall("\?module[^\"\']*",done.read.decode(utf-8))
#for i in done:
#    done_links.append(i)
#gathered = open(os.path.join(dirr,"gathered.txt"), "a+")
#gathered1=re.findall("\?module[^\"\']*",gathered.read.decode(utf-8))
#for j in gathered:
#    links.append(j)

if not os.path.exists(os.path.join(dirr,"1")):
    os.mkdir(os.path.join(dirr,"1"))
     #созает папку с номером первой текущей поддиректории

def packer(page, dirr):

    cntdir = len(os.listdir(dirr)) #считет колчество папок в главной директории ПОСМОТРЕТЬ, ТОЛЬКО ЛИ ПАПОК. Может вынести за цикл?
    print("init cntdir =", cntdir)
    cntfile = len(os.listdir(dirr + "/" + str(cntdir))) #считает колисество файлов в данной поддиректории
    print("current cntfile =", cntfile)
    #создает папку с номером текущей поддиректории

    if cntfile < 50:
        cur = open (os.path.join(dirr, str(cntdir), str(cntfile + 1)+".txt"),'w')
        cur.write(page)
        print ("page "+str(cntfile)+" written to  folder "+str(cntdir))
    else:
        cntdir +=1
        print("cntdir =", cntdir)
        os.mkdir(os.path.join(dirr,str(cntdir)))
        print ("folder"+str(cntdir)+"created") #создает новую папку с номером на 1 больше
        packer(page, dirr)
        return "new folder needed"


def download(href):
    b = urllib.request.Request('http://www.zavety-i.ru/'+ href, headers = {'User-Agent':"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"})
    a = urllib.request.urlopen(b)
    if href in links:
        links.remove(href)
        done_links.append(href)
#        done.wtite(str(href) + " ") #пишем в конец файлика памяти пройденных ссылок
    page = a.read().decode('utf-8')
    packer(page, dirr)
    batch = re.findall("\?module[^\"\']*",page)
    for link in batch:
        if link not in links and link not in done_links:
            links.append(link)
#            gathered.write(link + " ") #пишем в конец файлика памяти непройденных ссылок

download("/")
if links != []:
    for k in links:
        download(k)

else:
    print("links empty!")