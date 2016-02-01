__author__ = '123'
import re, os
def crawler (hrefs, visited):
    for link in hrefs:
        if link in hrefs and link not in visited:
            b = urllib.request.Request('http://www.zavety-i.ru/'+link, headers = {'User-Agent':"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"})
            a = urllib.request.urlopen(b)
            page = a.read().decode('utf-8')


dirr = input('input path to save files:')
os.mkdir(os.path.join(dirr,"1") #созает папку с номером первой текущей поддиректории

def packer(dirr, page,):

    #cntdir = len(os.listdir(dirr)) #считет колчество папок в главной директории ПОСМОТРЕТЬ, ТОЛЬКО ЛИ ПАПОК. Может вынести за цикл?
    cntdir = 1
    cntfile = len(os.listdir(dirr + "/" + str(cntdir))) #считает колисество файлов в данной поддиректории
    #создает папку с номером текущей поддиректории

    if cntfile < 50:
        cur = open (os.path.join(dir, str(cntdir), str(cntfile + 1)+".txt"),'w' )
        cur.write(page)
        return "written to current folder"
    else:
        cntdir +=1
        folder (dirr, cntdir) #создает новую папку с номером на 1 больше
        packer(dirr, page)
        return "new folder needed"

def folder (dirr, cnt): #создает папку с номером  новой текущей поддиректории
    os.mkdir(dirr, cnt)
    return "folder"+str(cnt)+"created"
#1. создается главная директориядиректория
#2. создается первая папка
#3. проводится запись
os.mkdir