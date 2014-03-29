
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
import argparse

def set_vector_cut(canvas):
    canvas.setStrokeColorRGB(1, 0, 0)
    canvas.setLineWidth(0.002*inch)

def rect(path, width, height, radius=None, margin=0.1*inch):
    canvas = Canvas(path, pagesize=(width + 2*margin, height + 2*margin))
    set_vector_cut(canvas)

    if radius:
        canvas.roundRect(margin, margin, width, height, radius)
    else:
        canvas.rect(margin, margin, width, height)

    canvas.showPage()
    canvas.save()

parser = argparse.ArgumentParser(description='Create rectangle cut sheets')
parser.add_argument('width', type=float, action='store',
                    help='rectangle width in INCHES')
parser.add_argument('height', type=float, action='store',
                    help='rectangle height in INCHES')
parser.add_argument('-r', '--radius', type=float, action='store', default=None,
                    dest='radius', help='corner radius in INCHES')
parser.add_argument('-m', '--margin', type=float, action='store', default=0.1,
                    dest='margin', help='page margin in INCHES')
parser.add_argument('-o', '--output', type=str, default='rect.pdf', 
                    dest='output', action='store', help='output pdf file')

args = parser.parse_args()
for arg in ['width', 'height', 'radius', 'margin']:
    value = getattr(args, arg)
    if value: setattr(args, arg, value*inch)

rect(args.output, args.width, args.height, 
     radius=args.radius, margin=args.margin)