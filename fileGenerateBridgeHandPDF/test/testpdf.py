from bridgelib.pdf import *

def test_createPDF():
    f = open('test.pdf', 'wb')
    pdf = createPDF()
    f.write(pdf)
    f.close()



if __name__ == '__main__':
    test_createPDF()
