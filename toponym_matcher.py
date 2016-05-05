import re, pprint
import pandas as pd
import numpy as np
import collections
from pyspark.sql import SQLContext
import nltk
from pyspark.sql.types import *
import difflib
from pyspark import SparkContext, HiveContext
# sc = SparkContext(appName = "test")
from operator import add
import csv
from pyspark.sql import *
from difflib import SequenceMatcher



if __name__=="__main__":
  sc = SparkContext(appName = "test")
  lines = sc.textFile("op1.txt",use_unicode=False)
  sqlContext = SQLContext(sc)
  newrdd = lines.mapPartitions(lambda x:csv.reader(x))

  #sd = {}
  def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

  def mapper(key):
      sd = {}



      if key not in sd.keys():
         if sd.keys()!=[]:

                for elem in sd.keys():
                        if SequenceMatcher(elem,key)>0.5:
                                sd[elem] = key

                        else:
                                sd['key']= key

                yield(sd)

         else:
           sd['key'] = key
           yield(sd)


  values = newrdd.map(lambda x:list(mapper(x)))
  values.saveAsTextFile("output2")
