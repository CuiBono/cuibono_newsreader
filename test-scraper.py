#!/usr/bin/env python
#

import sys
from BeautifulSoup import BeautifulSoup
if __name__ == "__main__":
    path = sys.argv[1]
    html = open(path, 'r').read()
    soup = BeautifulSoup(html)
    divs = soup.findAll('div', {'class': 'tet_div'})
    
    print 'found %d divs' % len(divs)
    print divs
    
    for div in divs:
        ps = div.findAll('p')
        for p in ps:
            print p
    
