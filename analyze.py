#!/usr/local/bin/python

import sys
from zipfile import ZipFile

for input_path in sys.argv[1:]:
    print "\n    Analyzing %s\n" % input_path
    print "-"*(14+len(input_path)+4)
    if input_path.endswith(".zip"):
        zf = ZipFile(input_path, 'r')
        input_fh = zf.open(zf.infolist()[0])
    else:
        input_fh = open(input_path)

    as_str = ''.join(
            [line.split('\t')[3].strip() for line in input_fh
                if line.startswith('#') == False ])
    print "Read in %d genotype components" % len(as_str)
    print "  First occurence of 'GATTACA' @ %d" % as_str.find('GATTACA')
    print "   Last occurence of 'GATTACA' @ %d" % as_str.rfind('GATTACA')
    print " Total occurences of 'GATTACA' = %d" % as_str.count('GATTACA')
    print " Kitty score (# of 'CAT's)     = %d" % as_str.count('CAT')
    print " Who's it? (# of 'TAG's)       = %d" % as_str.count('TAG')
    print " GATT compliance               = %d" % as_str.count('GATT')
    print
    g_count = sum(1 for c in as_str if c == 'G')
    a_count = sum(1 for c in as_str if c == 'A')
    t_count = sum(1 for c in as_str if c == 'T')
    c_count = sum(1 for c in as_str if c == 'C')
    jonx = sum(1 for c in as_str if c not in ['G', 'A', 'T', 'C'])
    print "Found %d G's" % g_count
    print "Found %d A's" % a_count
    print "Found %d T's" % t_count
    print "Found %d C's" % c_count
    print "Found %d something elses" % jonx
