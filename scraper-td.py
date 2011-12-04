#!/usr/bin/env python
#

import sys
from BeautifulSoup import BeautifulSoup
if __name__ == "__main__":
    path = sys.argv[1]
    html = open(path, 'r').read()
    soup = BeautifulSoup(html)
    divs = soup.findAll('div', {'class': 'post'})
    
    print 'found %d divs' % len(divs)
    
    headline_tags = set(
        ["entry-title"]
    )
    
    date_tags = set(
        ["
    
    body_tags = set(
        ["entry-content"]
    )
    
    transcript_tags = set(
        ["tet-dev"]
    )
    
    
    # HEADLINE , BODY, TRANSCRIPT
    headline = []
    body     = []
    transcript      = []    
    for div in divs:
        classes = set()
        ps = div.findAll('p')
        important = []
        for p in ps:
            c = p.get('class')
            if not c or c in ignore_tags:
                continue
            classes.add(c)
            important.append(p)
        print "-------------"
        print p.text
        if ('tet-dev'):     
            del p['class']
            data = str(p)
            body.append(data)
            print p
        else:
            print important
            for p in important:
                c = p.get('class')
                data = str(p)
            if c in headline_tags:
                headline.append(data)
                print data
            elif c in body_tags:
                body.append(data)
            elif c in transcript_tags:
                transcript.append(data)
        print
        body.append(str(p))


    h = ''.join(headline)
    b = ''.join(body)
    t = ''.join(transcript)
    fields = [h, b, t]
    
        # do some error checking!!
    for f in fields:
        if '\t' in f:
            raise Exception("illegal tab character found!!")
        elif '\t' in f:
            raise Exception('illegal newline character found!!')
    #for i in range(0, len(fields)):
     #   print i
      #  print "---------"
       # print fields[i]		
   # print '\n'.join(fields)
