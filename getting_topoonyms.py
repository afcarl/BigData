import re, pprint
import pandas as pd
import numpy as np
import collections
from pyspark.sql import SQLContext
import nltk
import difflib
from pyspark import SparkContext, HiveContext
sc = SparkContext(appName = "test")
from operator import add
import csv

def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences



if __name__=="__main__":

  rdd = sc.textFile("at_the_rates.csv",use_unicode=False)
  rdd = rdd.mapPartitions(lambda x: csv.reader(x))

  #sc.parallelize(rdd).saveAsTextFile('output')
  newrdd = rdd.map(lambda x: x[3])

  pos_places = []
  def mapper(sent1):
    pos_places1 = []
    sent1 = str(sent1)
    if " at " in sent1:
#            pos_places1 = []
            try:
                #i = i+1
                #print sent1
                sent2_l = sent1.split(' in ')
                #print sent2_l
                sent3_l = []

                if len(sent2_l)==2:
                    sent3_l = sent2_l[-1].strip().split()[:2]
                elif len(sent2_l)>=2:

                    sent2_l[-1] = sent2_l[-1].split()
                    sent2_l[-2] = sent2_l[-2].split()
                    sent3_l = sent2_l[-1] + sent2_l[-2]

                sent3_l = map(lambda x:re.sub(r'[!@#$;%&*^(),:./\?|=+]','',str(x)),sent3_l)
                sent3_l = map(lambda x:re.sub(r"'s",'',str(x)),sent3_l)
                #print sent3_l


                #print sent3_l,'sent3_l'
                # sent1 = pattern.sub('',sent1)
                #print sent1.split()
                pos = ie_preprocess(sent1)
                #print pos
                grammar = "NP: {<DT>?<JJ>*<NN>}"
                cp = nltk.RegexpParser(grammar)
                result = cp.parse(pos[0])
                fl= [item for sublist in pos for item in sublist]
                fl = collections.OrderedDict(fl)
                #print fl

                if sent3_l!=[]:

                    for l in sent3_l:
                        #print l,'l in the list'
                        try:
                            if fl[l]=='NNP':

                                #   print l
                                pos_places1.append(l)
                        except:
                            pass

            except IOError as e:
                print e
                pos_places1.append(l)
                pass
            if pos_places1!=[]:
                return ''.join(pos_places1)
      ##     pos_places.append(''.join(pos_places1))

  # s c.parallelize(pos_places).saveAsTextFile('output')



  values = newrdd.map(mapper)
  values.saveAsTextFile('output4')

