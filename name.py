# -*- coding: utf-8 -*-

import nltk, re
import glob
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
st = StanfordNERTagger('/Users/lnt/Dropbox/TM/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz', '/Users/lnt/Dropbox/TM/stanford-ner/stanford-ner.jar', encoding='utf-8')

glob_list = glob.glob('/Users/lnt/Dropbox/TM/text_v1/*/*/*.txt')
name_list = []

def name_data(name_list):
    for doc in glob_list:
        f = open(doc)
        text = f.read().decode('utf8')
        tokenized_text = word_tokenize(text)
        classified_text = st.tag(tokenized_text)

        for x,y in classified_text:
            if y == 'PERSON' and (x not in name_list):
                name_list.append(x.lower())

    return name_list

print name_data(name_list)


#[u'hein', u'van', u'den', u'berg', u'philosophie', u'tarski', u'wolff', u'kant', u'monique', u'lamers', u'labyrinth', u'von', u'wegen', u'seite', u'stelle', u'wittgenstein', u'ben', u'stuyvenberg', u'sjiagha-yenimu', u'marind', u'anna', u'kaal', u'eric', u'akkerman', u'tweettekst', u'lourens', u'de', u'vries', u'maaike', u'haak', u'marca', u'schasfoort', u'maurice', u'vliegen', u'nel', u'jong', u'petra', u'bos', u'tina', u'krennmayr', u'emiel', u'miltenburg', u'menu', u'skip', u'piek', u'vossen', u'van', u'tiel', u'antal', u'bosch', u'r.', u'lobanova', u'losse', u'alessandro', u'lopopolo', u'benjamin', u'timmermans', u'lora', u'aroyo', u'roser', u'morante', u'vosssen', u'tommaso', u'caselli', u'walter', u'daelemans', u'harry', u'bunt', u'joel', u'tetreault', u'chantal', u'son', u'dutchsemcor', u'laurens', u'rietveld', u'antske', u'fokkens', u'fred', u'lieburg', u'guus', u'schreiber', u'pompeu', u'fabra', u'sagrada', u'familia', u'serge', u'ter', u'braake', u'delen', u'facebookdelen', u'pinterest', u'geen', u'startpagina', u'abonneren', u'yassine', u'karimi', u'miel', u'groten', u'saskia', u'scheltjens', u'algemeen', u'rijksarchief', u'presentatie', u'de', u'deductie', u'johan', u'witt', u'den', u'haag', u'waalwijk', u'paul', u'trigt', u'binnenhof', u'homepage', u'watson', u'zhisheng', u'huang', u'boelelaan', u'annette', u'ten', u'teije', u'mendeley', u'frank', u'harmelen', u'alan', u'bundy', u'wielinga', u'jacopo', u'urbani', u'pink', u'hondecoeter', u'bob', u'volkskrant', u'spindleruv', u'mlyn', u'dieter', u'fensel', u'james', u'a.', u'hendler', u'carole', u'goble', u'abraham', u'bernstein', u'caroline', u'waij', u'matthew', u'taylor', u'jan', u'top', u'l.', u'rijgersberg', u'j.', u'willems', u'd.', u'm.', u'assem', u'wigham', u'n.', u'p.', u'vorst', u'beulens', u'koenderink', u'bunte', u'f.', u'h.', u'hofstede', u'g.', u'wolfert', u'louw', u'd.', u'broekstra', u'tiffany', u'hulzebos', u'antoine', u'isaac', u'shenghui', u'wang', u'patrice', u'landry', u'genevieve', u'clavel', u'jeroen', u'hoppenbrouwers', u'antonis', u'loizou', u'davide', u'ceolin', u'rinke', u'hoekstra', u'grigoris', u'antoniou', u'groth', u'linkitup', u'stefan', u'schlobach', u'dov', u'gabbay', u'veruska', u'carretta', u'zamborlini', u'cedric', u'pruski', u'marcos', u'da', u'silveira', u'giancarlo', u'guizzardi', u'bill', u'evans', u'horst', u'ajira', u'ceriel', u'jacobs', u'hadoop', u'esper', u'spyros', u'kotoulas', u'reasoner', u'marvin', u'margara', u'chang', u'liu', u'guilin', u'qi', u'jason', u'maassen', u'niels', u'drost', u'thomas', u'scharrenbach', u'boncz', u'mika', u'harth', u'hogan', u'kessel', u'werkhoven', u'kielmann', u'cafaro', u'aloisio', u'maaseen', u'li', u'zeng', u'wielemaker', u'willem', u'hage', u'wouter', u'beek', u'atteveldt', u'christian', u'baden', u'jana', u'diesner', u'arendsen', u'a.m.', u'baars', u'balau', u'bartels', u'c.j', u'beukeboom', u'billedo', u'boeynaems', u'der', u'bom', u'b.', u'brugman', u'bushman', u'j.d', u'eden', u'hamer', u't.', u'hartmann', u'hoeksema', u'hoorn', u'dr.', u'b.k', u'johnson', u'drs', u'kerkhof', u'kleinnijenhuis', u'c.', u'klemm', u'e.j', u'miedzobrodzka', u'oegema', u'j.w', u'r.a.', u'paauwe', u'ranzini', u'spekman', u'sungur', u'tanis', u'veldhuis', u'vermeulen', u'k.', u'welbers', u'mirjam', u'informatie', u'ewa', u'elly', u'konijn', u'lydia', u'krabbendam', u'ulrik', u'sandborg-petersen', u'petersen', u'reinoud', u'oosting', u'beantwoorden', u'dit', u'categorie\xebn', u'naam', u'registreren', u'mis', u'geen', u'greetje', u'corporaal', u'beersma', u'bakker', u'mrs', u'e.', u'bandringa', u'banerjee', u'berkel', u'boersma', u'borst', u'bovenberg', u'f.j.', u'companjen', u'g.f.', u'dijkstra', u'i.', u'drori', u's.', u'duijn', u'dyck', u'j.e', u'ferguson', u'gilder', u'glimmerveen', u'graaf', u'groenewegen', u'i.r', u'hellsten', u'hond', u'jelsma', u'kalkman', u'koerten', u'koster', u'w.', u'kuipers', u'a.h.', u'marrewijk', u'merkus', u'moser', u'mulder', u'ma', u'nerghes', u'nies', u'henk', u'onderdenwijngaard', u'passenier', u'schmidt', u'sijde', u'sleebos', u'spierenburg', u'y.', u'taminiau', u'j.c.', u'teelken', u'veenstra', u'veenswijk', u'verver', u'wakkee', u'wels', u'wieringen', u'j.j.', u'wolbers', u's.b', u'zoest', u'shafa', u'vianen', u'bechtoldt', u'rohrman', u'homan', u'kleef', u'jori', u'julie', u'valk', u'hivos', u'peter', u'besselaar', u'ulf', u'sandstr\xf6m', u'salah', u'sugimoto', u'u.', u'al', u'teresa', u'mom', u'michael', u'dennis', u'beckers', u'firmansyah', u'david', u'irene', u'sinteur', u'idrissou', u'bei', u'wen', u'carolien', u'metselaar', u'gaston', u'heimeriks', u'anne-marie', u'oostveen', u'verbree', u'gurney', u'pleun', u'arensbergen', u'tjerk', u'wardenaar', u'giovanni', u'sileno', u'boer', u'engers', u'shannon', u'vitae', u'joost', u'breuker', u'adriaan', u'groot', u'nico', u'frijda', u'levelt', u'prof', u's.a.', u'cerri', u'blix', u'sebastian', u'schmieg', u'kevin', u'potts', u'tom', u'maarten', u'directie', u'automatisering', u'rijksbelastingen', u'alexander', u'winkels', u'someren', u'finlayson', u'bruneau', u'schloss', u'dagstuhl', u'duval', u'herik', u'loiseau', u'filipe', u'scienza', u'tecnologia', u'sartor', u'ashley', u'hindriks', u'weerdt', u'riemsdijk', u'warnier', u'palmirani', u'pagallo', u'springer', u'janssen', u'macintosh', u'scholl', u'tambouris', u'wimmer', u'trauner', u'verlag', u'abramowicz', u'maciaszek', u'w\u0119cel', u'rosemann', u'atkinson', u'pinto', u'ajani', u'prosser', u'wien', u'casellas', u'francesconi', u'montemagni', u'casanovas', u'governatori', u'ven', u'hupkes', u'&', u'rubino', u'leibniz', u'sijtsma', u'lettieri', u'trompper', u'klarman', u'di', u'bello', u'gordon', u'maat', u'vitali', u'r\xe1tai', u'amrita', u'das', u'andrew', u'niemeyer', u'peperkamp', u'roel', u'oever', u'hitchcock', u'carla', u'kooten', u'bie', u'mother', u'putten', u'en', u'mary', u'foltz']