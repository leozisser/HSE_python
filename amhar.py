
amh = open ('C:/coding/Python/amhar.tsv','r', encoding='utf-8')
a = [line.split()for line in amh]
x = a[0]
#print(x)
y = []
test = open ("C:/coding/Python/amhtest2.txt", "w", encoding="utf-8")
for k in a:
        y.append(k[0])

b = {}
for i in a[1:]:
    for j in i[1:]:
        b[j]=y[a.index(i)]+x[i.index(j)]
#test.write(str(b))



def amhar(line):

   for char in b:
      line = line.replace(char, b[char])
   return line

inn = open ('C:/coding/Python/amh.txt','r', encoding='utf-8')
for line in inn:
    test.write(amhar(line))