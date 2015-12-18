# -*- coding: utf-8 -*-
import sys
def ipageo(line):

   ipa = {'ბ':'b','დ':'d','ძ':'dz','ჯ':'dʒ','გ':'ɡ','ღ':'ɣ','ჰ':'h','კ':'kʼ',
          'ქ':'kʰ','ლ':'l','მ':'m','ნ':'n','პ':'pʼ','ფ':'pʰ','ყ':'qʼ','რ':'r',
          'ს':'s','შ':'ʃ','ტ':'tʼ','თ':'tʰ','წ':'tsʼ','ც':'tsʰ','ჭ':'tʃʼ',
          'ჩ':'tʃʰ','ვ':'v','ხ':'x','ზ':'z','ჟ':'ʒ','ა':'ɑ','ე':'ɛ','ი':'i','ო':'ɔ','უ':'u'}

   for char in ipa:
      line = line.replace(char, ipa[char])
      #print(char)
   return line
out = open(sys.argv[1],'w',encoding='utf-8')
with open(sys.argv[2], 'r', encoding='utf-8') as inn:
   for line in inn:
      out.write(ipageo(line))
       


#k = input("name:")
#out = open(sys.argv[1],'w',encoding='utf-8')
#out.write(ipageo(k))
