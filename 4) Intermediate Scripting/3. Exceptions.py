import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename',  help='the first number of lines to read')
args = parser.parse_args()
filename = args.filename
try:
    f = open(filename)
except FileNotFoundError as err:
    print(f"Error: {err}")
else:
    print(f.read())