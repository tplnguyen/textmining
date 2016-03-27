# -*- coding: utf-8 -*-
#from codecs import decode
data = dict()
mails = []

def match_list(name_list, mail_list):
    for name in name_list:
        for mail in mail_list:
            if name in mail:
                data[name] = [mail]
                #print("The email adress of ", name," is ",mail)
            elif name not in data and name not in mail:
                data[name] = ["I'm sorry. This staff member's email address in not in our database."]
            elif name in data.keys() and name in str(mail):
                data[name].append(mail)

    return data

match_list(name_list, mail_list)

newfile = open("output.txt", "w+")
for x in data.keys():
    newfile.write(x + "\t" + y + "\n").encode('utf-8')

newfile.close()
#data=decode(data)
