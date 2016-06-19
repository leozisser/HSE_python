__author__ = '123'
import requests, csv, time, os

if not os.path.exists("vkdata"):
    dirr = os.mkdir("vkdata")

token = '1caa182d8573f016c008f205fdbd6cede8292ba0fdff302b09758366a982868b264bc90b3d596b29f5cb5'

userdata = open("userdata.csv", "w", newline='', )
datawriter = csv.writer(userdata, delimiter = "\t", quotechar = '', quoting=csv.QUOTE_NONE)
datawriter.writerow (['user_id', 'Name', 'Gender', 'Birth_Date', 'religion', 'relations', 'languages'])#krasnoselkup

fields = "bdate, sex, education, relation, religion, school"#learn what 'personal' is and maybe add

userlink = 'https://api.vk.com/method/users.search'
wallink =  'https://api.vk.com/method/wall.get'

params_s = {"access_token":token, "country":1, "city": 2123, "fields":fields, "count":10}

fields = {'first_name':1, 'last_name':1, 'sex':2,'uid':0, 'bdate':3, 'religion':4, 'relation':5, 'langs':6}

crawler = requests.get(userlink, params = params_s)

batch = crawler.json()

text_fields = {'first_name':1, 'last_name':1, 'sex':2,'uid':0, 'bdate':3, 'religion':4, 'relation':5, 'langs':6}

# for man in batch['response'][1:]:
#     line = {""*8}
#     for feature in man:
#         print__author__ = '123'
import requests, csv, time, os
token = '1caa182d8573f016c008f205fdbd6cede8292ba0fdff302b09758366a982868b264bc90b3d596b29f5cb5'

if not os.path.exists("vkdata"):
    dirr = os.mkdir("vkdata")

userdata = open(os.path.join("vkdata", "userdata.txt"), "w", )
# datawriter = csv.writer(userdata, delimiter = "\t", quotechar = '', quoting=csv.QUOTE_NONE)
# datawriter.writerow ([ 'Last Name','First Name', 'Gender', 'Birth_Date', 'religion', 'relations', 'languages', 'user_id',])#krasnoselkup
userdata.write( 'Last Name'+'\t'+ 'First Name'+'\t'+ 'Gender'+'\t'+ 'Birth_Date'+'\t'+ 'religion'+'\t'+ 'relations'+'\t'+ 'languages'+'\t'+ 'user_id',)
fields = "bdate, sex, education, relation, religion, school, personal, langs"#learn what 'personal' is and maybe add

userlink = 'https://api.vk.com/method/users.search'
wallink =  'https://api.vk.com/method/wall.get'

params_s = {"access_token":token, "country":1, "city": 2123, "fields":fields, "count":100}

# textfields = {'first_name':1, 'last_name':0, 'sex':2,'uid':7, 'bdate':3, 'religion':4, 'relation':5, 'langs':6}
textfields = ['last_name', 'first_name', 'sex', 'bdate', 'religion', 'relation', 'langs', 'uid']
crawler = requests.get(userlink, params = params_s)


def wall(id):
    cur =  open(os.path.join("vkdata",str(id)) +'.txt', 'w', encoding='utf-8')
    params_w = {'owner_id':id,'count':15,'filter':'owner'}
    dump = requests.get(wallink, params=params_w)
    posts = dump.json()

    try:
        for post in posts['response'][1:]:
            post['text'] = post['text'].replace('<br>','\n')
            cur.write(post['text'] + '\n')
    except:
        pass


batch = crawler.json()
# print(batch)
#print(batch['response'][1])
for man in batch['response'][1:]:
    line = ''
    for feature in textfields:
        try:
            line +=str(man[feature]).replace('\t',' ')+'\t'
            print(line)
        except:
            line+= "n\\a"+'\t'
    userdata.write('\n'+line)
    uid = [man['uid']]

    wall(uid)

userdata.close()
# batch['response']
print (batch)