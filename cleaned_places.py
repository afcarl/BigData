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


if __name__=="__main__":
  sc = SparkContext(appName = "test")
  lines = sc.textFile("at_the_rates.csv",use_unicode=False)
  sqlContext = SQLContext(sc)




  lines = lines.mapPartitions(lambda x: csv.reader(x))
  tweets = lines.map(lambda x: x[3])
  tweets.saveAsTextFile("tweets")
