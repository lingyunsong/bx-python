"""
Tests for `bx.seq.nib`.
"""

import unittest
import sys
import os.path
import nib

test_nib = "test_data/seq_tests/test.nib"

# Same sequence data as stored in test.nib

valid_seq = "TGGAGGCATTTGTGATTCAATAGATGCAGAAAGAAACCTTCCTAGAGCTG" \
          + "GCGTTCTCTAACTAAAAGTGGAAAGTTCTGAGGAATGAGGACTGTTATAA" \
          + "ATCCCACCCCACACCGCACCTTCTCCAGGGAAGTTTCATGGCCGTGAAGA" \
          + "GGACAGAAAGTGAGAACCAAGATggaactgaataaacaagcttcacactg" \
          + "ttagtttccccatatgcttaccttcccacagatgccaaccttggaggcct" \
          + "aagaggcctagaatattatcctttgtctgatcatttctctacaaatttat" \
          + "tgttctttgttaagatgctacataagcccaaattctaaccacccctttga" \
          + "gttacccatcatcaagtttctcccatgtg"

valid_seq_len = len( valid_seq )

class NIBTestCase( unittest.TestCase ):

    def setUp(self):
        sys.stdout = None # this causes an AttributeError if any of these
                          # .. tests inadvertently print something

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_get( self ):
        nibfile = nib.NibFile( file( test_nib ) )
        # Try all combinations of even / odd boundaries
        check_get( nibfile, 0, 10 )
        check_get( nibfile, 1, 10 )
        check_get( nibfile, 0, 11 )
        check_get( nibfile, 1, 11 )
        # Test near end of file also
        check_get( nibfile, valid_seq_len - 10, 10 )
        check_get( nibfile, valid_seq_len - 11, 11 )

def check_get( nibfile, start, len ):
    assert nibfile.get( start, len ) == valid_seq[start:start+len]

test_classes = [ NIBTestCase ]
suite = unittest.TestSuite( [ unittest.makeSuite( c ) for c in test_classes ] )
