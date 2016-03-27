# -*- coding: utf-8 -*-

import nltk, re
import glob
from nltk import RegexpParser
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

st = StanfordNERTagger('/Users/lnt/Dropbox/TM/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz', '/Users/lnt/Dropbox/TM/stanford-ner/stanford-ner.jar', encoding='utf-8')
glob_list = glob.glob('/Users/lnt/Dropbox/TM/text_v1/*/*/*.txt')
text_list = []
mail_list = []

def mail_data(mail_list):
    for doc in glob_list:
        f = open(doc)
        text = f.read().decode('utf8')
        text2 = text.replace('[dot]', '.').replace('[@]', '@').replace('youknowwhat', '@')
        text_list.append(text2)

    for i in text_list:
        mail = re.findall(r'[\w\.-]+@[\w\.-]+', i)
        if mail != [] and (mail[0] not in mail_list):
            mail_list.append(mail[0])

    for j in mail_list:
        if '.com' not in j and '.nl' not in j and '.uva' not in j:
            mail_list.remove(j)

    return mail_list

print mail_data(mail_list)

#OUTPUT = [u'hein.van.den.berg2@gmail.com', u'contactsupport@readspeaker.com', u'm.lamers@vu.nl', u'emiel.van.miltenburg@vu.nl', u'lora.aroyo@vu.nl', u'z.huang@vu.nl', u'frank.van.harmelen@cs.vu.nl', u'guus.schreiber@vu.nl', u'hoekstra@uva.nl', u'wouter@vanatteveldt.com', u'a.m.baars@vu.nl', u'e.j.miedzobrodzka@vu.nl', u'b.beersma@vu.nl', u'j.p.kalkman@vu.nl', u'f.ten.holder@vu.nl', u'sg.sileno@uva.nl', u'a.w.f.boer@uva.nl']
