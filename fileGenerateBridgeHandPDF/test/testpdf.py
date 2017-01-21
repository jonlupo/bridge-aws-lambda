from bridgelib.pdf import *

def test_createPDF():
    f = open('createPDF.pdf', 'wb')
    pdf = createPDF()
    f.write(pdf)
    f.close()

def test_drawtext():
    buffer = StringIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setLineWidth(.3)

    draw_text(canvas=p, text="Hi")
    draw_text(canvas=p, text="Hi", size=80)
    draw_text(canvas=p, text="Hi", size=20, origin=[132,423])
    draw_text(canvas=p, text="Hi", size=20, origin=(42,423), color=(255,255,0))
    draw_text(canvas=p, text="Hi", size=40, origin=(300,100), color=[0, 0, 255], font="ZapfDingbats")
    f = open('drawtext.pdf', 'wb')
    p.save()
    buffer.reset()
    r = buffer.read()
    buffer.close()
    f.write(r)
    f.close()



if __name__ == '__main__':
    test_createPDF()
    test_drawtext()
