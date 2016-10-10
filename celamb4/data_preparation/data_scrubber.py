#!/usr/bin/env python

import logging
import sys
import re

def main(argv):

    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)
    titles = open('titles.html', 'w')
    rows = 0

    with open('raw.html', 'r') as data:
        for line in data:
            if 'FM_MC_CourseTitle' in line:
                titles.write("%s," % re.sub('<[^<]+?>', '', line.strip().replace("'","")))
                rows += 1


    titles.close()
    logging.info('Found %d course titles' % rows)

if __name__ == "__main__":
    main(sys.argv)
