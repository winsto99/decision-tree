# applydt.py
# Applies a decision tree to a test file and classifies the data

import sys
from dt_io import *
from Tree import *


def classify(att, dt):
    '''
    Classify a single set of attributes, given a decision tree
    '''
    return '1'


def parse_test_file(filename):
    '''
    Parses a test file of comma-separated attributes into a list of
     lists of attributes
    '''
    data = []
    thefile = open(filename, 'r')
    [data.append(l.strip().split(',')) for l in thefile]
    thefile.close()
    return data


def write_output_file(c, att, filename):
    '''
    Writes classes and attributes to file filename
    '''
    outstr='\n'.join([[c[i]+','+''.join(att[i])][0] for i in range(0,len(c))])
    thefile = open(filename, 'w')
    thefile.write(outstr)
    thefile.close()


def apply_decision_tree(test_data_fn, dt_fn, output_fn):
    print "Applying decision tree "+dt_fn+" to test file "+test_data_fn+" ..."
    att = parse_test_file(test_data_fn)
    dt = load_dt(dt_fn)
    classes = [classify(a, dt) for a in att]
    write_output_file(classes, att, output_fn)
    print "Done! Classified attributes stored in "+output_fn


#Apply decision tree on data in passed file
apply_decision_tree(sys.argv[1], sys.argv[2], sys.argv[3])

