__author__ = '123'
# -*- encoding: utf-8 -*-
import os, re, sys, unicodedata, nltk, string, operator, argparse
#1. гуляем по всем папкам, созданным WikiWxtractor'ом,
#2. по каждому файлу в этой папке
#3. для каждого файла нормализуем строки (приводим к нижнему регистру, удаляем числа, знаки препинания)
#добавляем в общий словарь с ключем токен, значением частота
#сортируем по убыванию и пишем в файл

corpora_dict = {}
#remove_punct_map = dict.fromkeys([i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith("P")], " ")
#punct_table = dict((ord(char), None) for char in string.punctuation)
def makelist (source):
    #remove_numbers_map  = dict.fromkeys([i for i in range(48,58)], " ")
    for line in source:
        #line = line.replace("\d","").translate(punct_table)
        tokens = line.lower().split()
        for token in tokens:
            if token in corpora_dict:
                corpora_dict[token] += 1
            else:
                corpora_dict[token] = 1





inputpath = os.path.abspath(input("specify input directory: "))
output_file = open (os.path.join(input("specify output directory: "), "result.txt"), "a", encoding="utf-8")
for  d, dirs, files in os.walk(inputpath):
    for f in files:
        open(os.path.join(inputpath, f), 'r', encoding = "utf-8", closefd=1)
        makelist(f)
sorted_x = sorted(corpora_dict.items(), key=operator.itemgetter(1), reverse=True)
for tuple in sorted_x:
    output_file.write(str(tuple)+ "\n")

#parser = argparse.ArgumentParser(description='Run Wikilist')
