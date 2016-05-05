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
  lines = sc.textFile("ats.txt",use_unicode=False)
  sqlContext = SQLContext(sc)
  #newrdd = lines.mapPartitions(lambda x:csv.reader(x))
  wc = lines.flatMap(lambda x:x.split('\n')).map(lambda x:(x,1)).reduceByKey(add)
  wc.saveAsTextFile("counts")

