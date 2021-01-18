#!/bin/python


from ..readOif import readOif
from ..PPreadColoursUser import PPreadColoursUser


def test_PPreadColoursUser():
     
     resval=0.6
     
     padain=readOif('./data/test/oiftestoutput')
     padafr=PPreadColoursUser(padain, 'r-X', 0.6, 0.0)
     
     val=padafr.at[0,'r-X']
     
     assert resval==val
     
     return