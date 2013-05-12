import feedparser
import re



def setTags (*args):
    #return args #this causes a string formatting error
    return list(args)


#put this in a function

tags = ['python','gnu','c++','WordPress']
print "LOOKING FOR FEEDS with the following tags: "
for tag in tags:
    print "* %s" %tag 
matched = list()
filtered = list()
def extendTags(*args):
    while True: 
        resp = raw_input("do you wish to extend list of tags (y/n) ?  \n >>> ")
        if resp == 'Y' or resp =='y':
            add = raw_input ('enter new tag \n >>> ')
            if add in tags:
                print 'this tag is already in the existing list' 
            else:
                tags.append(add)
        else:
             break
extendTags()

def feedQuerySummary(*args):
    if len(matched) == 0:
        print "\n:( :( :( no matches for this feedTitle"
    else:                    
        print "\n$$$$$$ FOUND: matched tags count for this feedTitle %d , here are the matched %r " %(len(matched),matched)
        print "\n$$$$$$ HERE IS THE FILTERED FEED (by titles) \n"
        for feed in filtered:
            print feed.title  

def findMatches(*args, **kwargs):
    print "feed # %r" %(args[0])
    matchStatus = False
    for tag in tags:
        if tag.lower() in args[0].lower():
            matched.append(tag)
            matchStatus = True
            
    return matchStatus

def gatherFeedTitles(*args, **kwargs):
    feeds = feedparser.parse('https://news.ycombinator.com/rss')

    for feed in  feeds.entries:
        if findMatches(feed.title):
            filtered.append(feed)
      
gatherFeedTitles()
feedQuerySummary()
'''
    # SYNTAX ERRORS graveyard 

    # print is a stm not a func so it can't be inside the list compr expression
    [print tag for tag in tags]

'''
