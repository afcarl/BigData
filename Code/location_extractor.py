def location_extractor(tweet):
    symbol_list = [',','.','<','>','/','?',':',';','[',']','{','}','|','\\','=','+','_',')','(','*','^','%','$','#','@','!']
    #note - I delibrately omitted '-' and '&' from this list, because they often form part of the place names. but you can put them in again.
    preposition_list=['at', 'At', 'in', 'In', '@', 'to', 'To', '2', 'From', 'from', 'through', 'Through', 'near', 'Near']
    misleading_list=['want','Want','click', 'Click', 'its', "it's", 'Its', "Its"]
    tweetwords = tweet.split()

#     print "Before: {}".format(tweetwords)
    indx = 0
    for word in tweetwords:
        if word[:1] in symbol_list:
            symb = word[:1]
            indx+=1
            if word[1:]=="":#sometimes symbols are by themselves anyway. 
                continue #This prevents unnecessarily inserting an empty list item
            else:
                tweetwords.insert(indx,word[1:])
                indx-=1
                tweetwords[indx]=symb
        elif word[-1:] in symbol_list:
            symb = word[-1:]
            tweetwords[indx]=word[:-1]
            indx+=1
            tweetwords.insert(indx,symb)
            indx-=1
        indx+=1
#     print "\nAfter: {}".format(tweetwords)
    
    locations = []
    loc_word_flag = False
    misl_flag = False
    loc_initial_flag=False
    for word in tweetwords:
    #     print "\nIn For. Word:{}".format(word)#unnecessary
        if misl_flag == True:
            misl_flag = False
            continue
        elif loc_word_flag == False:
    #         print "in if 1 "#unnecessary
            if word in misleading_list:
                misl_flag = True
                continue
            elif word in preposition_list:
    #             print "in if 2 "#unnecessary
                loc_word_flag=True
                locations.append("")
                location_words=0
                continue
            else:
    #             print "in else 3 "#unnecessary
                continue
        else: #this section onwards is for words we think might be locations...
    #         print "in else 4 "#unnecessary
            if location_words==0 and word in symbol_list:
    #             print "in if 5 "#unnecessary
                continue # this enables us to catch locations that are tagged with a '#'
        
        #New code 12:40:
            elif loc_initial_flag==True and word in symbol_list:
                loc_initial_flag=False
                continue 


            elif word not in preposition_list and word not in symbol_list:
    #             print "in if 6 "#unnecessary
                if word[:4]=='http':
                    location_words=0
                    loc_word_flag=False
                    continue
                else:
                    loc_pos=len(locations)-1
                    locations[loc_pos]+=word+" "
                    location_words+=1
        #New code 12:40:
                    if len(word)==1:
                        loc_initial_flag=True
                    if location_words<4:
        #                 print "in if 7 "#unnecessary
                        continue
                    else:
        #                 print "in else 8 "#unnecessary
                        location_words=0
                        loc_word_flag=False
                        continue
            elif word in preposition_list:
    #             print "in else 9 "#unnecessary
                loc_word_flag=True
                locations.append("")
                location_words=0
                continue
            else:
    #             print "in else 10 "#unnecessary
                location_words=0
                loc_word_flag=False
                continue

def location_extractor(tweet):
    symbol_list = [',','.','<','>','/','?',':',';','[',']','{','}','|','\\','=','+','_',')','(','*','^','%','$','#','@','!']
    #note - I delibrately omitted '-' and '&' from this list, because they often form part of the place names. but you can put them in again.
    preposition_list=['at', 'At', 'in', 'In', '@', 'to', 'To', '2', 'From', 'from', 'through', 'Through', 'near', 'Near']
    misleading_list=['want','Want','click', 'Click', 'its', "it's", 'Its', "Its"]
    tweetwords = tweet.split()

#     print "Before: {}".format(tweetwords)
    indx = 0
    for word in tweetwords:
        if word[:1] in symbol_list:
            symb = word[:1]
            indx+=1
            if word[1:]=="":#sometimes symbols are by themselves anyway. 
                continue #This prevents unnecessarily inserting an empty list item
            else:
                tweetwords.insert(indx,word[1:])
                indx-=1
                tweetwords[indx]=symb
        elif word[-1:] in symbol_list:
            symb = word[-1:]
            tweetwords[indx]=word[:-1]
            indx+=1
            tweetwords.insert(indx,symb)
            indx-=1
        indx+=1
#     print "\nAfter: {}".format(tweetwords)
    
    locations = []
    loc_word_flag = False
    misl_flag = False
    loc_initial_flag=False
    for word in tweetwords:
    #     print "\nIn For. Word:{}".format(word)#unnecessary
        if misl_flag == True:
            misl_flag = False
            continue
        elif loc_word_flag == False:
    #         print "in if 1 "#unnecessary
            if word in misleading_list:
                misl_flag = True
                continue
            elif word in preposition_list:
    #             print "in if 2 "#unnecessary
                loc_word_flag=True
                locations.append("")
                location_words=0
                continue
            else:
    #             print "in else 3 "#unnecessary
                continue
        else: #this section onwards is for words we think might be locations...
    #         print "in else 4 "#unnecessary
            if location_words==0 and word in symbol_list:
    #             print "in if 5 "#unnecessary
                continue # this enables us to catch locations that are tagged with a '#'
        
        #New code 12:40:
            elif loc_initial_flag==True and word in symbol_list:
                loc_initial_flag=False
                continue 


            elif word not in preposition_list and word not in symbol_list:
    #             print "in if 6 "#unnecessary
                if word[:4]=='http':
                    location_words=0
                    loc_word_flag=False
                    continue
                else:
                    loc_pos=len(locations)-1
                    locations[loc_pos]+=word+" "
                    location_words+=1
        #New code 12:40:
                    if len(word)==1:
                        loc_initial_flag=True
                    if location_words<4:
        #                 print "in if 7 "#unnecessary
                        continue
                    else:
        #                 print "in else 8 "#unnecessary
                        location_words=0
                        loc_word_flag=False
                        continue
            elif word in preposition_list:
    #             print "in else 9 "#unnecessary
                loc_word_flag=True
                locations.append("")
                location_words=0
                continue
            else:
    #             print "in else 10 "#unnecessary
                location_words=0
                loc_word_flag=False
                continue

>>>>>>> f845cf6db38cbc08153499a61896c78822320d6b
    return locations