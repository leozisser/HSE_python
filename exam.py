__author__ = 'Leo'
#-*- coding: utf-8 -*-
import csv
import pandas as pd
import re
"""
читаем датафрейм, делаем по словарю для каждого из параметров, по которым выравниваем подкорпус;
делаем регулярку, которaя ловит все значения параметра, для каждого значения по группе;
прогоняем регуляркой каждую ячейку соотв. столбца
если в регулярке срабатывает некоторая по номеру группа(+=1, потому что считаем с нуля),от соответств значения отнимаем -= word_count, а в выходной документ записываем соотв строчку большого дока
если лимит превышен, останавливаемся. балансировка так себе, но грубо сойдет.
ох, боюсь, не допишу я вовремя.
"""


subcorp = open("subcorp.txt", 'w', encoding='utf-8')
re_sphere = re.compile(('художественная')|('церковно-богословская')|('публицистика')|('мемуары')|('Учебно-научная')|('Офиц-деловая')|('Церковно-богословская')|('Бытовая+электронная комм')|('Производственно-техн')|('реклама'))
re_date = re.compile(('1950-60')|('1961-70')|('1971-80')|('1981-90')|('1991-00')|('2001-10')|('2011-15'))


spheredict = {'1':40000000, '2':11000000, '3':29000000, '4': 12000000, '5': 1500000, '6':1500000, '7':3600000, '8':900000, '9':500000}

datedict = {'1':15000000,'2':15000000,'3':12000000,'4':15000000,'5':10000000,'6':15000000,'7':15000000}

df = pd.read_csv('source_post1950_wordcount.csv')

for i in df:
    for j in [9]:
        if re.match(re_date,i).mgroup(j)!= None:
            datedict[str(j)]-= df.words[i]     #no time to find out
    for j in [7]
        if re.match(re_sphere, df.sphere[i])!=None:
            if spheredict[str(j)]>=0:
                spheredict[str(j)]-= df.words[i]
                subcorp.write(i)            #VEEEERRRRRRYYYYY baaaad but could work m a y b e . . .
            else:
                pass



"""
дальше говорим, что если хотя бы в одном словаре не осталось положит значений, BREAK/
получаем то что получаем  
"""


# corp =  open('source_post1950_wordcount.csv', 'r', encoding='utf-8')
# read = csv.reader(corp, delimiter = ',')
#
# for row in read:
#         content = list(row[i] for i in included_cols)
subcorp.close()
