__author__ = '123'
import re, os, urllib.request

startinglink = ("http://zavety-i.ru/")
links = []
done_links = []

regex = re.compile("\?module[^\"\']*")

dirr = input('input path to save files:')
os.mkdir(os.path.join(dirr,"1"))

def download(href):
    b = urllib.request.Request('http://www.zavety-i.ru/'+ href, headers = {'User-Agent':"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"})
    a = urllib.request.urlopen(b)
    links.remove(href)
    done_links.append(href)
    page = a.read().decode('utf-8')
    packer(page, dirr)
    page.readlines()
    for line in page:
        batch = re.findall(href,line)#.split(href)
        for link in batch:
            if link not in links and link not in done_links:
                links.append(link)




def crawler (hrefs, visited):
    for link in hrefs:
        if link in hrefs and link not in visited:
            b = urllib.request.Request('http://www.zavety-i.ru/'+link, headers = {'User-Agent':"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"})
            a = urllib.request.urlopen(b)
            page = a.read().decode('utf-8')


 #������ ����� � ������� ������ ������� �������������

def packer(page, dirr):

    cntdir = len(os.listdir(dirr)) #������ ��������� ����� � ������� ���������� ����������, ������ �� �����. ����� ������� �� ����?
    #cntdir = 1
    cntfile = len(os.listdir(dirr + "/" + str(cntdir))) #������� ���������� ������ � ������ �������������
    #������� ����� � ������� ������� �������������

    if cntfile < 50:
        cur = open (os.path.join(dirr, str(cntdir), str(cntfile + 1)+".txt"),'w')
        cur.write(page)
        return "written to current folder"
    else:
        cntdir +=1
        folder (dirr, cntdir) #������� ����� ����� � ������� �� 1 ������
        packer(page, dirr)
        return "new folder needed"


def folder (dirr, cnt): #������� ����� � �������  ����� ������� �������������
    os.mkdir(dirr, cnt)
    return "folder"+str(cnt)+"created"
#1. ��������� ������� ��������������������
#2. ��������� ������ �����
#3. ���������� ������
