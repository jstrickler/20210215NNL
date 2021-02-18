import fileinput
from argparse import ArgumentParser
import re

parser = ArgumentParser(description="Faux grep")

parser.add_argument("-i", dest="ignore_case", action="store_true", help="ignore case")
parser.add_argument("-f", dest="show_names", action="store_true", help="show file name")
parser.add_argument("pattern", help="pattern to find")
parser.add_argument("files", nargs="*", help="files to search")

args = parser.parse_args()

if args.ignore_case:
    flag = re.I
else:
    flag = 0

pattern = re.compile(args.pattern, flag)

for raw_line in fileinput.input(args.files):  # sys.argv[1:] by default
    if re.search(pattern, raw_line):
        if args.show_names:
            print(fileinput.filename(), end=' ')
        line = raw_line.rstrip()
        print(line)

