__author__ = '123'
#-*- coding: utf-8 -*-
import pymysql, csv, codecs, pymysql
data = open("userdata.csv", 'r', encoding='utf-8')



vkread = csv.reader(data, delimiter = "\t", quotechar = '', quoting=csv.QUOTE_NONE)



out =  open("sqlout.txt", 'w', encoding='utf-8')
# next(vkread, None) #how d'you get rid of headers any other way?

sql = pymysql.connect(host='localhost', user='123', passwd='')
c = sql.cursor()
c.execute('create database vkdata')
c.execute('create table vktable (last_name varchar(20), first_name varchar(15), gender varchar(3), bdate varchar(10), religion varchar(3), langs varchar(3), id varchar(10)') #sad but true, i didnt get  the languages out


for i in vkread:
    listed = list(i)
    c.execute('insert into vktable (last_name, first_name, gender, bdate, religion, relations, langs, id)', listed)

cr.close()