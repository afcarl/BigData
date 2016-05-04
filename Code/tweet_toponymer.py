"""
Inputs: 
	1) twitter data file name(wih path), 
	2) name of location extractor function to apply, and 
	3) name (with path) of desired output file (ideally, shoud default to input filename+_with_toponym.csv)
Outputs: .csv file which is the same as input, but with an additional column containing the list of toponyms in the file
"""
from __future__ import print_function
import sys
import pandas as pd
from location_extractor import location_extractor
#import priya's function here
functs = { 'location_extractor': location_extractor }#add priya's function to dictionary


def tweet_toponymer(dataframe,extractor_function):
    dataframe['toponym']= dataframe[' "tweet"'].apply(extractor_function)



if __name__=='__main__':
    if len(sys.argv)<4:
        sys.stderr.write('USAGE: python %s <INPUT_CSV> <loc_extrctr_func> <OUTPUT_csv>\n' % sys.argv[0])
        sys.exit(1)


    data = pd.read_csv(sys.argv[1], usecols=['id' , ' "tweet"'])
    tweet_toponymer(data,functs[sys.argv[2]])
    data.to_csv(sys.argv[3])
    print ("Successful. here's the first ouput:")
    print (data.head(1))