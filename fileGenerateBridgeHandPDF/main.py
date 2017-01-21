import bridgelib.pdf as pdf
from test import testpdf
from test import parsepbn_test as pbntest

if __name__ == '__main__':
    print 'pbntest.test_mult_tag: '
    print pbntest.test_mult_tag()
    print 'testpdf.test_createPDF'
    testpdf.test_createPDF()
