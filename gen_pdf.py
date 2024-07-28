import argparse
import pdfkit
from utils import *
from datetime import datetime

parser = argparse.ArgumentParser(description='Generate a PDF from HTML content.')
parser.add_argument('num', type=int, help='The number of HTML sections to generate')

args = parser.parse_args()

now = datetime.now()
filename=now.strftime("%Y_%m_%d_AMC.pdf")
path=""
path+=filename

allhtml=gen_html(args.num)

pdfkit.from_string(allhtml, path)
print("done")