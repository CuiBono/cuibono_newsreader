#!/usr/bin/env python
#

import sys
from BeautifulSoup import BeautifulSoup
if __name__ == "__main__":
    #open the file provided by the user
    path = sys.argv[1]
    # put all the data from the file into s
    s = open(path, 'r').read()
    # get the length of the string
    doc = len(s)
    # i is our counter of our current position in s
    i = 0
    # list of divs found in s
    transcripts = []
    # if we have a div, this is the bookmarker for the start of the div
    start = None
    # loop through all of the characters in s
    while i < doc:
        # if we haven't seen a div yet
        if start is None:
            #looking for starting div tag
            if s[i:].startswith("<div class=\"tet_div\""):
                # mark the place of the starting div
                start = i
        # when we already have a div
        else: 
            #find closing div
            if s[i:].startswith("</div>"):
                # get the div and the text within it
                # remove the junky code p tags
                div = s[start:i+6].replace("<p>", "").replace("</p>", "")
                # add the div to our list
                transcripts.append(div)
                # reset start to none so we find the starting place of the next div
                start = None        
        i = i + 1
    # we want to cleanup our output a bit more
    for div in transcripts:
        # parse the div string with beautiful soup
        soup = BeautifulSoup(div)
        # identify script tags
        scripts = soup.findAll('script')
        # remove script tags from the div 
        for script in scripts:
            script.extract()
        #TODO put this in the database
        print soup
        
