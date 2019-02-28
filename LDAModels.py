# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 12:07:24 2019

@author: nsp133
"""

import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from stopwords import my_stopwords

cv = CountVectorizer()
nmf = NMF()
tf = TfidfVectorizer()
lda = LatentDirichletAllocation()
for i in range(1,2):
    print('Filename result'+str(i))
    data = pd.read_csv('D:\\Savitri\\data\\application\\application-resources\\Results\\results'+str(i) +'.csv',  encoding='ISO-8859-1',error_bad_lines=False)
    
    #data = data[pd.notnull(data['Title'])]
    print(data.head(1))
    
    print('Data Size:= ', len(data))
    #mylist = my_stop_words
    
    my_stop_words = text.ENGLISH_STOP_WORDS.union(["a", "able", "about", "above", "abst", "accordance", "according", "accordingly", "across", "act", "actually", "added", "adj", "adult", "affected", "affecting", "affects", "after", "afterwards", "again", "against", "age", "aged", "ageing", "ah", "all", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "app", "apparently", "approximately", "are", "area", "areas", "aren", "aren't", "aren\'t", "arent", "arise", "around", "as", "aside", "ask", "asked", "asking", "asks", "association", "at", "auth", "available", "away", "awfully", "b", "back", "backed", "backing", "backs", "based", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "began", "begin", "beginning", "beginnings", "begins", "behind", "being", "beings", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "big", "bill", "biol", "both", "bottom", "brief", "briefly", "but", "by", "ca", "call", "came", "can", "can't", "can\'t", "cancer", "cannot", "cant", "caps", "capsule", "capsules", "case", "cases", "cause", "causes", "certain", "certainly", "challenge", "changes", "clear", "clearly", "co", "com", "come", "comes", "common", "con", "condition", "conditions", "contain", "containing", "contains", "could", "couldn't", "couldn\'t", "couldnt", "cry", "date", "de", "dependent", "describe", "detail", "device", "diagnose", "diagnosed", "diagnosis", "did", "didn't", "didn\'t", "differ", "different", "differently", "disease", "diseases", "disorder", "do", "doc", "doctor", "does", "doesn't", "doesn\'t", "doing", "don't", "don\'t", "done", "down", "downed", "downing", "downs", "downwards", "dr", "dr.", "drug", "drugs", "due", "during", "each", "early", "ed", "edu", "effect", "eg", "eight", "eighty", "either", "elder", "elderly", "eleven", "else", "elsewhere", "empty", "end", "ended", "ending", "ends", "enough", "especially", "et", "et-al", "etc", "even", "evenly", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exam", "except", "experience", "face", "faces", "fact", "facts", "far", "feel", "feeling", "felt", "few", "ff", "fifteen", "fifth", "fifty", "fill", "find", "finds", "fire", "first", "five", "fix", "follow", "followed", "following", "follows", "for", "former", "formerly", "forth", "forty", "found", "four", "from", "front", "full", "fully", "further", "furthered", "furthering", "furthermore", "furthers", "gave", "gender", "general", "generally", "get", "gets", "getting", "give", "given", "gives", "giving", "go", "goes", "going", "gone", "good", "goods", "got", "gotten", "great", "greater", "greatest", "group", "grouped", "grouping", "groups", "had", "hadn't", "hadn\'t", "happens", "hardly", "has", "hasn't", "hasn\'t", "hasnt", "have", "haven't", "haven\'t", "having", "he", "he'd", "he'll", "he's", "he\'d", "he\'ll", "he\'s", "hed", "hence", "her", "here", "here's", "here\'s", "hereafter", "hereby", "herein", "heres", "hereupon", "hers", "herself", "hes", "hi", "hid", "high", "higher", "highest", "him", "himself", "his", "hither", "home", "hospital", "how", "how's", "how\'s", "howbeit", "however", "hundred", "i", "i'd", "i'll", "i'm", "i've", "i\'d", "i\'ll", "i\'m", "i\'ve", "id", "ie", "if", "im", "immediate", "immediately", "importance", "important", "in", "inc", "indeed", "index", "information", "instead", "interest", "interested", "interesting", "interests", "into", "invention", "inward", "is", "isn't", "isn\'t", "it", "it'll", "it's", "it\'ll", "it\'s", "itd", "its", "itself", "just", "keep", "keepkeeps", "keeps", "kept", "kg", "kind", "km", "knew", "know", "known", "knows", "large", "largely", "last", "lately", "later", "latest", "latter", "latterly", "least", "less", "lest", "let", "let's", "let\'s", "lets", "like", "liked", "likely", "line", "little", "long", "longer", "longest", "look", "looking", "looks", "ltd", "made", "mainly", "make", "makes", "making", "man", "many", "may", "maybe", "me", "mean", "means", "meantime", "meanwhile", "med", "medication", "medications", "medicine", "medicines", "meds", "member", "members", "men", "merely", "mg", "might", "mill", "million", "mine", "miss", "ml", "more", "moreover", "most", "mostly", "move", "mr", "mrs", "much", "mug", "must", "mustn't", "mustn\'t", "my", "myself", "n", "na", "name", "namely", "nay", "nd", "near", "nearly", "necessarily", "necessary", "need", "needed", "needing", "needs", "neither", "never", "nevertheless", "new", "newer", "newest", "next", "nine", "ninety", "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "nothing", "now", "nowhere", "number", "numbers", "obtain", "obtained", "obviously", "of", "off", "often", "oh", "ok", "okay", "old", "older", "oldest", "omitted", "on", "once", "one", "ones", "only", "onto", "open", "opened", "opening", "opens", "or", "ord", "order", "ordered", "ordering", "orders", "otc])", "other", "others", "otherwise", "ought", "our", "ours", "ourselves", "oursourselves", "out", "outside", "over", "over-the-counter", "overall", "owing", "own", "page", "pages", "part", "parted", "particular", "particularly", "parting", "parts", "past", "patient", "patients", "per", "perhaps", "pharma", "pharmaceutical", "pharmaceuticals", "physician", "physicians", "pill", "pills", "place", "placed", "places", "please", "plus", "point", "pointed", "pointing", "points", "poorly", "possible", "possibly", "potentially", "pp", "predominantly", "prescribe", "prescribed", "prescription", "present", "presented", "presenting", "presents", "previously", "primarily", "probably", "problem", "problemprob", "problems", "probs", "promptly", "proud", "provides", "put", "puts", "que", "quickly", "quite", "qv", "ran", "rather", "rd", "re", "readily", "really", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research", "respectively", "resulted", "resulting", "results", "right", "room", "rooms", "run", "said", "same", "saw", "say", "saying", "says", "sec", "second", "seconds", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "sees", "self", "selves", "sent", "serious", "seven", "several", "shall", "shan't", "shan\'t", "she", "she'd", "she'll", "she's", "she\'d", "she\'ll", "she\'s", "shed", "shes", "should", "shouldn't", "shouldn\'t", "show", "showed", "showing", "shown", "showns", "shows", "side", "side-effect", "side-effects", "sides", "significant", "significantly", "similar", "similarly", "since", "sincere", "six", "sixty", "slightly", "small", "smaller", "smallest", "so", "some", "somebody", "somehow", "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "source", "specialist", "specialists", "specifically", "specified", "specify", "specifying", "state", "states", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "suffer", "sufferingsuffered", "sufficiently", "suggest", "sup", "supply", "sure", "suret", "symptom", "symptoms", "system", "tablet", "tablets", "tabs", "take", "taken", "taking", "task", "tell", "ten", "tends", "test", "testing", "tests", "than", "thank", "thanks", "thanx", "that", "that'll", "that's", "that've", "that\'ll", "that\'s", "that\'ve", "thats", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "there'll", "there's", "there've", "there\'ll", "there\'s", "there\'ve", "thereafter", "thereby", "thered", "therefore", "therein", "thereof", "therere", "theres", "thereto", "thereupon", "these", "they", "they'd", "they'll", "they're", "they've", "they\'d", "they\'ll", "they\'re", "they\'ve", "theyd", "theyre", "thick", "thin", "thing", "things", "think", "thinks", "third", "this", "those", "thou", "though", "thoughh", "thought", "thoughts", "thousand", "three", "throug", "through", "throughout", "thru", "thus", "til", "tip", "to", "today", "together", "too", "took", "top", "toward", "towards", "treatment", "treatments", "trial", "trials", "tried", "tries", "truly", "try", "trying", "turn", "turned", "turning", "turns", "twelve", "twenty", "twice", "two", "type", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "up", "upon", "ups", "us", "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "value", "various", "very", "via", "view", "viz", "vol", "vols", "vs", "want", "wanted", "wanting", "wants", "was", "wasn't", "wasn\'t", "wasnt", "way", "ways", "we", "we'd", "we'll", "we're", "we've", "we\'d", "we\'ll", "we\'re", "we\'ve", "wed", "welcome", "well", "wells", "went", "were", "weren't", "weren\'t", "werent", "what", "what'll", "what's", "what\'ll", "what\'s", "whatever", "whats", "when", "when's", "when\'s", "whence", "whenever", "where", "where's", "where\'s", "whereafter", "whereas", "whereby", "wherein", "wheres", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "who'll", "who's", "who\'ll", "who\'s", "whod", "whoever", "whole", "whom", "whomever", "whos", "whose", "why", "why's", "why\'s", "widely", "will", "willing", "wish", "with", "within", "without", "women", "womens", "won't", "won\'t", "wont", "words", "work", "worked", "working", "works", "world", "would", "wouldn't", "wouldn\'t", "wouldnt", "www", "year", "years", "yes", "yet", "you", "you'd", "you'll", "you're", "you've", "you\'d", "you\'ll", "you\'re", "you\'ve", "youd", "young", "younger", "youngest", "your", "youre", "yours", "yourself", "yourselves", "zero"])
    tfidf = TfidfVectorizer(max_df=0.99, min_df=2, stop_words=my_stop_words)
    data = data[pd.notnull(data['Abstract'])]
    dtm = tfidf.fit_transform(data['Abstract'])
    #print('dtm',dtm[0][0])
    nmf_model = NMF(n_components=30,random_state=0)
    nmf_model.fit(dtm)
    len(tfidf.get_feature_names())
    len(nmf_model.components_)
    #print('model',nmf_model.components_)
    single_topic = nmf_model.components_[0]
    single_topic.argsort()
    single_topic.argsort()[-10:]
    top_word_indices = single_topic.argsort()[-10:]
    #for index in top_word_indices:
        #print('Index',tfidf.get_feature_names()[index])
    for index,topic in enumerate(nmf_model.components_):
        print(f'THE TOP 15 WORDS FOR TOPIC #{index}')
        
        print( [tfidf.get_feature_names()[i] for i in topic.argsort()[-30:]] )
        print('\n')
    dtm.shape
    len(data)
    topic_results = nmf_model.transform(dtm)
    topic_results.shape
    topic_results[0]
    topic_results.argmax(axis=1)
    data['Topic'] = topic_results.argmax(axis=1)
    #my_topic = {0: 'Excercise', 1: '', 2: '', 3:'', 4: '', 5: '' , 6: '',7: '', 8: '', 9:'', 10: '', 11: '' , 12: '',13: 'Brain: Nervous System', 14: 'Life Style', 15:'Genetic', 16: 'quality of Life', 17: 'Cancer' , 18: 'Male Obesity',19: 'Physical Training', 20: 'Dementia'}
    #data['Topic_label'] = data['Topic'].mao(my_topic)
    #data.to_csv('D:\\MC_Aging\\Results\\new_results31.csv', sep=';')
    #print(data.head(100))
